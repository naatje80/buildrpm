Name:		freerdp
Version:	2.3.2
Epoch:		2
Release:	1%{?dist}
Summary:	FreeRDP is a free remote desktop protocol library and clients

Group:		System libraries
License:	ASL 2.0
URL:		https://www.freerdp.com
Source0:	https://github.com/FreeRDP/FreeRDP/archive/refs/tags/%{version}.tar.gz

BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: libusb1-devel
BuildRequires: cairo-devel
BuildRequires: libXfixes-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrender-devel
BuildRequires: libXrandr-devel
BuildRequires: libXi-devel
BuildRequires: libXv-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libjpeg-devel 
BuildRequires: ffmpeg-devel

Requires:	freerdp-libs

%description
FreeRDP is a free implementation of the Remote Desktop Protocol (RDP), released under the Apache license. Enjoy the freedom of using your software wherever you want, the way you want it, in a world where interoperability can finally liberate your computing experience.

%package libs
Summary: FreeRDP libraries

%description libs
FreeRDP libraries

%package -n libwinpr
Summary: Windows Portable Runtime

%description -n libwinpr
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package devel
Summary: FreeRDP development files
Requires: freerdp-libs

%description devel
FreeRDP development files


%prep
%setup -q -n FreeRDP-%{version}


%build
#-DWITH_X264=ON
%{cmake} -DWITH_JPEG=ON -Wno-dev
make %{?_smp_mflags}


%install
%make_install


%files
%doc

%files libs
%{_libdir}/*.so.*

%files -n libwinpr
%{_libdir}/libwinpr2.so.*
%{_libdir}/libwinpr-tools2.so.*

%files devel

%changelog

