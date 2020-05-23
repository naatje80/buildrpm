
FROM centos:8
USER root
VOLUME /CENTOS8
RUN dnf -y groupinstall "Development Tools";     dnf -y install rpmdevtools yum-utils;     yum-config-manager --enable PowerTools
RUN mkdir -p ~/rpmbuild/{SPECS,SOURCES};     echo -e '%debug_package %{nil}\n%_rpmdir   /CENTOS8/RPMS\n%_srcrpmdir   /CENTOS8/SRPMS\n%_builddir	/tmp/rpmbuild/BUILD\n%_buildrootdir /tmp/rpmbuild/BUILDROOT\n%_sourcedir    %(echo $HOME)/rpmbuild/SOURCES\n%_specdir   %(echo $HOME)/rpmbuild/SOURCES' > ~/.rpmmacros
COPY vlc.spec /root/rpmbuild/SPECS
WORKDIR /root/rpmbuild
RUN echo -e '[localrepo]\nname=localrepo\nbaseurl=file:///CENTOS8\ngpgcheck=0\nenabled=1' > /etc/yum.repos.d/local.repo 
COPY build.sh /root/rpmbuild
RUN spectool -R -g ~/rpmbuild/SPECS/vlc.spec; yum-builddep -y ~/rpmbuild/SPECS/vlc.spec

