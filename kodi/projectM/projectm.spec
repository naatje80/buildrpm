Name:           projectm
Version:        3.1.12
Release:        1%{?dist}
Summary:        projectM - cross-platform music visualization

Group:          Music
License:        LGPL-2.1
URL:            https://github.com/projectM-visualizer/projectm
Source0:        https://github.com/projectM-visualizer/projectm/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  libglvnd-devel

%description
Experience psychedelic and mesmerizing visuals by transforming music into equations that render into a limitless array of user-contributed visualizations.

projectM is an open-source project that reimplements the esteemed Winamp Milkdrop by Geiss in a more modern, cross-platform reusable library.

Its purpose in life is to read an audio input and to produce mesmerizing visuals, detecting tempo, and rendering advanced equations into a limitless array of user-contributed visualizations.

%package devel
Summary: projectM development files
Requires: projectm

%description devel
projectM development files


%prep
%setup -q


%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
%make_install

%files
"%{_datadir}/projectM/presets/*"

%files devel

%changelog
