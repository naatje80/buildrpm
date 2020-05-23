Name:		libva-2.7-utils
Version:	2.7.1
Release:	1%{?dist}
Summary:	Utilities fo Video Acceleration (VA) API for Linux

Group:		Media
License:	MIT Open Source License
URL:		https://01.org/linuxmedia
Source0:	https://github.com/intel/libva-utils/archive/%{version}.tar.gz

BuildRequires:	autoconf which libva-2.7-devel

%description
Libva is a library providing the VA API video acceleration API.
This package contains the utilities for this library.

%package devel
Summary:    LibVa utilities development files    
Requires:   libva-2.7-utils libva-2.7-devel

%description devel
LibVa utilities development files    

%prep
%setup -q -n libva-utils-%{version}

%build
export PKG_CONFIG_PATH=%{_libdir}/libva-2.7/pkgconfig${PKG_CONFIG_PATH}
NOCONFIGURE=1  ./autogen.sh
%configure --libdir=%{_libdir}/%{name} --includedir=%{_includedir}/%{name}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc

%files devel


%changelog

