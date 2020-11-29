Name:	    sound-juicer	
Version:	3.38.0
Release:	1%{?dist}
Summary:	Audio CD Extractor	

%define _major_version %(version=%{version}; echo -n ${version%%.*})

Group:		Sound Tools	
License:        ???	
URL:		https://wiki.gnome.org/Apps/SoundJuicer
Source0:	https://download.gnome.org/sources/sound-juicer/%{_major_version}/sound-juicer-%{version}.tar.xz
Patch0:     older_meson.patch

BuildRequires:  meson
BuildRequires:	itstool
BuildRequires:  brasero-devel
BuildRequires:  libcanberra-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  libmusicbrainz5-devel
BuildRequires:  libdiscid-devel
BuildRequires:  iso-codes-devel
BuildRequires:  libappstream-glib-devel

Requires:   brasero
Requires:   libdiscid
Requires:   libcanberra
Requires:   gstreamer1
Requires:   gstreamer1-plugins-base
Requires:   gstreamer1-plugins-good
Requires:   libmusicbrainz5

%description
Audio CD Extractor


%prep
%setup -q
%patch0 -p 0

%build
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared
ninja -C build

%install
env DESTDIR=$RPM_BUILD_ROOT ninja -C build install

%files
%doc

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas 2>/dev/null

%changelog
