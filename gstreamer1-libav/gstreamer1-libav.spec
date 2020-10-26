Name:		gstreamer1-libav		
Version:	1.16.1
Release:	1%{?dist}
Summary:	GStreamer Libav plug-in		

Group:		Video
License:	GPLv2
URL:	    https://gstreamer.freedesktop.org/modules/gst-libav.html	
Source0:	https://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  yasm
BuildRequires:	python38
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-devel gstreamer1-plugins-base-devel


Requires: glib2
Requires: gstreamer1 gstreamer1-plugins-base

%description
GStreamer Libav plug-in contains one plugin with a set of elements using the Libav library code. It contains many popular decoders and encoders.

%prep
%setup -q -n gst-libav-%{version}


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

