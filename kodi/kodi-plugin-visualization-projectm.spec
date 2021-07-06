%define		kodi_release 	             Matrix
Name:		kodi-plugin-visualization-projectm
Version:	3.3.0
Release:	1%{?dist}
Summary:	ProjectM visualizer for Kodi

Group:		Media
License:	GPL-2.0
URL:		https://kodi.tv
Source0:	https://github.com/xbmc/visualization.projectm/archive/refs/tags/%{version}-%{kodi_release}.tar.gz

BuildRequires: 	kodi-main
BuildRequires:	cmake
BuildRequires:  libglvnd-devel
BuildRequires:	projectm-devel

Requires: 	kodi-main
Requires:	projectm

%description
kodi inputstream addon for several manifest types

%prep
%setup -q -n visualization.projectm-%{version}-%{kodi_release} 

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
"%{_datadir}/kodi/addons/visualization.projectm/resources/projectM/presets/*"


%changelog
