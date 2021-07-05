%define		kodi_release 	             Matrix
%define		inputstream_adaptive_version 2.6.17
Name:		kodi		
Version:	19.1
Release:	1%{?dist}
Summary:	Open source media center

Group:		Media
License:	GPL-2.0-or-later
URL:		https://kodi.tv
Source0:	https://github.com/xbmc/xbmc/archive/refs/tags/%{version}-%{kodi_release}.tar.gz
Source1:	https://github.com/xbmc/inputstream.adaptive/archive/refs/tags/%{inputstream_adaptive_version}-%{kodi_release}.tar.gz

Patch1:     	kodi-annobin-workaround.patch
Patch2:		el8_mariadb.patch

BuildRequires: alsa-lib-devel 
BuildRequires: avahi-compat-libdns_sd-devel 
BuildRequires: avahi-devel
BuildRequires: bluez-libs-devel
BuildRequires: bzip2-devel
BuildRequires: cmake 
BuildRequires: dbus-devel 
#BuildRequires: flatbuffers-devel 
#BuildRequires: fmt-devel 
BuildRequires: fontconfig-devel 
BuildRequires: freetype-devel 
BuildRequires: fribidi-devel 
#BuildRequires: fstrcmp-devel 
BuildRequires: giflib-devel 
BuildRequires: gperf 
BuildRequires: gtest 
BuildRequires: java-11-openjdk-headless 
BuildRequires: jre 
BuildRequires: lcms2-devel 
BuildRequires: libao-devel 
BuildRequires: libass-devel 
BuildRequires: libbluray-devel 
BuildRequires: libcap-devel 
BuildRequires: libcdio-devel 
#BuildRequires: libcec-devel 
BuildRequires: libcurl-devel 
BuildRequires: libidn2-devel 
BuildRequires: libjpeg-turbo-devel 
BuildRequires: libmicrohttpd-devel 
BuildRequires: libmpc-devel 
BuildRequires: libnfs-devel 
BuildRequires: libplist-devel 
BuildRequires: libpng-devel 
BuildRequires: libsmbclient-devel 
BuildRequires: libtool-ltdl-devel 
BuildRequires: libudev-devel 
BuildRequires: libunistring-devel 
BuildRequires: libusb-devel 
BuildRequires: libuuid-devel 
BuildRequires: libva-2.7-devel 
BuildRequires: intel-media-driver-devel
BuildRequires: libvdpau-devel 
BuildRequires: libxml2-devel 
BuildRequires: libXmu-devel 
BuildRequires: libXrandr-devel 
BuildRequires: libxslt-devel 
BuildRequires: libXt-devel 
#BuildRequires: lirc-devel 
BuildRequires: lzo-devel 
BuildRequires: mariadb-devel 
BuildRequires: mesa-libEGL-devel 
BuildRequires: mesa-libGL-devel 
BuildRequires: mesa-libGLU-devel 
BuildRequires: mesa-libGLw-devel 
BuildRequires: mesa-libOSMesa-devel 
BuildRequires: nasm 
BuildRequires: openssl-devel 
BuildRequires: pcre-devel 
BuildRequires: pulseaudio-libs-devel 
BuildRequires: python3-devel 
BuildRequires: python3-pillow 
#BuildRequires: rapidjson-devel 
#BuildRequires: shairplay-devel 
BuildRequires: sqlite-devel 
BuildRequires: swig 
BuildRequires: taglib-devel 
BuildRequires: trousers-devel 
BuildRequires: uuid-devel 
BuildRequires: yasm
BuildRequires: mariadb-devel
BuildRequires: tinyxml-devel

# Test
BuildRequires: groff
BuildRequires: ghostscript

#Requires: flatbuffers 
Requires: libunistring 
Requires: curl
Requires: libva-2.7
Requires: intel-media-driver
Requires: zlib
Requires: tinyxml
Requires: libnfs

%description
Kodi is an award-winning free and open source home theater/media center software and entertainment 
hub for digital media. With its beautiful interface and powerful skinning engine, it's available 
for Android, BSD, Linux, macOS, iOS and Windows.

%prep
%setup -q -n xbmc-%{version}-%{kodi_release}
%patch1 -p1
%patch2 -p1
%setup -T -b 1 -D -n xbmc-%{version}-%{kodi_release}

%build
export PKG_CONFIG_PATH=/usr/lib64/libva-2.7/pkgconfig
export CXXFLAGS=-I/usr/include/libva-2.7
export LDFLAGS=-Wl,-rpath,/usr/lib64/libva-2.7
mkdir build
cd build
%cmake ../ \
    -Wno-dev \
    -DAPP_RENDER_SYSTEM=gl \
    -DCORE_PLATFORM_NAME=x11 \
    -DVAAPI_libva-drm_INCLUDE_DIR=/usr/include/libva-2.7 \
    -DVAAPI_libva-x11_INCLUDE_DIR=/usr/include/libva-2.7 \
    -DVAAPI_libva_INCLUDE_DIR=/usr/include/libva-2.7 \
    -DVAAPI_libva_LIBRARY=/usr/lib64/libva-2.7/libva.so \
    -DVAAPI_libva-drm_LIBRARY=/usr/lib64/libva-2.7/libva-drm.so \
    -DVAAPI_libva-x11_LIBRARY=/usr/lib64/libva-2.7/libva-x11.so \
    -DENABLE_INTERNAL_FLATBUFFERS=ON \
    -DENABLE_INTERNAL_FMT=ON \
    -DENABLE_INTERNAL_FSTRCMP=ON \
    -DENABLE_INTERNAL_RapidJSON=ON \
    -DENABLE_INTERNAL_SPDLOG=ON \
    -DENABLE_INTERNAL_GTEST=ON \
    -DTINYXML_INCLUDE_DIR=/usr/include \
    -DTINYXML_LIBRARY_RELEASE=/usr/lib64/libtinyxml.so \
    -DMARIADBCLIENT_INCLUDE_DIR=/usr/include \
    -DENABLE_MARIADBCLIENT=ON \
    -DENABLE_MYSQLCLIENT=OFF
#exit 1
make %{?_smp_mflags}

%install
cd build
%make_install


%files
%doc



%changelog

