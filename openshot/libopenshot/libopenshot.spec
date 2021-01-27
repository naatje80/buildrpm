Name:		libopenshot
Version:	0.2.5
Release:	1%{?dist}
Summary: 	OpenShot Library (libopenshot)	

Group:		Video	
License:	LGPL-3.0
URL:		https://www.openshot.org
Source0:	https://github.com/OpenShot/libopenshot/archive/v%{version}.tar.gz	


BuildRequires: cmake
BuildRequires: python3-devel
BuildRequires: ffmpeg-devel
#BuildRequires: ImageMagick-devel ImageMagick-c++-devel
BuildRequires: ImageMagick-devel
BuildRequires: libopenshot-audio-devel 
BuildRequires: qt5-qtbase-devel qt5-qtwebkit-devel qt5-qtmultimedia-devel
#BuildRequires: qt5-qtbase-devel qt5-qtmultimedia-devel
BuildRequires: swig
BuildRequires: doxygen
BuildRequires: zeromq-devel
#BuildRequires: unittest-cpp-devel
#BuildRequires: cppzmq-devel
BuildRequires: ruby-devel

Requires: python3
Requires: ffmpeg
Requires: ImageMagick
Requires: libopenshot-audio
Requires: qt5-qtbase qt5-qtwebkit qt5-qtmultimedia
#Requires: qt5-qtbase qt5-qtmultimedia
Requires: zeromq

%description
This repo is the primary development home for libopenshot. OpenShot Library (libopenshot) is an open-source project dedicated to delivering high quality video editing, animation, and playback solutions to the world. API currently supports C++, Python, and Ruby.


%package devel
Summary:  OpenShot Library (libopenshot) development files
Requires: libopenshot

%description devel
OpenShot Library (libopenshot) development files

%prep
%setup -q -n libopenshot-%{version}
exit 1

%build
%cmake -Wno-dev 
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_libdir}/python*/*
%{_libdir}/ruby/*

%files devel

%changelog
