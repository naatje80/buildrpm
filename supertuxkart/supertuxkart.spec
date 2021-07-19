%define build_timestamp %(date +"%Y%m%d")

Name:		supertuxkart
Version:	gitbuild
Release:	%{build_timestamp}.1%{?dist}
Summary:	SuperTuxKart is a 3D open-source arcade racer with a variety characters, tracks, and modes to play.

Group:		Amusements/Games
License:	GNU GPL, CC-BY & CC-BY-SA
URL:		https://supertuxkart.net

BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	subversion
BuildRequires:	SDL2-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libcurl-devel
BuildRequires:	libpng-devel
BuildRequires:	libogg-devel
BuildRequires:	zlib-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	libXrandr-devel
BuildRequires:	wayland-devel
BuildRequires:	libxkbcommon-devel
BuildRequires:	openal-soft-devel
BuildRequires:	freetype-devel
BuildRequires:	harfbuzz-devel
BuildRequires:	fribidi-devel
BuildRequires:	openssl-devel
BuildRequires:  libsquish-devel

Requires:		SDL2
Requires:		libjpeg-turbo
Requires:		libcurl
Requires:		libpng
Requires:		libogg
Requires:		zlib
Requires:		libvorbis
Requires:		mesa-libGL
Requires:		libXrandr
Requires:		libxkbcommon
Requires:		openal-soft
Requires:		freetype
Requires:		harfbuzz
Requires:		fribidi
Requires:		openssl
Requires:       libsquish

%description
SuperTuxKart is a free kart racing game. It focuses on fun and not on realistic kart physics. Instructions can be found on the in-game help page.

Hardware Requirements
To run0 SuperTuxKart, make sure that your computer's specifications are equal or higher than the following specifications:

A graphics card capable of 3D rendering - NVIDIA GeForce 470 GTX, AMD Radeon 6870 HD series card or Intel HD Graphics 4000 and newer. OpenGL >= 3.3
You should have a dual-core CPU that's running at 1 GHz or faster.
You'll need at least 512 MB of free VRAM (video memory).
System memory: 1 GB
Minimum disk space: 700 MB
Ideally, you'll want a joystick with at least 6 buttons.

%prep
rm -rf stk-code stk-assets
git clone https://github.com/supertuxkart/stk-code.git stk-code
svn checkout https://svn.code.sf.net/p/supertuxkart/code/stk-assets stk-assets

%build
cd stk-code
mkdir build
cd build
%cmake ../ -DUSE_WIIUSE=OFF -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLE=OFF -DBUILD_EXAMPLE_SDL=OFF -DBUILD_SHARED_LIBS=OFF
make %{?_smp_mflags}


%install
cd stk-code
cd build
make install DESTDIR=%{buildroot}

%files
%doc

%post
firewall-cmd --zone=public --permanent --add-port=2757/udp
firewall-cmd --zone=public --permanent --add-soruce-port=2757/udp
firewall-cmd --zone=public --permanent --add-port=2759/udp
firewall-cmd --zone=public --permanent --add-source-port=2759/udp
firewall-cmd --reload

%postrun 
firewall-cmd --zone=public --permanent --remove-port=2757/udp
firewall-cmd --zone=public --permanent --remove-soruce-port=2757/udp
firewall-cmd --zone=public --permanent --remove-port=2759/udp
firewall-cmd --zone=public --permanent --remove-source-port=2759/udp
firewall-cmd --reload

%changelog
