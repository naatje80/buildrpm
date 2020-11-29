Name:	    libdiscid
Version:	0.6.2
Release:	1%{?dist}
Summary:	C library for creating MusicBrainz and freedb disc IDs from audio CD

Group:		Sound Tools
License:    GPLv2.1
URL:		https://musicbrainz.org/doc/libdiscid
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/libdiscid/libdiscid-%{version}.tar.gz

%package devel
Summary:    libdiscid devvelopment files
Requires:   libdiscid

%description devel
libdiscid devvelopment files

%description

libdiscid is a C library for creating MusicBrainz and freedb disc IDs from audio CDs. It reads 
a CD's table of contents (TOC) and generates an identifier which can be used to lookup the CD 
at MusicBrainz. Additionally, it provides a submission URL for adding the disc ID to the database 
and gathers ISRCs and the MCN (=UPC/EAN) from disc.

The interface of this library is new, but the disc ID algorithm and the operating system dependent 
CD-ROM/DVD-ROM access code have been ported from libmusicbrainz version 2.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc

%files devel

%changelog
