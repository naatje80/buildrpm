Name:		libmanette
Version:	0.2.5
Release:	1%{?dist}
Summary:	The simple GObject game controller library.
	

Group:		Games
License:	LGPLv2.1
URL:		https://salsa.debian.org/gnome-team/libmanette
Source0:	https://gitlab.gnome.org/GNOME/libmanette/-/archive/%{version}/libmanette-%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:  glib2-devel
BuildRequires:	libgudev-devel
BuildRequires:	libevdev-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	vala


Requires:	glib2
Requires:	libgudev
Requires:	libevdev

%description
The simple GObject game controller library.
libmanette offers painless access to game controllers, from any programming
language and with little dependencies.

It supports the de-facto standard gamepad, as defined by the
W3C standard gamepad specification or as
implemented by the
SDL GameController.

Convertion of raw gamepad events into usable ones is handled transparently using
an embedded library of mappings in the popular SDL mapping string format.
The API is inspired by the device and event handling of GDK, so anybody used to

GTK should feel right at home.

%package devel
Summary:	libmatte development files
Requires:	libmanette

%description devel
libmatte development files

%prep
%setup -q


%build
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared
ninja -C build

%install
env DESTDIR=$RPM_BUILD_ROOT ninja -C build install

%files
%doc

%files devel

%changelog

