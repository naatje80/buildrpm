Name:		cdemu-client
Version:	3.2.4
Release:	1%{?dist}
Summary:	CDEmu client is a simple command-line client for controlling CDEmu daemon.

Group:		System Tools	
License:	GPLv2+
URL:		http://cdemu.sourceforge.net
Source0:        https://github.com/cdemu/cdemu/archive/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:	libmirage-devel

Requires:	libmirage
Requires:	vhba-module
Requires:	cdemu-daemon

%description
CDEmu client is a simple command-line client for controlling CDEmu daemon.

It provides a way to perform the key tasks related to controlling the CDEmu daemon, such as loading and unloading devices, displaying devices' status and retrieving/setting devices' debug masks.

%prep
%setup -q -n cdemu-%{name}-%{version}/%{name}


%build
%cmake
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog