Name:		python3-zmq
Version:	13.1.0
Release:	1%{?dist}
Summary: 	Python bindings for ØMQ

Group:	    Development
License:	Apache2 License
URL:		https://zeromq.org/languages/python

BuildRequires:	python3-devel
BuildRequires:  python3-Cython
BuildRequires:  zeromq-devel

Requires:	    python3
Requires:       zeromq

%description
This package contains Python bindings for ØMQ (zeromq). ØMQ is a lightweight and fast messaging implementation.


%prep
rm -rf %{name}-%{version}
git clone -b v%{version} https://github.com/zeromq/pyzmq %{name}-%{version}

%build
cd %{name}-%{version}
python3 setup.py build


%install
cd %{name}-%{version}
python3 setup.py install --root %{buildroot}


%files

%changelog
