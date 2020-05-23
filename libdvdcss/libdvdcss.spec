Name:		libdvdcss
Version:	1.4.2
Release:	1%{?dist}
Summary:	A simple library designed for accessing DVDs like a block device without having to bother about the decryption.

Group:      Video Tools	
License:	GPLv2
URL:        http://www.videolan.org/developers/libdvdcss.html
Source0:    http://download.videolan.org/pub/libdvdcss/%{version}/libdvdcss-%{version}.tar.bz2	


%package devel
Summary:  development libraries for libdvdcss

Requires: libdvdcss

%description
libdvdcss is a library that computer programs can use to access the
contents of a DVD.


    1/ DVD zones

   All DVDs and commercially distributed readers include some information
about their zone. When a DVD is put into a DVD reader, the information is
compared, in order to limit the number of countries where the DVD can be
used. The DVD zone and the reader's zone should match.


    2/ CSS

   CSS (Content Scrambling System) protects most commercial DVDs.  Writers
of DVD reader programs obtain keys by purchasing them from the DVD CCA (DVD
Copy Control Association) which will permit them to decrypt CSS-protected
DVDs. They also get instructions on how to use CSS, which are kept secret
under a confidentiality agreement.  When a program reads a DVD, it
communicates with the DVD reader all the time, in order to get the
decryption information with the help of the key.


    3/ Copying DVDs

   The present systems do not prevent the copying of DVDs. With the right
equipment, a perfect physical copy of the media can be made (often called a
'bit by bit') which will be possible to exploit in the same way.
Furthermore, since the media must be decrypted by the reading program in
order to appear on the screen, the decrypted content of the media will be
accessible while it is being viewed - whatever the equipment used.


    4/ Weaknesses of CSS

   CSS has been the subject of academic studies which have, through reverse
engineering, uncovered how it works and what encryption algorithm it uses.
These studies also show that the keys used by CSS are extremely weak from a
cryptographic (code-breaking) perspective, which has led to more effective
decryption algorithms and the discovery of keys.  It is possible to obtain
a complete list of keys in a few minutes on an ordinary desktop computer.


    5/ How libdvdcss works

   The list of CSS keys is therefore perfectly well known, and a sample of
these keys is distributed with libdvdcss.  The libdvdcss library operates
in a similar manner to a DVD reader program, by using a key to decode the
content, except that libdvdcss uses a key from the sample.  If all of the
sample keys fail, then libdvdcss computes the rest of the key set and tries
each of them.

   This might still not work, particularly if the DVD and the reader are
not from the same zone. As a last resort, libdvdcss will step outside of
the whole DVD/reader system and will decrypt the encoded stream directly,
exploiting weaknesses in the CSS encryption.


%description devel
Development libraries for libdvdcss

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
