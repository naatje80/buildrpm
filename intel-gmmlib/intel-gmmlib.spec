Name:		intel-gmmlib
Version:	20.1.1
Release:	1%{?dist}
Summary:	Intel(R) Graphics Memory Management Library

Group:		Media	
License:	MIT Open Source License
URL:		https://github.com/intel/gmmlib
Source0:	https://github.com/intel/gmmlib/archive/intel-gmmlib-%{version}.tar.gz

BuildRequires:	cmake

%description
The Intel(R) Graphics Memory Management Library provides device specific and buffer management for the Intel(R) Graphics Compute Runtime for OpenCL(TM) and the Intel(R) Media Driver for VAAPI.

%package devel
Summary:        intel-gmmlib development files.
Requires:       intel-gmmlib

%description devel
The Intel(R) Graphics Memory Management Library development files

%prep
%setup -q -n gmmlib-%{name}-%{version}


%build
mkdir Build
cd Build
%cmake -DBUILD_TYPE=Release ../
make %{?_smp_mflags}


%install
cd Build
make install DESTDIR=%{buildroot}


%files

%files devel

%changelog