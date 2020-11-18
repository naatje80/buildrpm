Name:		SDL2_net
Version:	2.0.1
Release:	1%{?dist}
Summary:	SDL portable network library
License:	zlib
URL:		http://www.libsdl.org/projects/SDL_net/
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.gz
BuildRequires:	SDL2-devel >= 2.0

%description
This is a portable network library for use with SDL.

%package	devel
Summary:	Libraries and includes to develop SDL networked applications
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	SDL2-devel%{?_isa} >= 2.0

%description	devel
This is a portable network library for use with SDL.

This is the libraries and include files you can use to develop SDL
networked applications.

%prep
%autosetup
# Fix end-of-line encoding
sed -i 's/\r//' README.txt CHANGES.txt COPYING.txt

%build
%configure --disable-static --disable-gui
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING.txt
%doc README.txt CHANGES.txt

%files devel


%changelog
* Mon Nov 16 2020 Nathan Sanders - 2.0.1-1
- Updated for Centos8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.1-1
- Update to 2.0.1 (RHBZ #1296753)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 9 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.0-1
- Initial spec based on upstream provided sample spec file (#1107250)
