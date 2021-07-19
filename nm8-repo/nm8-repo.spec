Name:		nm8-repo
Version:	2.00
Release:	3%{?dist}
Summary:	nm8 repo

Group:		Applications/Multimedia
License:	GPLv2+	
URL:		https://nm8.home.xs4all.nl

# First generate key (with signer name: RPM Key Signer and without a password): 
# gpg --generate-key
# Extract key with: gpg --armor --export "RPM Key Signer"  > nm8-repo/RPM-GPG-KEY
Source0:    RPM-GPG-KEY

%description
nm8 repo installation

%prep

%build

%install
mkdir -p %{buildroot}/etc/pki/rpm-gpg
cp %{SOURCE0} %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-nm8
mkdir -p  %{buildroot}/etc/yum.repos.d
echo """[nm8repo]
name=NM8 Repo
baseurl=https://nm8.home.xs4all.nl/ROCKYLINUX/RPMS
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-nm8
gpgcheck=1
enabled=1


[nm8repo-source]
name=NM8 Repo - Source
baseurl=https://nm8.home.xs4all.nl/ROCKYLINUX/SRPMS
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-nm8
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-nm8
""" > %{buildroot}/etc/yum.repos.d/nm8.repo

%post
yum-config-manager --enable PowerTools

%files


%changelog