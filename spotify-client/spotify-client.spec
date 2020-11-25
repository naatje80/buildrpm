Name:		spotify-client
Version:	1.1.42.622
Release:	1%{?dist}
Summary:	spotify client application for Linux

%define _curl_version   7.73.0

Group:		Music
License:	closed source
URL:		https://www.spotify.com/
Source0:	https://repository-origin.spotify.com/pool/non-free/s/spotify-client/spotify-client_%{version}.gbd112320-37_amd64.deb
Source1:        https://curl.se/download/curl-%{_curl_version}.tar.gz
Patch0:		curl_gnutls.patch

BuildRequires:  gnutls-devel
BuildRequires:  wget

%description
Steam is the ultimate destination for playing, discussing, and creating games.

%prep
# Downloading spotify deb currently breaks: force redownload using wget
wget -q https://repository-origin.spotify.com/pool/non-free/s/spotify-client/spotify-client_%{version}.gbd112320-37_amd64.deb -O %{_sourcedir}/spotify-client_%{version}.gbd112320-37_amd64.deb
%setup -q -T -c %{name}-%{version}
ar -xv %{SOURCE0}
%setup -T -D -b 1 -n curl-%{_curl_version}
%patch0 -p 1

%build
cd ../curl-%{_curl_version}
./configure --with-gnutls --without-ssl --enable-shared --disable-static --enable-versioned-symbols
make %{?_smp_mflags}

%install
cd ../%{name}-%{version}
tar -xvf data.tar.gz -C %{buildroot}
cd ../curl-%{_curl_version}
%{__install} -Dp -m0755 ./lib/.libs/libcurl-gnutls.so.4.7.0 %{buildroot}%{_datadir}/spotify/libcurl-gnutls.so.4
cd %{buildroot}
mkdir -p usr/share/applications
mv usr/share/spotify/spotify.desktop usr/share/applications
for SIZE in {512,256,128,64,48,32,24,22,16}
do
    mkdir -p usr/share/icons/hicolor/${SIZE}x${SIZE}/apps
    mv usr/share/spotify/icons/spotify-linux-${SIZE}.png usr/share/icons/hicolor/${SIZE}x${SIZE}/apps/spotify-client.png
done
chmod 0755 %{buildroot}%{_datadir}/spotify/libcef.so 

%files


%changelog
