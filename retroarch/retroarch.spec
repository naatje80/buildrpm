%define 	build_timestamp %(date +"%Y%m%d")

Name:		retroarch
Version:	gitbuild
Release:	%{build_timestamp}.1%{?dist}
Summary:	Cross-platform, sophisticated frontend for the libretro API. 

Group:		Games	
License:	GPLv3.0
URL:		https://www.retroarch.com
Source0:	https://github.com/libretro/libretro-super/archive/refs/tags/Latest.tar.gz

#BuildRequires:	
#Requires:	

%description
RetroArch is the reference frontend for the libretro API. Popular examples of implementations 
for this API includes video game system emulators and game engines as well as more generalized 
3D programs. These programs are instantiated as dynamic libraries. We refer to these as 
"libretro cores".

%prep
%setup -q -n libretro-super-Latest


%build
#./configure \
#    --prefix=/usr 
#make %{?_smp_mflags}
./libretro-fetch.sh
./libretro-build.sh

%install
./libretro-install.sh
#%make_install


%files
%doc



%changelog

