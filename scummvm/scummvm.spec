%define 	build_timestamp %(date +"%Y%m%d")

Name:		scummvm	
Version:	gitbuild
Release:	%{build_timestamp}.1%{?dist}
Summary:	Multiple 2d adventure games runner

Group:		Gaming
License:	GPlv2.1
URL:		http://www.scummvm.org		

BuildRequires:	SDL2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:  freetype-devel
BuildRequires:	flac-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	liba52-devel
BuildRequires:	fluidsynth-devel
BuildRequires:	libtheora-devel

Requires:	SDL2
Requires:  	libjpeg-turbo
Requires:  	libmad
Requires:	libpng
Requires:	libvorbis
Requires:  	freetype
Requires:	flac-libs
Requires:	alsa-lib
Requires:	libmpeg2
Requires:	liba52
Requires:	fluidsynth-libs
Requires:	libtheora

Patch0:		disable_unsupported_warning.patch
Patch1:		remove_subtile_warning.patch

%description
ScummVM is a program which allows you to run certain classic graphical
point-and-click adventure games, provided you already have their data
files. The clever part about this: ScummVM just replaces the executables
shipped with the game, allowing you to play them on systems for which
they were never designed!

%prep
export CFLAGS=-Wno-error=format-security
export CXXFLAGS=-Wno-error=format-security
rm -rf scummvm
git clone --depth 1 https://github.com/scummvm/scummvm.git
cd scummvm
%patch0 -p 0
%patch1 -p 0

%build
export CXX=g++
export CC=gcc
cd %{_builddir}/scummvm
%configure  --enable-release \
            --enable-all-engines 
make %{?_smp_mflags} VERBOSE=1 V=1

%install
cd %{_builddir}/scummvm
make install DESTDIR=%{buildroot}
strip %{buildroot}/usr/bin/scummvm

%files
%doc

%changelog
