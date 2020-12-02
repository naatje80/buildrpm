Name:		libcddb
Version:	1.3.2
Release:	1%{?dist}
Summary:	C library to access data on a CDDB server	

Group:		Music	
License:	GPLv2
URL:		http://libcddb.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libcddb/libcddb-%{version}.tar.bz2

#BuildRequires:	
#Requires:	

%description
Libcddb is a C library to access data on a CDDB server (freedb.org). It allows you to:

    - search the database for possible CD matches;
    - retrieve detailed information about a specific CD;
    - submit new CD entries to the database.

Libcddb supports both the custom CDDB protocol and tunnelling the query and read operations over plain HTTP. It is also possible to use an HTTP proxy server. If you want to speed things up, you can make use of the built-in caching facility provided by the library. 

%package devel
Summary:	libcddb development files
Requires:	libcddb

%description devel
libcddb development files

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc

%files devel

%changelog

