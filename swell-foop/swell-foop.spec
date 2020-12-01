Name:		swell-foop		
Version:	3.34.1
Release:	1%{?dist}
Summary:	Gnome Same Game

%define _major_version %(version=%{version}; echo -n ${version%%.*})

Group:		Games
License:	GPLv3
URL:		https://wiki.gnome.org/Apps/Swell%20Foop
Source0:    https://download.gnome.org/sources/swell-foop/%{_major_version}/swell-foop-%{version}.tar.xz


BuildRequires:	meson	
BuildRequires:  vala
BuildRequires:  clutter-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:  gtk3-devel
BuildRequires:	desktop-file-utils 
BuildRequires:  libappstream-glib
BuildRequires:  itstool

Requires:       gtk3

%description
Swell Foop is a puzzle game, previously known as Same GNOME. 
The goal is to remove the objects in as few moves as possible. Similar objects 
that are adjacent to each other are removed as a group. The remaining objects then 
collapse to fill in the gaps and new groups are formed. You cannot remove single objects.


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