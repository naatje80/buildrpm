#! /bin/sh

PACKAGE=$(basename ${1} .spec)
DOCKERNAME=$(echo ${PACKAGE}|tr "[:upper:]" "[:lower:]")
OS=${2}

START=$(date)

function usage {
    echo "Usage: build-rpm.sh <PACKAGE> <OS>"
    exit 0
}

if [[ ${OS} != "centos7" && ${OS} != "centos8" ]]
then
    echo "Currently only centos7 and centos8 are supported"
    usage
fi

if [[ ${OS} == "centos8" ]]
then
    INSTALL_CMD="dnf"
    OS="centos:8"
    REPODIR="CENTOS8"
else
    INSTALL_CMD="yum"
    OS="centos:7"
    REPODIR="CENTOS7"
fi

if [[ ! -e ${PACKAGE}.spec ]]
then
    echo "Rpm spec file does not exist yet!"
    exit 1
fi

BUILDSCRIPT="""
#! /bin/sh
set -o pipefail
spectool -R -g ~/rpmbuild/SPECS/${PACKAGE}.spec
yum-builddep -y ~/rpmbuild/SPECS/${PACKAGE}.spec
rpmbuild -bc ~/rpmbuild/SPECS/${PACKAGE}.spec
if [[ \${?} -ne 0 ]]
then
    exit 1
fi
rpmbuild --short-circuit -bi ~/rpmbuild/SPECS/${PACKAGE}.spec
rpmbuild -bl ~/rpmbuild/SPECS/${PACKAGE}.spec 2>&1| sort -u| grep '^   '| grep -v '(but unpackaged)'| sed 's/^   //'|sed 's/^\(.*\)$/\"\1\"/' > /tmp/package_files.log
sed -i -e 's/\/usr\/bin\//%{_bindir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\/sbin\//%{_sbindir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\/lib64\//%{_libdir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\/include\//%{_includedir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\/libexec\//%{_libexecdir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\/share\/man\//%{_mandir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\/share\/info\//%{_infodir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\/share\/doc\//%{_docdir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\/share\//%{_datadir}\//g' /tmp/package_files.log
sed -i -e 's/\/etc\//%{_sysconfdir}\//g' /tmp/package_files.log
sed -i -e 's/\/run\//%{_rundir}\//g' /tmp/package_files.log
sed -i -e 's/\/var\/lib\//%{_sharedstate-dir}\//g' /tmp/package_files.log
sed -i -e 's/\/usr\//%{_exec_prefix}\//g' /tmp/package_files.log
cat /tmp/package_files.log|egrep -v -e '*[.]cmake\"$|*[.]so\"$|*[.]h\"$|*[.]pc\"$' > /tmp/FILES.LOG
cat /tmp/package_files.log|egrep -e '*[.]cmake\"$|*[.]so\"$|*[.]h\"$|*[.]pc\"$' > /tmp/DEVEL_FILES.LOG
if [[ \$(grep -c '%files devel' /root/rpmbuild/SPECS/${PACKAGE}.spec) -ne 0 ]]
then
    sed -i -e '/%files devel[\s]*$/r /tmp/DEVEL_FILES.LOG' /root/rpmbuild/SPECS/${PACKAGE}.spec
else
    sed -i -e '/%files[\s]*$/r /tmp/DEVEL_FILES.LOG' /root/rpmbuild/SPECS/${PACKAGE}.spec
fi
sed -i -e '/%files[\s]*$/r /tmp/FILES.LOG' /root/rpmbuild/SPECS/${PACKAGE}.spec
rpmbuild --noclean -ba ~/rpmbuild/SPECS/${PACKAGE}.spec
"""

DOCKERFILE="""
FROM ${OS}
USER root
VOLUME /${REPODIR}
RUN yum -y update; \
    ${INSTALL_CMD} -y groupinstall \"Development Tools\"; \
    ${INSTALL_CMD} -y install rpmdevtools yum-utils; \
    yum-config-manager --enable powertools 
RUN mkdir -p ~/rpmbuild/{SPECS,SOURCES}; \
    echo -e '%debug_package %{nil}\n%_rpmdir   /${REPODIR}/RPMS\n%_srcrpmdir   /${REPODIR}/SRPMS\n%_builddir	/tmp/rpmbuild/BUILD\n%_buildrootdir /tmp/rpmbuild/BUILDROOT\n%_sourcedir    %(echo \$HOME)/rpmbuild/SOURCES\n%_specdir   %(echo \$HOME)/rpmbuild/SOURCES' > ~/.rpmmacros
COPY ${PACKAGE}.spec /root/rpmbuild/SPECS
WORKDIR /root/rpmbuild
RUN echo -e '[localrepo]\nname=localrepo\nbaseurl=file:///CENTOS8/RPMS\ngpgcheck=0\nenabled=1' > /etc/yum.repos.d/local.repo 
COPY build.sh /root/rpmbuild
"""


if [[ -d Build ]]
then
    rm -rf Build
fi

mkdir Build
echo "${BUILDSCRIPT}" > Build/build.sh; chmod +x Build/build.sh
SOURCE_FILES=`cat ${PACKAGE}.spec|grep '^Source[0-9]\+:\|^Patch[0-9]\+:' | grep -v -e 'http\|https'|tr -d ' '|cut -d ':' -f2-`
if [[ -n ${SOURCE_FILES} ]]; then DOCKERFILE="${DOCKERFILE}COPY"; fi
for FILE in ${SOURCE_FILES}
do
    if [[ -e ${FILE} ]]
    then
        cp ${FILE} Build/
        DOCKERFILE="${DOCKERFILE} ${FILE}"
    else
        echo "ERROR: Source or patch file ${FILE} not found!"
    fi
done 
if [[ -n ${SOURCE_FILES} ]]; then DOCKERFILE="${DOCKERFILE}  /root/rpmbuild/SOURCES/"; fi

echo "${DOCKERFILE}" > Build/Dockerfile
cp ${PACKAGE}.spec Build/
cd Build
docker build -t ${DOCKERNAME} .
if [[ ${?} == 0 ]]
then
    #docker run --rm -l ${PACKAGE}-build -v /volume1/Sys/repo/rpmbuild/${REPODIR}:/${REPODIR} ${PACKAGE} sh ./build.sh &&
    docker run --name=${DOCKERNAME}-build -v /volume1/Sys/repo/rpmbuild/${REPODIR}:/${REPODIR} ${DOCKERNAME} sh ./build.sh &&
        ( createrepo -v --update /volume1/Sys/repo/rpmbuild/${REPODIR}/RPMS; createrepo -v --update /volume1/Sys/repo/rpmbuild/${REPODIR}/SRPMS; \
            docker rm ${DOCKERNAME}-build ) ||
        ( echo -e "\n############################################################\nERROR Compiling: ${PACKAGE}, opening docker for debugging....\n############################################################";
            docker commit ${DOCKERNAME}-build debug-container; 
            docker rm ${DOCKERNAME}-build; docker run --rm -ti -v /volume1/Sys/repo/rpmbuild/${REPODIR}:/${REPODIR} debug-container /bin/bash )
        #find -type f -newerct "${START}" -exec  && 
fi
