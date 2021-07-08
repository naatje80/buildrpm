%define		kodi_release 	             Matrix
Name:		kodi-plugin-visualization-shadertoy
Version:	2.3.0
Release:	1%{?dist}
Summary:	Shadertoy visualization for Kodi

Group:		Media
License:	GPL-2.0
URL:		https://kodi.tv
Source0:	https://github.com/xbmc/visualization.shadertoy/archive/refs/tags/%{version}-%{kodi_release}.tar.gz

BuildRequires: 	kodi-main
BuildRequires:	cmake
BuildRequires:  glm-devel
BuildRequires:  libglvnd-devel

Requires: 	kodi-main

%description
Shadertoy visualization for Kodi

%prep
%setup -q -n visualization.shadertoy-%{version}-%{kodi_release} 

%build
mkdir build
cd build
%cmake ../ \
    -Wno-dev \
    -DBUILD_TESTING=OFF \
    -DCMAKE_BUILD_TYPE=Release 
make %{?_smp_mflags}


%install
cd build
%make_install

%files


%changelog
