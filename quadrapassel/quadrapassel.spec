Name:		quadrapassel
Version:	3.38.1
Release:	1%{?dist}
Summary:	Tetris clone

%define _major_version %(version=%{version}; echo -n ${version%%.*})

Group:		Games	
License:	GPL2
URL:		https://wiki.gnome.org/Apps/Quadrapassel
Source0:	https://download.gnome.org/sources/%{name}/%{_major_version}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	vala
BuildRequires:	clutter-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:	gsound-devel
BuildRequires:	libmanette-devel
BuildRequires:	librsvg2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	itstool

Requires:	gsound
Requires:	libmanette
Requires:	librsvg2

%description
Quadrapassel comes from the classic falling-block game, Tetris. The goal of the game is to create complete horizontal lines of blocks, which will disappear. The blocks come in seven different shapes made from four blocks each: one straight, two L-shaped, one square, and two S-shaped. The blocks fall from the top center of the screen in a random order. You rotate the blocks and move them across the screen to drop them in complete lines. You score by dropping blocks fast and completing lines. As your score gets higher, you level up and the blocks fall faster.

In previous versions, the game was known as Gnometris.
 
%prep
%setup -q


%build
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared
ninja -C build

%install
env DESTDIR=$RPM_BUILD_ROOT ninja -C build install


%files
%doc



%changelog

