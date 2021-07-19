Name:	 	remmina	
Version:	1.4.20
Release:	1%{?dist}
Summary:	The GTK Remmina Remote Desktop Client

Group:		Remote
License:	GPLv2
URL:		https://remmina.org
Source0:	https://gitlab.com/Remmina/Remmina/-/archive/v%{version}/Remmina-v%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:	gtk3-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  openssl-devel
BuildRequires:  libsodium-devel
BuildRequires:	libssh-devel
BuildRequires:  json-glib-devel
BuildRequires:  libsoup-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  freerdp-devel >= 2.3.2
BuildRequires:	libvncserver-devel
BuildRequires:  spice-gtk3-devel
BuildRequires:  webkitgtk4-devel
BuildRequires:  vte291-devel
BuildRequires:  cups-devel
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  libsecret-devel

Requires:	libsodium
Requires: 	vte291
Requires:   libsecret

%description
Remmina is a remote desktop client written in GTK+, aiming to be useful for system administrators and travellers, who need to work with lots of remote computers in front of either large monitors or tiny netbooks. Remmina supports multiple network protocols in an integrated and consistent user interface. Currently RDP, VNC, SPICE, NX, XDMCP, SSH and EXEC are supported.

%prep
%setup -q -n Remmina-v%{version}


%build
%{cmake} -DWITH_AVAHI=OFF -DWITH_APPINDICATOR=OFF
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files

%doc


%changelog
