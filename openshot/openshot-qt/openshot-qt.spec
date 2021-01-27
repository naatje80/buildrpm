%define         _libdir /usr/lib

Name:		openshot-qt
Version: 	2.5.1
Release:	1%{?dist}
Summary: 	OpenShot Video Editor	

Group:	        Video	
License:	LGPL-3.0	
URL:		http://www.openshot.org
Source0:	https://github.com/OpenShot/openshot-qt/archive/v%{version}.tar.gz

BuildRequires:	python3-devel
BuildRequires:	libopenshot-audio-devel
BuildRequires:  libopenshot-devel	
BuildRequires:	python3-sip-devel
BuildRequires:  python3-setuptools

Requires:	python3
Requires:	libopenshot-audio
Requires:   libopenshot	
Requires:	python3-sip
Requires:	python3-zmq
Requires:	python3-requests
Requires:   PyQt5

%description
This repo is the primary development home for OpenShot Video Editor (version 2+), a PyQt video editing application which utilizes the powerful libopenshot C++ library. 

%prep
%setup -q -n openshot-qt-%{version}


%build


%install
python3 setup.py install --root %{buildroot}
# Patch file to ensure also for non-gnome desktop session icons are loaded
sed -i '5i\from os import environ\n' %{buildroot}/%{_bindir}/openshot-qt
sed -i '7i\environ["DESKTOP_SESSION"]="gnome"\n' %{buildroot}/%{_bindir}/openshot-qt

%files

%changelog
