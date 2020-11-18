Name: fluidsynth
Version: 2.1.5
Release: 1%{?dist}
Summary: A real-time software synthesizer based on SoundFont 2 specifications.

License: LGPL
Group: Sound
URL: http://www.fluidsynth.org/
Source0: https://github.com/FluidSynth/fluidsynth/archive/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	glib2-devel

%description
FluidSynth is a real-time software synthesizer based on the SoundFont
2 specifications. FluidSynth can read MIDI events from MIDI input
devices and render them to audio devices using SoundFont files to
define the instrument sounds. It can also play MIDI files and supports
real time effect control via SoundFont modulators and MIDI
controls. FluidSynth can be interfaced to other programs in different
ways, including linking as a shared library.

%package libs
Summary: Run-time libraries FluidSynth

%description libs
Run-time libraries FluidSynth

%package devel
Summary: Libraries and includes to build FluidSynth into other applications
Group: Development/Libraries

Requires:   fluidsynth-libs

%description devel
FluidSynth is a real-time software synthesizer based on the SoundFont
2 specifications. FluidSynth can read MIDI events from MIDI input
devices and render them to audio devices using SoundFont files to
define the instrument sounds. It can also play MIDI files and supports
real time effect control via SoundFont modulators and MIDI
controls. FluidSynth can be interfaced to other programs in different
ways, including linking as a shared library.

This package contains libraries and includes for building applications
with FluidSynth support.

%prep
%setup -q

%build
mkdir build
cd build
%cmake ../ 
make %{?_smp_mflags}

%install
cd build
%make_install

%files

%files libs
%{_libdir}/libfluidsynth.so.*

%files devel

%changelog
* Thu Nov 12 2020 Nathan Sanders
- Updated for use with Centos8

* Mon Aug 25 2003 Josh Green <jgreen@users.sourceforge.net>
- Created initial fluidsynth.spec.in
