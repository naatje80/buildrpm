Name:           ffmpeg
Version:        4.2.2
Release:        4%{?dist}
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
Requires:       x264
Requires:       x265
Requires:       libvpx
Requires:       fdk-aac
Requires:       pulseaudio-libs
Requires:       lame-libs
Requires:       libtheora
Requires:       libvorbis

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
./configure --prefix=/usr --libdir=%{_libdir} --enable-gpl --enable-libfdk_aac --enable-libmp3lame --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-libx265 --enable-nonfree --enable-avresample --disable-static --enable-shared --enable-libpulse
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files

%files devel