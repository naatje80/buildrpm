%define MajorVersion 3.38
Name:	        sound-juicer	
Version:	%{MajorVersion}.0
Release:	1%{?dist}
Summary:	Audio CD Extractor	

Group:		Sound Tools	
License:        ???	
URL:		https://wiki.gnome.org/Apps/SoundJuicer
Source0:	https://download.gnome.org/sources/sound-juicer/%{MajorVersion}/sound-juicer-%{version}.tar.xz

BuildRequires:	itstool
BuildRequires:  brasero-devel
BuildRequires:  libcanberra-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libmusicbrainz5-devel
BuildRequires:  libdiscid-devel
BuildRequires:  iso-codes-devel
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  libappstream-glib

#Requires:	

%description
Audio CD Extractor


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas 2>/dev/null

%changelog
