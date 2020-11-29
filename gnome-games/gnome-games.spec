# 3.30.2 latest version compatible with GTK3
Name:		gnome-games		
Version:	3.30.2
Release:	1%{?dist}
Summary:	Simple game launcher for GNOME
	

Group:		Games
License:	GPLv3
URL:		https://wiki.gnome.org/Apps/Games
Source0:	https://gitlab.gnome.org/GNOME/gnome-games/-/archive/%{version}/gnome-games-%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:  vala
BuildRequires:  grilo-devel
BuildRequires:  gtk3-devel
BuildRequires:  libmanette-devel
BuildRequires:  retro-gtk-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsoup-devel
BuildRequires:  sqlite-devel
BuildRequires:  tracker-devel

Requires:	    retro-gtk
Requires:       librsvg2
Requires:       libsoup

%description
Games is a GNOME application to browse your local video games library and to easily pick and play a game from it.

%prep
%setup -q


%build
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared \
    -Ddesktop-plugin=true -Ddreamcast-plugin=false -Dgame-cube-plugin=false -Dlibretro-plugin=false \
    -Dlove-plugin=false -Dmame-plugin=false -Dnintendo-ds-plugin=false -Dplaystation-plugin=false \
    -Dsega-cd-plugin=false -Dsega-saturn-plugin=false -Dsteam-plugin=true -Dturbografx-cd-plugin=false \
    -Dvirtual-boy-plugin=false -Dwii-plugin=false
ninja -C build

%install
env DESTDIR=$RPM_BUILD_ROOT ninja -C build install

%files
%doc


%changelog

