Name:		vlc
Version:	3.0.10
Release:	1%{?dist}
Summary:	VLC media player

Group:		Video Application
License:	GPLv2
URL:		www.videolan.org
Source0:	http://get.videolan.org/vlc/%{version}/vlc-%{version}.tar.xz

BuildRequires:	lua-devel
BuildRequires:	yasm
BuildRequires:	libva-devel
BuildRequires:	libass-devel
BuildRequires:	libkate-devel
BuildRequires:	libbluray-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libcddb-devel
BuildRequires:	libmodplug-devel
BuildRequires:	zlib-devel
BuildRequires:	dbus-devel
BuildRequires:	lua-devel
BuildRequires:	zvbi
BuildRequires:	libdvdread-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
BuildRequires:	libxml2-devel
BuildRequires:	mesa-libGLU-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	qt-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:	qt5-qtx11extras-devel
BuildRequires:	libdvbpsi-devel
BuildRequires:	v4l-utils
BuildRequires:  liba52-devel
BuildRequires:  devtoolset-4-gcc-c++

Requires:	libdvdcss

%description
VLC is a free and open source cross-platform multimedia player and framework that plays most multimedia files, and various streaming protocols. 

%package devel
Summary:	VLC development files.
Requires:	vlc

%description devel
VLC development files.

%prep
%setup -q


%build
export PATH=/opt/rh/devtoolset-4/root/bin:$PATH
%configure --enable-release
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files

%files devel


%changelog
