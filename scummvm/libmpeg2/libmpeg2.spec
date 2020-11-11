Name:		libmpeg2
Version:	0.5.1
Release:	%{version}.1%{?dist}
Summary:	A free MPEG-2 video stream decoder

Group:		Video
License:	GPL
URL:		https://libmpeg2.sourceforge.io/

Source0:	https://libmpeg2.sourceforge.io/files/libmpeg2-0.5.1.tar.gz

%description
libmpeg2 is a free library for decoding mpeg-2 and mpeg-1 video streams. It is released under the terms of the GPL license.

%package devel
Summary:	MPEG-2 video stream decoder development files
Requires:	libmpeg2

%description devel
MPEG-2 video stream decoder development files

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
