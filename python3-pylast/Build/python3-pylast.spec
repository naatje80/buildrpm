Name:		python3-pylast
Version:	3.2.1
Release:	1%{?dist}
Summary: 	A Python interface to Last.fm and Libre.fm

Group:	    Music	
License:	Apache2 License
URL:		https://pypi.org/project/pylast

BuildRequires:	python3-devel
Requires:	python3
Requires:	python3-six

%description


%prep
rm -rf %{name}-%{version}
git clone -b %{version} https://github.com/pylast/pylast.git %{name}-%{version}

%build
cd %{name}-%{version}
python3 setup.py build


%install
cd %{name}-%{version}
python3 setup.py install --root %{buildroot}


%files

%changelog
