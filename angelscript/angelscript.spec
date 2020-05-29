Name:		angelscript
Version:	2.34.0
Release:	1%{?dist}
Summary:	cross-platform scripting library

Group:		System Environment/Libraries
License:	zlib License
URL:		https://www.angelcode.com/angelscript/
Source0:    https://www.angelcode.com/angelscript/sdk/files/angelscript_%{version}.zip
Patch0:     cmake_lib64.patch

BuildRequires:  cmake

%package devel
Summary:    AngelScript development libraries
Requires:   angelscript

%description
The AngelCode Scripting Library, or AngelScript as it is also known, is an extremely flexible cross-platform
scripting library designed to allow applications to extend their functionality through external scripts. 
It has been designed from the beginning to be an easy to use component, both for the application programmer 
and the script writer.

Efforts have been made to let it call standard C functions and C++ methods with little to no need for proxy 
functions. The application simply registers the functions, objects, and methods that the scripts should be 
able to work with and nothing more has to be done with your code. The same functions used by the application 
internally can also be used by the scripting engine, which eliminates the need to duplicate functionality.

For the script writer the scripting language follows the widely known syntax of C/C++, but without the need to 
worry about pointers and memory leaks. Contrary to most scripting languages, AngelScript uses the common C/C++ 
datatypes for more efficient communication with the host application.

%description devel
AngelScript development libraries

%prep
%setup -q -n sdk
%patch0 -p 0

%build
cd angelscript/projects/cmake
%cmake
make %{?_smp_mflags}


%install
cd angelscript/projects/cmake
make install DESTDIR=%{buildroot}

%files
%doc

%files devel

%changelog
