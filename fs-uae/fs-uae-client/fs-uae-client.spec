Name:		fs-uae-client
Version:	3.0.5
Release:	1%{?dist}
Summary:	FS-UAE Amiga Emulator Client

Group:		System Tools	
License:	GPLv2+
URL:		https://fs-uae.net
Source0:	https://fs-uae.net/stable/%{version}/fs-uae-%{version}.tar.gz


BuildRequires:  glib2-devel
BuildRequires:  libpng-devel
BuildRequires:  SDL2-devel
BuildRequires:  openal-soft-devel
BuildRequires:  libXi-devel

Requires:       glib2
Requires:       libpng
Requires:       SDL2
Requires:       openal-soft
Requires:       libXi

%description
FS-UAE Amiga Emulator Client

%prep
%setup -q -n fs-uae-%{version}


%build
# Build fails with default configure options, therefore using manual configure
./configure --prefix=/usr --libdir=/usr/lib64 --with-libmpeg2=builtin
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}



%files



%changelog



