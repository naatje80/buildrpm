Name:		SDL2_ttf		
Version:	2.0.15
Release:	1%{?dist}
Summary:	SDL2 TrueType fonts library

Group:		System libraries
License:	zlib license
URL:		https://www.libsdl.org
Source0:	https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-%{version}.tar.gz

BuildRequires:	SDL2-devel
BuildRequires:  freetype-devel

Requires:	SDL2
Requires:   freetype

%description
This is a sample library which allows you to use TrueType fonts in your SDL applications. 
It comes with an example program "showfont" which displays an example string for a given 
TrueType font file.

%package	devel
Summary:	Development files for SDL2_ttf library
Requires:	SDL2-devel
Requires:   freetype-devel

%description	devel
Development files for SDL2_ttf library

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc

%files devel

%changelog

