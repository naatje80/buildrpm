Name:		intel-media-driver
Version:	20.1.1
Release:	1%{?dist}
Summary:	Intel(R) Media Driver for VAAPI

Group:		Media
License:	MIT Open Source License and BSD-3-Clause
URL:		https://github.com/intel/media-driver
Source0:	https://github.com/intel/media-driver/archive/intel-media-%{version}.tar.gz

BuildRequires:	cmake intel-gmmlib-devel libva-2.7-devel libpciaccess-devel
Requires:	    intel-gmmlib libpciaccess libva-2.7

%description
The Intel(R) Media Driver for VAAPI is a new VA-API (Video Acceleration API) user mode driver supporting hardware accelerated decoding, encoding, and video post processing for GEN based graphics hardware.

%package devel
Summary:        The Intel(R) Media Driver for VAAPI development files
Requires:       intel-media-driver intel-gmmlib-devel libva-2.7-devel

%description devel
The Intel(R) Media Driver for VAAPI development files

%prep
%setup -q -n media-driver-intel-media-%{version}

%build
mkdir Build
cd Build
export PKG_CONFIG_PATH=%{_libdir}/libva-2.7/pkgconfig${PKG_CONFIG_PATH}
export CXXFLAGS=-I%{_includedir}/libva-2.7
%cmake -DBUILD_TYPE=Release ../
make %{?_smp_mflags}


%install
cd Build
make install DESTDIR=%{buildroot}


%files
%{_libdir}/libva-2.7/dri/iHD_drv_video.so
%doc

%files devel

%changelog

