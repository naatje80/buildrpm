%define		kodi_release 	             Matrix
Name:		kodi
Version:	19.1
Release:	4%{?dist}
Summary:	Open source media center

Group:		Media
License:	GPL-2.0-or-later
URL:		https://kodi.tv

Requires: kodi-main == 19.1
Requires: kodi-plugin-inputstream-adaptive <= 2.6.17
Requires: kodi-plugin-visualization-projectm <= 3.3.0
Requires: kodi-plugin-visualization-starburst <= 2.4.0
Requires: kodi-plugin-visualization-shadertoy <= 2.3.0
Requires: kodi-plugin-visualization-fishbmc <= 6.3.0
Requires: kodi-plugin-vfs-libarchive <= 2.0.1
Requires: kodi-plugin-vfs-rar <= 4.0.0

%description
Kodi is an award-winning free and open source home theater/media center software and entertainment 
hub for digital media. With its beautiful interface and powerful skinning engine, it's available 
for Android, BSD, Linux, macOS, iOS and Windows.

%prep

%build

%install

%files
%doc

%post
firewall-cmd --zone=public --permanent --add-port=8080/tcp
firewall-cmd --zone=public --permanent --add-port=9090/tcp
firewall-cmd --reload

%changelog

