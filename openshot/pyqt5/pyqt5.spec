Name:		PyQt5		
Version:	5.13.2
Release:	1%{?dist}
Summary:	Python bindings for Qt v5

Group:		Development
License:	GPLv3
URL:		https://www.riverbankcomputing.com/software/pyqt/
Source0:	http://ponce.cc/slackware/sources/repo/PyQt5-%{version}.tar.gz

BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	python3
BuildRequires:	python3-sip-devel

Requires:	    qt5-qtwebkit

%description
Python bindings for Qt v5

%prep
%setup -q

%build
python3 configure.py --confirm-license --qmake /usr/bin/qmake-qt5
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=${RPM_BUILD_ROOT}


%files
%doc



%changelog


