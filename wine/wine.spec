Name:           wine
Version:        5.20
Release:        1%{?dist}
Summary:        A compatibility layer for windows applications

Group:          Applications/Emulators
License:        LGPLv2+
URL:            https://www.winehq.org/
Source0:        https://dl.winehq.org/wine/source/5.x/wine-%{version}.tar.xz 

BuildRequires: libX11-devel(x86-64) libX11-devel(x86-32)
BuildRequires: freetype-devel(x86-64) freetype-devel(x86-32)
BuildRequires: libjpeg-turbo-devel(x86-64) libjpeg-turbo-devel(x86-32)
BuildRequires: libtiff-devel(x86-64) libtiff-devel(x86-32)
BuildRequires: libXcursor-devel(x86-64) libXcursor-devel(x86-32)
BuildRequires: pulseaudio-libs-devel(x86-64) pulseaudio-libs-devel(x86-32)
BuildRequires: mesa-vulkan-devel(x86-64) mesa-vulkan-devel(x86-32)
BuildRequires: samba-winbind-clients(x86-64)
BuildRequires: glibc-devel(x86-64) glibc-devel(x86-32) 
BuildRequires: libgcc(x86-64) libgcc(x86-32)
BuildRequires: gnutls-devel(x86-64) gnutls-devel(x86-32) 
BuildRequires: libxml2-devel(x86-64) libxml2-devel(x86-32) 
BuildRequires: libpng-devel(x86-64) libpng-devel(x86-32)
BuildRequires: libXrender-devel(x86-64) sulibXrender-devel(x86-32) 
BuildRequires: alsa-lib-devel(x86-64) alsa-lib-devel(x86-32) 

%description
Wine as a compatibility layer for UNIX to run Windows applications. This
package includes a program loader, which allows unmodified Windows
3.x/9x/NT binaries to run on x86 and x86_64 Unixes. Wine can use native system
.dll files if they are available.

In Fedora wine is a meta-package which will install everything needed for wine
to work smoothly. Smaller setups can be achieved by installing some of the
wine-* sub packages.

%prep
%setup -q -n wine-%{version}

%build
%define _configure ../configure

mkdir build-{32,64}

cd build-64
%configure --enable-win64
make %{?_smp_mflags}
cd ..

cd build-32
%configure --with-wine64=../build-64
make %{?_smp_mflags}

%install
cd build-32
%makeinstall \
        includedir=%{buildroot}%{_includedir} \
        sysconfdir=%{buildroot}%{_sysconfdir}/wine \
        dlldir=%{buildroot}%{_libdir}/wine \
        LDCONFIG=/bin/true \
        UPDATE_DESKTOP_DATABASE=/bin/true
cd ..
cd build-64
%makeinstall \
        includedir=%{buildroot}%{_includedir} \
        sysconfdir=%{buildroot}%{_sysconfdir}/wine \
        dlldir=%{buildroot}%{_libdir}/wine \
        LDCONFIG=/bin/true \
        UPDATE_DESKTOP_DATABASE=/bin/true

%files
%doc