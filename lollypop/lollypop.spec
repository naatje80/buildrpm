Name:       lollypop
Version:    1.1.4.16
Release:    1%{?dist}
Summary:    Lollypop is a new GNOME music playing application.

Group:      Music
License:    GPLv3
URL:        https://wiki.gnome.org/Apps/Lollypop
Source0:    https://gitlab.gnome.org/World/lollypop/uploads/6b4e4e7a2c17f0770c1e2b3354ae5a3a/lollypop-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  libsoup-devel

Requires:  python3
Requires:  python3-gobject
Requires:  python3-pylast
Requires:  python3-pillow
Requires:  gstreamer1
Requires:  gstreamer1-plugins-base
Requires:  gtk3
Requires:  totem-pl-parser

%description
Lollypop is a new GNOME music playing application.

It provides:
   * mp3/4, ogg and flac.
   * Genre/Cover browsing
   * Genre/Artist/Cover browsing
   * Search
   * Main playlist (called queue in other apps)
   * Party mode
   * Replay gain
   * Cover art downloader
   * Context artist view
   * MTP sync
   * Fullscreen view
   * Radios support
   * Last.fm support
   * Auto install codecs
   * HiDPI support
   * Tunein support

%prep
%setup -q


%build
meson build --prefix /usr --libdir lib64 --backend ninja --buildtype release --strip --default-library shared
ninja-build -C build


%install
env DESTDIR=$RPM_BUILD_ROOT ninja-build -C build install


%files

%post
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null

%changelog
