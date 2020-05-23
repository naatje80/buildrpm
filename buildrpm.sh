#! /bin/sh

PACKAGE=$(basename ${1} .spec)
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
rpmbuild -bi ~/rpmbuild/SPECS/${PACKAGE}.spec
if [[ ${?} -eq 0 ]]
then
    rpmbuild -bl ~/rpmbuild/SPECS/${PACKAGE}.spec 2>&1| sort -u|grep '^   '|grep -v '(but unpackaged)'|tr -d ' ' > /tmp/package_files.log
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
    sed -i -e 's/\/var\//%{_localstate-dir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\//%{_exec_prefix}\//g' /tmp/package_files.log
    cat /tmp/package_files.log|egrep -v -e '*.so$|*.h$|*.pc$' > /tmp/FILES.LOG; \
    cat /tmp/package_files.log|egrep -e '*.so$|*.h$|*.pc$' > /tmp/DEVEL_FILES.LOG
    sed -i -e '/%files[\s]*$/r /tmp/FILES.LOG' /root/rpmbuild/SPECS/${PACKAGE}.spec; \
    sed -i -e '/%files devel[\s]*$/r /tmp/DEVEL_FILES.LOG' /root/rpmbuild/SPECS/${PACKAGE}.spec
    rpmbuild -ba ~/rpmbuild/SPECS/${PACKAGE}.spec
fi
"""

DOCKERFILE="""
FROM ${OS}
USER root
VOLUME /${REPODIR}
RUN ${INSTALL_CMD} -y groupinstall \"Development Tools\"; \
    ${INSTALL_CMD} -y install rpmdevtools yum-utils; \
    yum-config-manager --enable PowerTools
RUN mkdir -p ~/rpmbuild/{SPECS,SOURCES}; \
    echo -e '%debug_package %{nil}\n%_rpmdir   /${REPODIR}/RPMS\n%_srcrpmdir   /${REPODIR}/SRPMS\n%_builddir	/tmp/rpmbuild/BUILD\n%_buildrootdir /tmp/rpmbuild/BUILDROOT\n%_sourcedir    %(echo \$HOME)/rpmbuild/SOURCES\n%_specdir   %(echo \$HOME)/rpmbuild/SOURCES' > ~/.rpmmacros
COPY ${PACKAGE}.spec /root/rpmbuild/SPECS
WORKDIR /root/rpmbuild
RUN echo -e '[localrepo]\nname=localrepo\nbaseurl=file:///CENTOS8\ngpgcheck=0\nenabled=1' > /etc/yum.repos.d/local.repo 
COPY build.sh /root/rpmbuild
RUN spectool -R -g ~/rpmbuild/SPECS/${PACKAGE}.spec; yum-builddep -y ~/rpmbuild/SPECS/${PACKAGE}.spec
"""


if [[ -d Build ]]
then
    rm -rf Build
fi

mkdir Build
echo "${BUILDSCRIPT}" > Build/build.sh; chmod +x Build/build.sh
if [[ $(ls -l *.patch 2>/dev/null|wc -c) -ne 0 ]]
then
    cp *.patch Build/
    DOCKERFILE="${DOCKERFILE}COPY *.patch /root/rpmbuild/SOURCES"
fi
echo "${DOCKERFILE}" > Build/Dockerfile
cp ${PACKAGE}.spec Build/
cd Build
#ln -s /mnt/Sys/repo/rpmbuild/${REPODIR}
docker build -v /mnt/Sys/repo/rpmbuild/${REPODIR}:/${REPODIR} -t ${PACKAGE}-build .
if [[ ${?} == 0 ]]
then
    docker run -v /mnt/Sys/repo/rpmbuild/${REPODIR}:/${REPODIR} ${PACKAGE}-build sh ./build.sh &&
        createrepo -v --update /mnt/Sys/repo/rpmbuild/${REPODIR}
        #find -type f -newerct "${START}" -exec  && 
fi