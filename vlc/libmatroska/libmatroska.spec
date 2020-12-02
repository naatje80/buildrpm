Name:		libmatroska	
Version:	1.6.2	
Release:	1%{?dist}
Summary:	C++ libary to parse and create Matroska files

Group:		Video	
License:	LGPL v2.1	
URL:		https://matroska.org/
Source0:	https://dl.matroska.org/downloads/libmatroska/libmatroska-%{version}.tar.xz

BuildRequires:	cmake	
BuildRequires:  libebml-devel

Requires:       libebml

%description
a C++ libary to parse and create Matroska files

%package devel
Summary:	libmatroska development files
Requires:	libmatroska

%description devel
libmatroska development files

%prep
%setup -q


%build
%cmake
make %{?_smp_mflags}


%install
%make_install


%files
%doc

%files devel


%changelog

