Name:		libsquish
Version:	1.10
Release:	1%{?dist}
Summary:	Open source DXT compression library.

Group:      System Environment/Libraries	
License:	GPLv2
URL:        https://code.google.com/archive/p/libsquish
Source0:    https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/libsquish/squish-%{version}.tar.gz	
Patch0:     compile_shared.patch
Patch1:     kColour.patch

%package devel
Summary:  development libraries for libsquish

Requires: libsquish

%description
The squish library (abbreviated to libsquish) is an open source DXT compression library written in C++ with the following features:

Supports the DXT1, DXT3 and DXT5 formats.
Optimised for both SSE and Altivec SIMD instruction sets.
Builds on multiple platforms (x86 and PPC tested).
Very simple interface.

%description devel
Development libraries for libsquish

%prep
%setup -q -n squish-%{version}
%patch0 -p 0
%patch1 -p 0

%build
USE_SSE=1 CXXFLAGS="-O2 -fPIC -g" INSTALL_DIR="/usr" make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/usr/include
mkdir -p %{buildroot}/usr/lib64
USE_SSE=1 CXXFLAGS="-O2 -fPIC -g" INSTALL_DIR="\${DESTDIR}/usr" make install DESTDIR=%{buildroot}


%files
%doc

%files devel


%changelog