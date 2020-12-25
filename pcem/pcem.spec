Name:		pcem		
Version:	17
Release:	1%{?dist}
Summary:	An IBM PC emulator

Group:		Emulators
License:	GPL-v2
URL:		https://pcem-emulator.co.uk
Source0:	https://pcem-emulator.co.uk/files/PCemV%{version}Linux.tar.gz

BuildRequires:	wxGTK3-devel
BuildRequires:	openal-soft-devel
BuildRequires:  SDL2-devel

Requires:	wxGTK3
Requires:	openal-soft
Requires:   SDL2

%description
PCem (short for PC Emulator) is an IBM PC emulator for Windows and Linux that specializes in running old operating systems and software that are designed for IBM PC compatibles. Originally developed as an IBM PC XT emulator, it later emulates other IBM PC compatible computers as well.

%prep
%setup -q -c %{name}-%{version}


%build
./configure --prefix=/usr --libdir=/usr/lib64
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

