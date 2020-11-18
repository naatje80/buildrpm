Name:		libmirage
Version:	3.2.4
Release:	1%{?dist}
Summary:	libMirage is a CD-ROM image access library.

Group:		System Tools
License:	GPLv2+
URL:		http://cdemu.sourceforge.net
Source0:        https://github.com/cdemu/cdemu/archive/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	cmake
BuildRequires:	glib2-devel

Requires:	glib2

%description
libMirage is a CD-ROM image access library. It is written in C and based on GLib. It's aim is to provide uniform access to the data stored in various image formats.


%package devel
Summary:	Development files for libMirage.

%description devel
Development files for libMirage.

%prep
%setup -q -n cdemu-%{name}-%{version}/%{name}


%build
%cmake
exit 1
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_libdir}/libmirage*/*.so

%files devel

%changelog

