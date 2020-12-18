Name:		gweled		
Version:	0.9.1
Release:	1%{?dist}
Summary:	A puzzle game with gems

Group:		Games
License:	GPLv2
URL:		https://gweled.org
Source0:	http://launchpad.net/gweled/trunk/0.9.1/+download/gweled-%{version}.tar.gz

BuildRequires:	gtk2-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libmikmod-devel
BuildRequires:  pulseaudio-libs-devel

Requires:	    gtk2
Requires:       librsvg2
Requires:       libmikmod
Requires:       pulseaudio-libs

%description
Gweled is a free version of a popular game called Bejeweled or Diamond Mine for GNU/Linux. The aim of the game is to make alignment of 3 or more gems, both vertically or horizontally by swapping adjacent gems. The game ends when there are no possible moves left.

You can also choose for two other game modes, timed or endless. In the Timed mode your limited on time, when your time is up, the game end. The Endless mode never ends, but your score will not be registred (also called the "Relax" or "Zen" mode).

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc

%changelog

