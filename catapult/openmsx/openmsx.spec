Name:		openmsx	
Version:	16.0
Release:	1%{?dist}
Summary:	MSX Emulator

Group:		Games
License:	GPL
URL:		https://openmsx.org
Source0:	https://github.com/openMSX/openMSX/releases/download/RELEASE_16_0/openmsx-%{version}.tar.gz

BuildRequires:	SDL2-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  python3
BuildRequires:  alsa-lib-devel
BuildRequires:  glew-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  tcl-devel
BuildRequires:  zlib-devel

Requires:   	SDL2
Requires:       SDL2_ttf
Requires:       alsa-lib
Requires:       libGLEW
Requires:       libogg
Requires:       libpng
Requires:       libtheora
Requires:       libvorbis
Requires:       tcl
Requires:       zlib

%description
openMSX is an emulator for the MSX home computer system. Its goal is to emulate all aspects of the MSX with 
100% accuracy: perfection in emulation. You can find everything you ever wanted to know about MSX, and more, 
in the Ultimate MSX FAQ.

%prep
%setup -q
sed -i 's#INSTALL_BASE:=/opt/openMSX#INSTALL_BASE:=/usr#' build/custom.mk



%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

