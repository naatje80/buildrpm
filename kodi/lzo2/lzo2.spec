Name:		lzo2
Version:	2.10
Release:	1%{?dist}
Summary:	LZO is a portable lossless data compression library written in ANSI C.

Group:		archive
License:	GPL v2+
URL:		http://www.oberhumer.com/opensource/lzo/
Source0:	http://www.oberhumer.com/opensource/lzo/download/lzo-%{version}.tar.gz

%description
* LZO is a portable lossless data compression library written in ANSI C.
* Offers pretty fast compression and *extremely* fast decompression.
* One of the fastest compression and decompression algorithms around. See the ratings for lzop in the famous Archive Comparison Test .
* Includes slower compression levels achieving a quite competitive compression ratio while still decompressing at this very high speed.
* Distributed under the terms of the GNU General Public License (GPL v2+). Commercial licenses are available through our LZO Professional license program.

%package devel
Summary: LZO development files
Requires: lzo2

%description devel
LZO development files

%prep
%setup -q -n lzo-%{version}


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

