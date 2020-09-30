Name:		nm8-repo
Version:	1.00
Release:	1%{?dist}
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
baseurl=https://nm8.home.xs4all.nl/$basearch
gpgcheck=0
enabled=1""" > %{buildroot}/etc/yum.repos.d/nm8.repo
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-nm8

%files


%changelog
