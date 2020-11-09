%define _libdir /usr/lib

Name:		steam	
Version:	1.0
Release:	1%{?dist}
Summary:	steam client

Group:		Games
License:	close source
URL:		https://store.steampowered.com/
Source0:	https://steamcdn-a.akamaihd.net/client/installer/steam.deb

Requires:	wmctrl

%description
Steam is the ultimate destination for playing, discussing, and creating games.

%prep
%setup -q -T -c %{name}-%{version}
ar -xv %{SOURCE0}
tar -xvf data.tar.xz

%install
for file in `find usr/ -type f -or -type l`
do
        install -D $file %{buildroot}/$file
done
for file in `find lib/ -type f`
do
        install -D $file %{buildroot}/usr/$file
done


%files

%changelog