Name:		retro-gtk	
Version:	0.15.3
Release:	1%{?dist}
Summary:	The GTK Libretro frontend framework.

Group:		Games
License:	GPL-3.0
URL:		https://gitlab.gnome.org/GNOME/retro-gtk
Source0:	https://gitlab.gnome.org/GNOME/retro-gtk/-/archive/%{version}/retro-gtk-%{version}.tar.bz2

BuildRequires:	meson	
BuildRequires:  libepoxy-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala

%description
The GTK Libretro frontend framework.

Libretro is a plugin format design to implement video game console emulators, 
video games and similar multimedia software. Such plugins are called Libretro cores.

RetroGTK is a framework easing the use of Libretro cores in conjunction with GTK.

%package devel
Summary:	retro-gtk development files
Requires:	retro-gtk

%description devel
Retro-gtk development files

%prep
%setup -q
sed -i 's/0.50.0/0.47.0/' meson.build

%build
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared
ninja -C build

%install
env DESTDIR=$RPM_BUILD_ROOT ninja -C build install


%files
%doc

%files devel


%changelog

