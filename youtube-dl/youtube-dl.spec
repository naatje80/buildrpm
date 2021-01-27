%define _date_version           2021-01-03

%define _version                %(date=%{_date_version}; date --date=${date} +%%Y.%%m.%%d)
%define _package_version        %(date=%{_date_version}; date --date=${date} +%%Y.%%-m.%%-d)

Name:		youtube-dl
Version:	%{_version}
Release:	1%{?dist}
Summary: 	A command-line program to download videos from e.g. YouTube.com

Group:	    Download	
License:	public domain
URL:        https://yt-dl.org

Source0:	https://yt-dl.org/downloads/%{version}/youtube-dl-%{version}.tar.gz

BuildRequires:	python3

Requires:	    python3
Requires:       ffmpeg

%description
youtube-dl is a command-line program to download videos from YouTube.com and a few more sites. 
It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform specific. 
It should work in your Unix box, in Windows or in Mac OS X. 

It is released to the public domain, which means you can modify it, redistribute it or use it however you like. 


%prep
%setup -q -n %{name}
PYTHONPATH=/tmp/pythondeps/lib/python3.6/site-packages pip3 install  --no-binary :all: --install-option="--prefix=/tmp/pythondeps" zapp
# Fix for version check
sed -i 's/0.0.0/0.5/g' /tmp/pythondeps/lib/python3.6/site-packages/zipp-0.0.0-py3.6.egg-info/PKG-INFO

%build
PYTHONPATH=/tmp/pythondeps/lib/python3.6/site-packages python3 setup.py bdist_zapp -e youtube_dl:main

%install
install -D -m 755 dist/youtube_dl-%{_package_version}.pyz ${RPM_BUILD_ROOT}/usr/bin/youtube-dl

%files

%changelog
