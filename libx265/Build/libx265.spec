Name:		x265
Version:	3.3
Release:	1%{?dist}
Summary:	x264 library

Group:		Video Libraries
License:	GPL	
URL:		http://www.videolan.org/developers/x264.html
Source0:	https://github.com/videolan/x265/archive/%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:  nasm

%description
x265 is a free software library and application for encoding video streams into the H.265/MPEG-4 AVC compression format.


%package devel
Summary:	Development files for x265
Requires:	x265

%description devel
Development files for x265

%prep
%setup -q -n %{name}-%{version}/source


%build
%cmake
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files

%files devel

%changelog
