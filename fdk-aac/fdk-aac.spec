Name:           fdk-aac
Version:        2.0.1
Release:        1%{?dist}
Summary:        A standalone library of the Fraunhofer FDK AAC code from Android.

Group:          Audio Codec
License:        Apache License v2.0
URL:            https://sourceforge.net/projects/opencore-amr
Source0:        https://github.com/mstorsjo/fdk-aac/archive/v%{version}.tar.gz

#BuildRequires: 
#Requires:      

%description
A standalone library of the Fraunhofer FDK AAC code from Android.

%package devel
Summary:        Developments files for fdk-aac
Requires:       fdk-aac

%description devel
Development files for fdk-aac.

%prep
%setup -q


%build
autoreconf -fi
%configure --enable-shared --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
exit 2

%files

%files devel