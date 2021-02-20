%define __python /usr/bin/python3.4

Name:		fs-uae-launcher
Version:	3.0.5
Release:	1%{?dist}
Summary:	FS-UAE Amiga Emulator GUI Launcher

Group:		System Tools	
License:	GPLv2+
URL:		https://fs-uae.net
Source0:	https://fs-uae.net/stable/%{version}/fs-uae-launcher-%{version}.tar.gz

BuildRequires:  python3

Requires:       fs-uae-client
Requires:       python3-qt5

%description
FS-UAE Amiga Emulator GUI Launcher

%prep
%setup -q -n fs-uae-launcher-%{version}
sed -i -e '7s/prefix := \/usr\/local/prefix := \/usr/' Makefile

%install
make install DESTDIR=%{buildroot}

%files

%changelog