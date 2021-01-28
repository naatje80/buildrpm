Name:           ffmpeg
Version:        4.2.2
Release:        6%{?dist}
Summary:        A collection of libraries and tools to process multimedia content.

Group:          Video Tools
License:        LGPLv2.1+
URL:            https://www.ffmpeg.org
Source0:        https://github.com/FFmpeg/FFmpeg/archive/n%{version}.tar.gz

BuildRequires:  nasm
BuildRequires:  x264-devel
BuildRequires:  x265-devel
BuildRequires:  fdk-aac-devel
BuildRequires:  libvpx-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  lame-devel
BuildRequires:  libtheora-devel
BuildRequires:  SDL-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libvdpau-devel
BuildRequires:  intel-media-driver-devel

Requires:       x264
Requires:       x265
Requires:       libvpx
Requires:       fdk-aac
Requires:       pulseaudio-libs
Requires:       lame-libs
Requires:       libtheora
Requires:       libvorbis
Requires:       libvdpau
Requires:       intel-media-driver

%description
FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.

%package devel
Summary:        FFmpeg development files.
Requires:       ffmpeg

%description devel
FFmpeg development files.

%prep
%setup -q -n FFmpeg-n%{version}

%build
export PKG_CONFIG_PATH=/usr/lib64/libva-2.7/pkgconfig
export LDFLAGS=-Wl,-rpath,/usr/lib64/libva-2.7
./configure --prefix=/usr --libdir=%{_libdir} --enable-gpl \
           --enable-libfdk_aac \
           --enable-libmp3lame \
           --enable-libtheora \
           --enable-libvorbis \
           --enable-libvpx \
           --enable-libx264 \
           --enable-libx265 \
           --enable-nonfree \
           --enable-avresample \
           --disable-static \
           --enable-shared \
           --enable-libpulse \
           --enable-vdpau \
           --enable-vaapi
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%files

%files devel