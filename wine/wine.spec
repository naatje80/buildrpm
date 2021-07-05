Name:           wine
Version:        6.12
Release:        1%{?dist}
Summary:        A compatibility layer for windows applications

Group:          Applications/Emulators
License:        LGPLv2+
URL:            https://www.winehq.org/
Source0:        https://dl.winehq.org/wine/source/6.x/wine-%{version}.tar.xz
Source1:        https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks

BuildRequires: libX11-devel(x86-64) libX11-devel(x86-32)
BuildRequires: freetype-devel(x86-64) freetype-devel(x86-32)
BuildRequires: libjpeg-turbo-devel(x86-64) libjpeg-turbo-devel(x86-32)
BuildRequires: libtiff-devel(x86-64) libtiff-devel(x86-32)
BuildRequires: libXcursor-devel(x86-64) libXcursor-devel(x86-32)
BuildRequires: pulseaudio-libs-devel(x86-64) pulseaudio-libs-devel(x86-32)
BuildRequires: samba-winbind-clients(x86-64)
BuildRequires: glibc-devel(x86-64) glibc-devel(x86-32) 
BuildRequires: libgcc(x86-64) libgcc(x86-32)
BuildRequires: gnutls-devel(x86-64) gnutls-devel(x86-32) 
BuildRequires: libxml2-devel(x86-64) libxml2-devel(x86-32) 
BuildRequires: libpng-devel(x86-64) libpng-devel(x86-32)
BuildRequires: libXrender-devel(x86-64) libXrender-devel(x86-32) 
BuildRequires: alsa-lib-devel(x86-64) alsa-lib-devel(x86-32)
BuildRequires: mesa-libGL-devel(x86-64) mesa-libGL-devel(x86-32)
BuildRequires: mesa-libGLU-devel(x86-64) mesa-libGLU-devel(x86-32)
BuildRequires: mesa-libOSMesa-devel(x86-64) mesa-libOSMesa-devel(x86-32) 
BuildRequires: libXrandr-devel(x86-64) libXrandr-devel(x86-32)
BuildRequires: libXinerama-devel(x86-64) libXinerama-devel(x86-32)
BuildRequires: vulkan-loader-devel(x86-64) vulkan-loader-devel(x86-32) vulkan-headers
BuildRequires: dbus-devel(x86-64) dbus-devel(x86-32)

Requires: libX11(x86-64) libX11(x86-32)
Requires: freetype(x86-64) freetype(x86-32)
Requires: libjpeg-turbo(x86-64) libjpeg-turbo(x86-32)
Requires: libtiff(x86-64) libtiff(x86-32)
Requires: libXcursor(x86-64) libXcursor(x86-32)
Requires: pulseaudio-libs(x86-64) pulseaudio-libs(x86-32)
Requires: samba-winbind-clients(x86-64)
Requires: glibc(x86-64) glibc(x86-32) 
Requires: libgcc(x86-64) libgcc(x86-32)
Requires: gnutls(x86-64) gnutls(x86-32) 
Requires: libxml2(x86-64) libxml2(x86-32) 
Requires: libpng(x86-64) libpng(x86-32)
Requires: libXrender(x86-64) libXrender(x86-32) 
Requires: alsa-lib(x86-64) alsa-lib(x86-32) 
Requires: mesa-libGL(x86-64) mesa-libGL(x86-32)
Requires: mesa-libGLU(x86-64) mesa-libGLU(x86-32)
Requires: mesa-libOSMesa(x86-64) mesa-libOSMesa(x86-32) 
Requires: mesa-dri-drivers(x86-64) mesa-dri-drivers(x86-32)
Requires: libXrandr(x86-64) libXrandr(x86-32)
Requires: libXinerama(x86-64) libXinerama(x86-32)
Requires: vulkan-loader(x86-64) vulkan-loader(x86-32)
Requires: dbus-libs(x86-64) dbus-libs(x86-32)

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
# To fix warning _FOTIFY_SOURCE redefined
export CFLAGS="`echo $RPM_OPT_FLAGS | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//'| sed -e 's/-m64//g'`"

mkdir build-{32,64}

cd build-64
%define _configure ../configure
%configure --enable-win64
make %{?_smp_mflags}
cd ..

cd build-32
%define _configure env PKG_CONFIG_PATH=/usr/lib/pkgconfig ../configure
%define _libdir /usr/lib
%configure --with-wine64=../build-64
make %{?_smp_mflags}

%install
cd build-32
%makeinstall 
cd ..

cd build-64
%define _libdir /usr/lib64
%makeinstall
cd ..

install -m 755 %{_sourcedir}/winetricks %{buildroot}/usr/bin/winetricks

%files
%doc
