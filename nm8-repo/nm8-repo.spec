Name:		nm8-repo
Version:	2.00
Release:	2%{?dist}
Summary:	nm8 repo

Group:		Applications/Multimedia
License:	GPLv2+	
URL:		https://nm8.home.xs4all.nl

%description
nm8 repo installatio

%prep

%build

%install
#mkdir -p %{buildroot}/etc/pki/rpm-gpg
#gpg --armor --export "nm8 repo" > %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-nm8
mkdir -p  %{buildroot}/etc/yum.repos.d
echo """[nm8repo]
name=NM8 Repo
baseurl=https://nm8.home.xs4all.nl/ROCKYLINUX/RPMS
gpgcheck=0
enabled=1

[nm8repo-source]
name=NM8 Repo - Source
baseurl=https://nm8.home.xs4all.nl/ROCKYLINUX/SRPMS
gpgcheck=0
enabled=0
""" > %{buildroot}/etc/yum.repos.d/nm8.repo
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-nm8

%post
yum-config-manager --enable PowerTools

%files


%changelog
