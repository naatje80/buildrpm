Name:           gstreamer1-plugins-ugly-nonfree
Version:        1.16.1
Release:        1%{?dist}
Summary:        GStreamer streaming media framework "ugly" nonfree plugins 

License:        LGPLv2+ and LGPLv2
URL:            https://gstreamer.freedesktop.org 
Source0:        https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz 
 
BuildRequires:  python38
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  lame-devel
BuildRequires:	x264-devel

Requires:	x264
Requires:	lame-libs

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins whose license is not fully compatible with LGPL.

%prep
%setup -q -n gst-plugins-ugly-%{version}

%build
%configure --disable-silent-rules --disable-fatal-warnings \
	--with-package-name="GStreamer-plugins-ugly nonfree package" \
	--with-package-origin="https://nm8.home.xs4all.nl" \
	--disable-nls --disable-examples \
	--disable-static --enable-shared --enable-gtk-doc-html=no \
	--disable-asfdemux --disable-dvdlpcmdec --disable-dvdsub \
	--disable-xingmux --disable-realmedia --disable-a52dec \
	--disable-amrnb --disable-amrwb --disable-cdio --disable-dvdread \
	--disable-mad --disable-mpeg2dec \
	--disable-sidplay --disable-x264 \
	--enable-x264 --disable-a52dec
make %{?_smp_mflags}


%install
install ./ext/x264/.libs/libgstx264.so -D  $RPM_BUILD_ROOT/%{_libdir}/gstreamer-1.0/libgstx264.so -m 644

%files
%doc


%changelog
