Name:		libmt32emu
Version:	2.5.0
Release:	1%{?dist}
Summary:	A multi-platform software synthesiser emulating pre-GM MIDI devices.

%define		urlversion	%(echo %{version}|sed 's/\\\./_/g')

Group:		library	
License:	GPLv2+
URL:		http://munt.sourceforge.net/
Source0:	https://github.com/munt/munt/archive/libmt32emu_%{urlversion}.tar.gz

BuildRequires:  cmake
BuildRequires:  glib2-devel
#Requires:	

%package devel
Summary:	libmt32emu library development files
Requires:	libmt32emu-devel

%description
A multi-platform software synthesiser emulating (currently inaccurately) pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I. In no way endorsed by or affiliated with Roland Corp. 

%description devel
Munt library development files

%prep
%setup -q -n munt-%{name}_%{urlversion}


%build
%cmake -Dmunt_WITH_MT32EMU_QT=No \
    -DCMAKE_BUILD_TYPE=Release \
    -Dlibmt32emu_PKGCONFIG_INSTALL_PREFIX=%{_libdir}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files

%files devel

%changelog

