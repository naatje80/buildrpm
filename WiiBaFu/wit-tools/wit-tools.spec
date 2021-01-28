%define	_build	8245

Name:		wit-tools
Version:	3.03a
Release:	1%{?dist}
Summary:	Wiimms ISO Tools is a set of command line tools to manipulate Wii and GameCube ISO images and WBFS containers

Group:		Tooling
License:	Closed Source
URL:		https://wit.wiimm.de
Source0:	https://wit.wiimm.de/download/wit-v%{version}-r%{_build}-x86_64.tar.gz

%description
Wiimms ISO Tools is a set of command line tools to manipulate Wii and GameCube ISO images and WBFS containers. The toolset consists of the following tools:

 *  wit (Wiimms ISO Tool):
    This is the main ISO manipulation tool : It can list, analyze, verify, convert, split, join, patch, mix, extract, compose, rename and compare Wii and GameCube images. It also can create and dump different other Wii file formats.

 *  wwt (Wiimms WBFS Tool):
    This is the main WBFS manipulation tool (WBFS manager) : It can create, check, repair, verify and clone WBFS files and partitions. It can list, add, extract, remove, rename and recover ISO images as part of a WBFS.

 *  wdf (Wiimms WDF Tool):
    wdf is a support tool for WDF, WIA, CISO and GCZ images. It converts (packs and unpacks), compares and dumps WDF and CISO images. Additionally it dumps WIA and GCT image and unpacks WIA images. The default command depends on the program file name (see command descriptions). Usual names are wdf, unwdf, wdf-cat, wdf-cmp and wdf-dump (with or without minus signs). »wdf +CAT« replaces the old tool wdf-cat and »wdf +DUMP« the old tool wdf-dump.

 *  wfuse (Wiimms FUSE Tool):
    Mount a Wii or GameCube image or a WBFS file or partition to a mount point using FUSE (Filesystem in USErspace). Use 'wfuse --umount mountdir' for unmounting. 

%prep
%setup -q -n wit-v%{version}-r%{_build}-x86_64
sed -i -e 's#BASE_PATH="/usr/local"#BASE_PATH="'$RPM_BUILD_ROOT'/usr"#' install.sh

%build


%install
./install.sh --no-sudo
exit 1

%files
%doc



%changelog

