Name:		openal-soft
Version:	1.21.0
Release:	1%{?dist}
Summary:	Cross-platform, software implementation of the OpenAL 3D audio API

Group:		Amusements/Games
License:	LGPL
URL:		https://openal-soft.org/
Source0:    https://openal-soft.org/openal-releases/openal-soft-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zlib-devel

Requires:   pulseaudio-libs
Requires:   zlib

%package devel
Summary:    OpenAL Soft development libraries
Requires:   openal-soft

%description
OpenAL Soft is an LGPL-licensed, cross-platform, software implementation of the OpenAL 3D audio API. It's forked 
from the open-sourced Windows version available originally from openal.org's SVN repository (now defunct).

OpenAL provides capabilities for playing audio in a virtual 3D environment. Distance attenuation, doppler shift, 
and directional sound emitters are among the features handled by the API. More advanced effects, including air 
absorption, occlusion, and environmental reverb, are available through the EFX extension. It also facilitates 
streaming audio, multi-channel buffers, and audio capture.

%description devel
OpenAL Soft development libraries

%prep
%setup -q


%build
%cmake
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc

%files devel

%changelog
