Summary:	A small and simple XML parser
Name:		tinyxml
Version:	2.6.2

%define downloadversion %(echo %version|sed 's/\\./_/g')
%define major		%(echo %version|cut -d. -f 1)	 

Release:	1%{?dist}
License:	zlib
Group:		System/Libraries
Url:		http://www.grinninglizard.com/tinyxml/
Source0:        https://sourceforge.net/projects/tinyxml/files/tinyxml/%{version}/tinyxml_%{downloadversion}.tar.gz/download
Patch0:		tinyxml-2.5.3-stl.patch

%description
TinyXML is a simple, small, C++ XML parser that can be easily 
integrating into other programs. Have you ever found yourself 
writing a text file parser every time you needed to save human 
readable data or serialize objects? TinyXML solves the text I/O 
file once and for all.

%package devel
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	tinyxml

%description devel
Development files and headers for %{name}.

%prep
%autosetup -n %{name} -p1

%build
for i in tinyxml.cpp tinystr.cpp tinyxmlerror.cpp tinyxmlparser.cpp; do
 	%{__cxx} %{optflags} -fPIC -o $i.o -c $i
done
%{__cxx} %{optflags} -shared -o lib%{name}.so.%{version} \
    %{build_ldflags} -Wl,-soname,lib%{name}.so.%{major} *.cpp.o 


%install
# Not really designed to be build as lib, DYI
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -m 755 lib%{name}.so.%{version} %{buildroot}%{_libdir}
ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so.%{major}
ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so
install -p -m 644 *.h %{buildroot}%{_includedir}


%files

%files devel
%doc changes.txt readme.txt
