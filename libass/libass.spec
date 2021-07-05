Name:		libass
Version:	0.14.0
Release:	1%{?dist}
Summary:	libass is a portable subtitle renderer for the ASS/SSA (Advanced Substation Alpha/Substation Alpha) subtitle format.

Group:		System Environment/Libraries
License:	Unkown
URL:		https://github.com/libass/libass
Source0:    https://github.com/libass/libass/releases/download/0.14.0/libass-0.14.0.tar.xz

BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	harfbuzz-devel
BuildRequires:	fontconfig-devel

Requires:		freetype
Requires:		fribidi
Requires:		harfbuzz
Requires:		fontconfig

%package devel
Summary:  development libraries for libass
Requires: libass

%description
libass is a portable subtitle renderer for the ASS/SSA (Advanced Substation Alpha/Substation Alpha) subtitle format. It is mostly compatible with VSFilter.

%description devel
Development libraries for libass

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc

%files devel


%changelog
