Name:		cdemu-daemon
Version:	3.2.4
Release:	1%{?dist}
Summary:	CDEmu daemon is the userspace daemon part of the cdemu suite.

Group:		System Tools
License:	GPLv2+
URL:		http://cdemu.sourceforge.net	
Source0: 	https://github.com/cdemu/cdemu/archive/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:	libmirage-devel
BuildRequires:	libao-devel

Requires:	libmirage
Requires:	vhba-module

%description
CDEmu daemon is the userspace daemon part of the cdemu suite.

It receives SCSI commands from kernel module and processes them, passing the requested data back to the kernel.

Daemon implements the actual virtual device; one instance per each device registered by kernel module. It uses libMirage, an image access library that is part of cdemu suite, for the image access (e.g. sector reading).

Daemon is controlled through methods that are exposed via D-BUS. It is written in C and based on GLib (and thus GObjects), but being controlled over D-BUS, it allows for different clients written in different languages.

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

