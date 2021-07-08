%define		kodi_release 	             Matrix
Name:		kodi-plugin-vfs-libarchive
Version:	2.0.1
Release:	1%{?dist}
Summary:	Libarchive VFS add-on for Kodi

Group:		Media
License:	GPL-2.0
URL:		https://kodi.tv
Source0:	https://github.com/xbmc/vfs.libarchive/archive/refs/tags/%{version}-%{kodi_release}.tar.gz

BuildRequires: 	kodi-main
BuildRequires:	cmake
BuildRequires:  libarchive-devel
BuildRequires:  xz-devel
BuildRequires:  bzip2-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  openssl-devel

Requires: 	kodi-main
Requires:   libarchive
Requires:   xz-libs
Requires:   bzip2-libs
Requires:   lz4-libs
Requires:   lzo

%description
Libarchive VFS add-on for Kodi

%prep
%setup -q -n vfs.libarchive-%{version}-%{kodi_release}

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
