# remirepo/fedora spec file for argon2
#
# Copyright (c) 2017-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global libname      libargon2
%global gh_owner     P-H-C
%global gh_project   phc-winner-argon2
%global soname       1

%global upstream_version 20171227
#global upstream_prever  RC1

Name:    argon2
Version: 20190702
Release: 0%{?dist}
Summary: The password-hashing tools

License: Public Domain or ASL 2.0
URL:     https://github.com/%{gh_owner}/%{gh_project}
Source0: https://github.com/P-H-C/phc-winner-argon2/archive/%{version}.zip


BuildRequires: gcc
Requires: %{libname}%{?_isa} = %{version}-%{release}


%description
Argon2 is a password-hashing function that summarizes the state of the art
in the design of memory-hard functions and can be used to hash passwords
for credential storage, key derivation, or other applications.

It has a simple design aimed at the highest memory filling rate and
effective use of multiple computing units, while still providing defense
against tradeoff attacks (by exploiting the cache and memory organization
of the recent processors).

Argon2 has three variants: Argon2i, Argon2d, and Argon2id.

* Argon2d is faster and uses data-depending memory access, which makes it
  highly resistant against GPU cracking attacks and suitable for applications
  with no threats from side-channel timing attacks (eg. cryptocurrencies). 
* Argon2i instead uses data-independent memory access, which is preferred for
  password hashing and password-based key derivation, but it is slower as it
  makes more passes over the memory to protect from tradeoff attacks.
* Argon2id is a hybrid of Argon2i and Argon2d, using a combination of
  data-depending and data-independent memory accesses, which gives some of
  Argon2i's resistance to side-channel cache timing attacks and much of
  Argon2d's resistance to GPU cracking attacks.


%package -n %{libname}
Summary:  The password-hashing library

%description -n %{libname}
Argon2 is a password-hashing function that summarizes the state of the art
in the design of memory-hard functions and can be used to hash passwords
for credential storage, key derivation, or other applications.


%package -n %{libname}-devel
Summary:  Development files for %{libname}
Requires: %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname}-devel
The %{libname}-devel package contains libraries and header files for
developing applications that use %{libname}.


%prep
%setup -qn %{gh_project}-%{gh_commit}

if ! grep -q 'ABI_VERSION = %{soname}' Makefile; then
  : soname have changed
  grep soname Makefile
  exit 1
fi

# Fix pkgconfig file
sed -e 's:lib/@HOST_MULTIARCH@:%{_lib}:;s/@UPSTREAM_VER@/%{version}/' -i %{libname}.pc

# Honours default RPM build options and library path, do not use -march=native
sed -e '/^CFLAGS/s:^CFLAGS:LDFLAGS=%{build_ldflags}\nCFLAGS:' \
    -e 's:-O3 -Wall:%{optflags}:' \
    -e '/^LIBRARY_REL/s:lib:%{_lib}:' \
    -e 's:-march=\$(OPTTARGET) :${CFLAGS} :' \
    -e 's:CFLAGS += -march=\$(OPTTARGET)::' \
    -i Makefile

%build
# parallel build is not supported
make -j1


%install
make install DESTDIR=%{buildroot}

# Drop static library
rm %{buildroot}%{_libdir}/%{libname}.a

# pkgconfig file
install -Dpm 644 %{libname}.pc %{buildroot}%{_libdir}/pkgconfig/%{libname}.pc

# Fix perms
chmod -x %{buildroot}%{_includedir}/%{name}.h


%check
make test


%files
%{_bindir}/%{name}

%files -n %{libname}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/%{libname}.so.%{soname}


%files -n %{libname}-devel
%doc *md
%{_includedir}/%{name}.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20171227-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Milan Broz <gmazyland@gmail.com> - 20171227-2
- Rebuilt to remove old library.

* Mon Mar 18 2019 Milan Broz <gmazyland@gmail.com> - 20171227-1
- Update to version 20171227 (soname increase).
- Temporarily keep libargon2.so.0.
- Fix a crash if running under memory pressure.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20161029-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20161029-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Remi Collet <remi@remirepo.net> - 20161029-5
- honours all build flags #1558128

* Thu Feb 15 2018 Remi Collet <remi@remirepo.net> - 20161029-4
- drop ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20161029-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Milan Broz <gmazyland@gmail.com> - 20161029-2
- Do not use -march=native in build, use system flags (rh #1512845).

* Wed Oct 18 2017 Remi Collet <remi@remirepo.net> - 20161029-1
- initial package