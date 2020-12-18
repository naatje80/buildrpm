Name:		libmikmod		
Version:	3.3.11.1	
Release:	1%{?dist}
Summary:	module audio library for mikmod

Group:		Audio
License:	GPLv2.1
URL:		http://mikmod.sourceforge.net
Source0:	https://kumisystems.dl.sourceforge.net/project/mikmod/libmikmod/%{version}/libmikmod-%{version}.tar.gz

BuildRequires:	pulseaudio-libs-devel
BuildRequires:	alsa-lib-devel

Requires:	    pulseaudio-libs
Requires:       alsa-lib

%package devel
Summary:	libmikmod development files
Requires:	libmikmod

%description devel
libmikmod development files

%description
Mikmod is a module player and library supporting many formats, including mod, s3m, it, and xm. Originally a player for MS-DOS, MikMod has been ported to other platforms, such as Unix, Macintosh, BeOS, and Java(!!)

Mikmod main authors are Jean-Paul Mikkers (MikMak), Jake Stine (Air Richter) and Frank Loemker. Steve McIntyre was the first Unix maintainer, followed by Peter Amstutz, Miodrag Vallat and finally Raphaël Assénat.

Unfortunately, since Raphaël Assénat did not have enough free time to work on MikMod those days, releases somewhat came to an halt. This is why he handed the baton to Shlomi Fish in order to add new features, fix bugs and bring the project further. As of September 2013, Shlomi handed the baton to Ozkan as the maintainer for the project.


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

