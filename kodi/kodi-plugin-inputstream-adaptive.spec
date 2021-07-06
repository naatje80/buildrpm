%define		kodi_release 	             Matrix
Name:		kodi-plugin-inputstream-adaptive
Version:	2.6.17
Release:	1%{?dist}
Summary:	Open source media center 

Group:		Media
License:	GPL-2.0
URL:		https://kodi.tv
Source0:	https://github.com/xbmc/inputstream.adaptive/archive/refs/tags/%{version}-%{kodi_release}.tar.gz

BuildRequires: 	kodi-main
BuildRequires:	cmake
BuildRequires:  expat-devel

Requires: 	kodi-main

%description
kodi inputstream addon for several manifest types

%prep
%setup -q -n inputstream.adaptive-%{version}-%{kodi_release}

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
%doc


%changelog
