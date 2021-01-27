Name:		libopenshot-audio
Version:	0.2.0
Release:	1%{?dist}
Summary:	OpenShot Audio Library

Group:		Video	
License:	GPL-3.0	
URL:		https://www.openshot.org
Source0:	https://github.com/OpenShot/libopenshot-audio/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:	alsa-lib-devel
BuildRequires:  freetype-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXcursor-devel

%description
OpenShot Audio Library (libopenshot-audio) is a program that allows the high-quality editing and playback of audio, and is based on the amazing JUCE library. 


%package devel
Summary: OpenShot Audio Library development files
Requires: libopenshot-audio

%description devel
OpenShot Audio Library development files


%prep
%setup -q -n libopenshot-audio-%{version}


%build
%cmake
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}


%files


%files devel

%changelog