Name:		mahjongg
Version:	3.38.3
Release:	1%{?dist}
Summary:	Soltaire tile game.

%define _major_version %(version=%{version}; echo -n ${version%%.*})

Group:		Games	
License:	GPL3+	
URL:		https://wiki.gnome.org/Apps/Mahjongg
Source0:	https://download.gnome.org/sources/gnome-mahjongg/%{_major_version}/gnome-mahjongg-%{version}.tar.xz
Patch0:     meson_build.patch

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gtk3-devel
BuildRequires:  librsvg2-devel
BuildRequires:	desktop-file-utils 
BuildRequires:  libappstream-glib
BuildRequires:	itstool

Requires:       gtk3

%description
Mahjongg is a solitaire (one player) version of the classic Eastern tile game, Mahjongg. The objective is
to select pairs of similar tiles.

Mahjongg's origins are not fully known, but many theories have been put forth. One such theory says that 
Noah played Mahjongg on the ark because the East hand is dominant, presumably the direction the rains came, 
in the flood. Another theory says that the Chinese philosopher, Confucius, made the game.

%prep
%setup -q -n gnome-%{name}-%{version}
%patch0 -p 0

%build
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared
ninja -C build

%install
env DESTDIR=$RPM_BUILD_ROOT ninja -C build install

%files
%doc


%changelog

