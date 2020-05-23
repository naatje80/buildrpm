Name:		x264
Version:	0.160.x
Release:	1%{?dist}
Summary:	x264 library

Group:		Video Libraries
License:	GPL	
URL:		http://www.videolan.org/developers/x264.html
Source0:	https://code.videolan.org/videolan/x264/-/archive/master/x264-master.tar.bz2

BuildRequires:	nasm	

%description
x264 is a free software library and application for encoding video streams into the H.264/MPEG-4 AVC compression format.


%package devel
Summary:	Development files for x264
Requires:	x264

%description devel
Development files for x264

%prep
%setup -q -n x264-master 


%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files

%files devel

%changelog
