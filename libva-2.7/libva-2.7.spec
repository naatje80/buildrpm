Name:		libva-2.7
Version:	2.7.1
Release:	1%{?dist}
Summary:	Video Acceleration (VA) API for Linux

Group:		Media
License:	MIT Open Source License
URL:		https://01.org/linuxmedia
Source0:	https://github.com/intel/libva/archive/%{version}.tar.gz

BuildRequires:	xorg-x11-server-devel autoconf which
#Requires:	    

%description
Libva is a library providing the VA API video acceleration API.


%package devel
Summary:        Video Acceleration (VA) API development files
Requires:       libva-2.7 xorg-x11-server-devel

%description devel
Video Acceleration (VA) API development files

%prep
%setup -q -n libva-%{version}

%build
NOCONFIGURE=1  ./autogen.sh
%configure --libdir=%{_libdir}/%{name} --includedir=%{_includedir}/%{name}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc

%files devel


%changelog

