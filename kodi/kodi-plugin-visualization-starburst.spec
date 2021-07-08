%define		kodi_release 	             Matrix
Name:		kodi-plugin-visualization-starburst
Version:	2.4.0
Release:	1%{?dist}
Summary:	StarBurst visualization for Kodi

Group:		Media
License:	GPL-2.0
URL:		https://kodi.tv
Source0:	https://github.com/xbmc/visualization.starburst/archive/refs/tags/%{version}-%{kodi_release}.tar.gz

Patch0:     glm_missing_include.patch

BuildRequires: 	kodi-main
BuildRequires:	cmake
BuildRequires:  glm-devel
BuildRequires:  libglvnd-devel

Requires: 	kodi-main

%description
StarBurst visualization for Kodi

%prep
%setup -q -n visualization.starburst-%{version}-%{kodi_release} 
%patch0 -p1

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
