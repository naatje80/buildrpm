%define gettext_version 0.21

Name:		handbrake
Version:	1.3.3
Release:	1%{?dist}
Summary:	The open source video transcoder

Group:		Applications/Multimedia
License:	GPLv2+	
URL:		https://handbrake.fr
Source0:    https://github.com/HandBrake/HandBrake/releases/download/%{version}/HandBrake-%{version}-source.tar.bz2
Source1:    https://ftp.gnu.org/pub/gnu/gettext/gettext-%{gettext_version}.tar.gz

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
BuildRequires:  opus-devel
BuildRequires:  speex-devel
BuildRequires:  libvpx-devel
BuildRequires:  libva-2.7-devel
BuildRequires:  libva-2.7-utils-devel
BuildRequires:  intel-media-sdk-devel
BuildRequires:  libass-devel
BuildRequires:  libvorbis-devel

Requires:	libdvdcss 
Requires:   intel-media-sdk
Requires:   libass
Requires:   libva-2.7
Requires:   libva-2.7-utils
Requires:   intel-media-sdk
Requires:   opus
Requires:   libvpx
Requires:   x264
Requires:   lame-libs
Requires:   libsamplerate

Patch0:         contrib_defs.patch

%description
HandBrake is a tool for converting video from nearly any format to a selection of modern, widely supported codecs.

%prep
%setup -q -n HandBrake-%{version}
%patch0 -p 0
%setup -T -D -b 1 -n gettext-%{gettext_version}

%build
cd ../gettext-%{gettext_version}
%configure --prefix=/tmp/gettext-%{gettext_version}
make %{?_smp_mflags}
make install 
cd ../HandBrake-%{version}
export CFLAGS="-I%{_includedir}/libva-2.7"
export LDFLAGS="-L%{_libdir}/libva-2.7 -Wl,-rpath,%{_libdir}/libva-2.7"
export PKG_CONFIG_PATH=%{_libdir}/libva-2.7/pkgconfig
export PATH=/tmp/gettext-%{gettext_version}/bin:$PATH
%configure --enable-qsv --enable-nvenc --launch-jobs %_smp_build_ncpus
cd %{_build}
make %{?_smp_mflags}


%install
cd ../HandBrake-%{version}
cd %{_build}
make install DESTDIR=%{buildroot}


%files


%changelog
