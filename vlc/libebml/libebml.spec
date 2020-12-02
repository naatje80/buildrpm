Name:		libebml		
Version:	1.4.0
Release:	1%{?dist}
Summary:	a C++ libary to parse EBML files

Group:		Video				
License:	LGPL v2,1
URL:		https://matroska.org
Source0:	https://dl.matroska.org/downloads/libebml/libebml-1.4.0.tar.xz

BuildRequires:	cmake

%description
a A++ library to parse EBML files

%package devel
Summary:	libEBML development files
Requires:	libebml

%description devel
libEBML development files

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

