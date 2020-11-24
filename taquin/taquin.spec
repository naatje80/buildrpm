Name:		taquin		
# Last version to support gtk3 3.22
Version:	3.36.7
Release:	1%{?dist}
Summary:	Sliding puzzle game

%define _major_version %(version=%{version}; echo -n ${version%%.*})

# Newer version of vala is required during build
%define vala_version 0.50.2
%define _vala_major_version %(version=%{vala_version}; echo -n ${version%%.*})

Group:		Games
License:	GPLv3
URL:		https://wiki.gnome.org/Apps/Taquin
Source0:	https://download.gnome.org/sources/gnome-taquin/%{_major_version}/gnome-taquin-%{version}.tar.xz
Source1:    http://download.gnome.org/sources/vala/%{_vala_major_version}/vala-%{vala_version}.tar.xz

BuildRequires:	meson	
BuildRequires:  gsound-devel
BuildRequires:  gtk3-devel
BuildRequires:  librsvg2-devel
BuildRequires:	desktop-file-utils 
BuildRequires:  libappstream-glib
BuildRequires:	itstool
# Required for vala
BuildRequires:  graphviz-devel

Requires:       gtk3
Requires:       librsvg2

%description
Taquin is a computer version of the 15-puzzle and other sliding puzzles. The object of Taquin is to move tiles so that they reach their places, either indicated with numbers, or with parts of a great image.

%prep
%setup -q -n gnome-%{name}-%{version}
%setup -T -D -b 1 -n vala-%{vala_version}

%build
cd ../vala-%{vala_version}
%configure --prefix=/tmp/vala-%{vala_version}
make %{?_smp_mflags}
make install 
cd ../gnome-%{name}-%{version}
export PATH=/tmp/vala-%{vala_version}/bin:$PATH
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared
ninja -C build

%install
cd ../gnome-%{name}-%{version}
env DESTDIR=$RPM_BUILD_ROOT ninja -C build install

%files
%doc



%changelog

