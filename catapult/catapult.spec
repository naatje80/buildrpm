Name:		catapult
Version:	16.0
Release:	1%{?dist}
Summary:	OpenMSX GUI frontend

Group:		Games
License:	GPL
URL:		https://openmsx.org
Source0:	https://github.com/openMSX/openMSX/releases/download/RELEASE_16_0/openmsx-catapult-%{version}.tar.gz

BuildRequires:	openmsx
BuildRequires:  python3
BuildRequires:  wxBase3-devel
BuildRequires:  wxGTK3-devel
BuildRequires:  libxml2-devel

Requires:	    openmsx
Requires:       wxBase3
Requires:       wxGTK3
Requires:       libxml2

%description
OpenMSX GUI frontend

%prep
%setup -q -n openmsx-%{name}-%{version}
sed -i 's#/opt/openMSX#/usr#' build/custom.mk 

%build
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

