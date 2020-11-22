# Last version to support gtk3 3.22
Name:		taquin		
Version:	3.35.2
Release:	1%{?dist}
Summary:	Sliding puzzle game

%define _major_version %(version=%{version}; echo -n ${version%%.*})

Group:		Games
License:	GPLv3
URL:		https://wiki.gnome.org/Apps/Taquin
Source0:	https://download.gnome.org/sources/gnome-taquin/%{_major_version}/gnome-taquin-%{version}.tar.xz

BuildRequires:	meson	
BuildRequires:  vala
BuildRequires:  gsound-devel
BuildRequires:  gtk3-devel
BuildRequires:  librsvg2-devel
BuildRequires:	desktop-file-utils 
BuildRequires:  libappstream-glib
BuildRequires:	itstool

Requires:       gtk3
Requires:       librsvg2

%description
Taquin is a computer version of the 15-puzzle and other sliding puzzles. The object of Taquin is to move tiles so that they reach their places, either indicated with numbers, or with parts of a great image.

%prep
%setup -q -n gnome-%{name}-%{version}


%build
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared
ninja -C build

%install
env DESTDIR=$RPM_BUILD_ROOT ninja -C build install

%files
%doc



%changelog

