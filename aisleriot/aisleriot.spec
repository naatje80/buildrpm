Name:		aisleriot
Version:	3.22.9
Release:	1%{?dist}
Summary:	Soltaire card game

%define _major_version %(version=%{version}; echo -n ${version%%.*})

Group:		Games	
License:	GPL3+	
URL:		https://wiki.gnome.org/Apps/Aisleriot
Source0:	https://download.gnome.org/sources/aisleriot/%{_major_version}/aisleriot-%{version}.tar.xz

BuildRequires:	guile-devel
BuildRequires:	GConf2-devel 
BuildRequires:	libcanberra-devel
BuildRequires:  librsvg2-devel
BuildRequires:	desktop-file-utils 
BuildRequires:	itstool

%description
Also known as Solitaire or sol. The rules for the games have been coded for your pleasure in the GNOME scripting language (Scheme) 

%prep
%setup -q


%build
%configure --enable-sound
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

