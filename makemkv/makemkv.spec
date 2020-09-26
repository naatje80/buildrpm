Name:           makemkv
Version:        1.15.2
Release:        1%{?dist}
Summary:        Video converter

Group:          Video tools
License:        Non Free
URL:            http://www.makemkv.com
Source0:        http://www.makemkv.com/download/makemkv-oss-%{version}.tar.gz
Source1:        http://www.makemkv.com/download/makemkv-bin-%{version}.tar.gz
Patch0:        accept_license.patch

BuildRequires:  which zlib-devel openssl-devel expat-devel ffmpeg-devel qt5-devel
Requires:       zlib openssl expat ffmpeg qt5-base

%description
MakeMKV is your one-click solution to convert video that you own into free and patents-unencumbered format that can be played everywhere. MakeMKV is a format converter, otherwise called "transcoder". It converts the video clips from proprietary (and usually encrypted) disc into a set of MKV files, preserving most information but not changing it in any way. The MKV format can store multiple video/audio tracks with all meta-information and preserve chapters. There are many players that can play MKV files nearly on all platforms, and there are tools to convert MKV files to many formats, including DVD and Blu-ray discs.

Additionally MakeMKV can instantly stream decrypted video without intermediate conversion to wide range of players, so you may watch Blu-ray and DVD discs with your favorite player on your favorite OS or on your favorite device.

%prep
%setup -q -c
cd %{name}-oss-%{version}
%setup -T -D -a 1
cd %{name}-bin-%{version}
%patch0 -p 0

%build
cd %{name}-oss-%{version}
%configure
make %{?_smp_mflags}

%install
cd %{name}-oss-%{version}
make install DESTDIR=%{buildroot}
cd ../%{name}-bin-%{version}
make install DESTDIR=%{buildroot}
cd %{buildroot}/%{_libdir}
chmod 755 *.*

%files