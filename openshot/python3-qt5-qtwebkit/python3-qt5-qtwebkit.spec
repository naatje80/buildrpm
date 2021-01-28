Name:		python3-qt5-qtwebkit		
Version:	5.13.1
Release:	1%{?dist}
Summary:	Python bindings for Qt v5

Group:		Development
License:	GPLv3
URL:		https://www.riverbankcomputing.com/software/pyqt/
Source0:    https://sourceforge.net/projects/pyqt5/files/PyQt5-%{version}.tar.gz/download

BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	python3
BuildRequires:	python3-sip-devel

Requires:	    qt5-qtwebkit
Requires:       python3-qt5

%description
Python bindings for Qt v5

%prep
%setup -q -n PyQt5_gpl-%{version}

%build
python3 configure.py --confirm-license --qmake /usr/bin/qmake-qt5
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=${RPM_BUILD_ROOT}
find ${RPM_BUILD_ROOT} ! -iname '*WebKit*' -exec rm -f '{}' \;

%files
%doc



%changelog


