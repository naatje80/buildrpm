
Name:		intel-media-sdk
Version:	20.1.1
Release:	1%{?dist}
Summary:	Intel(R) Media Driver for VAAPI

Group:      Media
License:	MIT Open Source License and BSD-3-Clause
URL:		https://software.intel.com/en-us/media-sdk
Source0:	https://github.com/Intel-Media-SDK/MediaSDK/archive/intel-mediasdk-%{version}.tar.gz

BuildRequires:	cmake libva-2.7-devel intel-media-driver-devel
Requires:	    libva-2.7 intel-media-driver

%description
Intel® Media SDK provides a plain C API to access hardware-accelerated video decode, encode and filtering on Intel® Gen graphics hardware platforms. Implementation written in C++ 11 with parts in C-for-Media (CM).
Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders: HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters: Color Conversion, Deinterlace, Denoise, Resize, Rotate, Comp

%package devel
Summary:        Intel® Media SDK development files development files      

%description devel
Intel® Media SDK development files

%prep
%setup -q -n MediaSDK-intel-mediasdk-%{version}

%build
mkdir Build
cd Build
export PKG_CONFIG_PATH=%{_libdir}/libva-2.7/pkgconfig${PKG_CONFIG_PATH}
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_SAMPLES=OFF -DBUILD_TUTORIALS=OFF ../
make %{?_smp_mflags}

%install
cd Build
make install DESTDIR=%{buildroot}

%files
%{_libdir}/*.so
%{_libdir}/mfx/*.so
%doc

%files devel


%changelog

