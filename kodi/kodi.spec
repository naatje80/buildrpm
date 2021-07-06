%define		kodi_release 	             Matrix
Name:		kodi
Version:	19.1
Release:	3%{?dist}
Summary:	Open source media center

Group:		Media
License:	GPL-2.0-or-later
URL:		https://kodi.tv

Requires: kodi-main == 19.1
Requires: kodi-plugin-inputstream-adaptive <= 2.6.17
Requires: kodi-plugin-visualization-projectm <= 3.3.0

%description
Kodi is an award-winning free and open source home theater/media center software and entertainment 
hub for digital media. With its beautiful interface and powerful skinning engine, it's available 
for Android, BSD, Linux, macOS, iOS and Windows.

%prep

%build

%install

%files
%doc



%changelog

