Name:		handbrake
Version:	1.3.2
Release:	1%{?dist}
Summary:	The open source video transcoder

Group:		Applications/Multimedia
License:	GPLv2+	
URL:		https://handbrake.fr
Source0:    https://github.com/HandBrake/HandBrake/releases/download/%{version}/HandBrake-%{version}-source.tar.bz2

BuildRequires:  python3
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  cmake
BuildRequires:  numactl-devel
BuildRequires:  gtk3-devel
BuildRequires:  libnotify-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	jansson-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	bzip2-devel	
BuildRequires:  lame-devel
BuildRequires:  x264-devel
BuildRequires:	libtheora-devel
BuildRequires:  libxml2-devel
BuildRequires:  opus-devel speex-devel libvpx-devel
BuildRequires:  libva-2.7-devel
BuildRequires:  intel-media-sdk-devel
BuildRequires:  libass-devel
BuildRequires:  libvorbis-devel

Requires:	libdvdcss intel-media-sdk
Requires:   libass libva-2.7 intel-media-sdk opus-devel libvpx x264 lame libsamplerate

Patch0:         contrib_defs.patch

%description
HandBrake is a tool for converting video from nearly any format to a selection of modern, widely supported codecs.

%prep
%setup -q -n HandBrake-%{version}
%patch0 -p 0

%build
export CFLAGS="-I%{_includedir}/libva-2.7"
export LDFLAGS="-L%{_libdir}/libva-2.7 -Wl,-rpath,{_libdir}/libva-2.7"
export PKG_CONFIG_PATH=%{_libdir}/libva-2.7/pkgconfig
%configure --enable-qsv
cd %{_build}
make %{?_smp_mflags}


%install
cd %{_build}
make install DESTDIR=%{buildroot}


%files


%changelog
