Name:		vlc
Version:	3.0.11
Release:	1%{?dist}
Summary:	VLC media player

Group:		Video Application
License:	GPLv2
URL:		www.videolan.org
Source0:	http://get.videolan.org/vlc/%{version}/vlc-%{version}.tar.xz

BuildRequires:	ffmpeg-devel
BuildRequires:	lua-devel
BuildRequires:	liba52-devel
BuildRequires:	libxcb-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	qt5-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	gtk3-devel
BuildRequires:	libnotify-devel
BuildRequires:	dbus-devel
BuildRequires:	libogg-devel
BuildRequires:	libbluray-devel
BuildRequires:	opus-devel
BuildRequires:	libvorbis-devel
BuildRequires:	flac-devel
BuildRequires:	libtheora-devel
BuildRequires:	x264-devel
BuildRequires:	x265-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	libcddb-devel 
BuildRequires:	libmpg123-devel
BuildRequires:	systemd-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
BuildRequires:  libmatroska-devel

Requires:	ffmpeg
Requires:	liba52
Requires:	libxcb
Requires:	alsa-lib
Requires:	qt5-qtbase
Requires:	libdvdread
Requires:	libdvdnav
Requires:	libnotify
Requires:	libogg
Requires:	libbluray
Requires:	opus
Requires:	libvorbis
Requires:	flac
Requires:	libtheora
Requires:	x264
Requires:	x265
Requires:	libmpeg2
Requires:	libcddb
Requires:	libmpg123
Requires:   xcb-util-keysyms
Requires:   speex
Requires:   speexdsp
Requires:   libmatroska

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
autoreconf -fi
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files

%changelog
