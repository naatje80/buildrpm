# Not yet available for Matrix
%define		kodi_release    Matrix
%define     plugin_group    vfs
%define     plugin_name     rar

Name:		kodi-plugin-%{plugin_group}-%{plugin_name}
Version:	4.0.0
Release:	1%{?dist}
Summary:	RAR VFS add-on for Kodi

Group:		Media
License:	GPL-2.0
URL:		https://kodi.tv
Source0:	https://github.com/xbmc/%{plugin_group}.%{plugin_name}/archive/refs/tags/%{version}-%{kodi_release}.tar.gz

BuildRequires: 	kodi-main
BuildRequires:	cmake
BuildRequires:  unrar
BuildRequires:  tinyxml-devel

Requires: 	kodi-main
Requires:   	unrar
Requires:  	tinyxml

%description
RAR VFS add-on for Kodi

%prep
%setup -q -n %{plugin_group}.%{plugin_name}-%{version}-%{kodi_release}

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
