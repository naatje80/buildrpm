Name: libnfs
Summary: NFS client library
Vendor: Ronnie Sahlberg
Packager: ronniesahlberg@gmail.com
Version: 4.0.0
Release: 1
Epoch: 0
License: GNU LGPL version 2.1
Group: System Environment/Libraries
URL: http://www.github.com/sahlberg/libnfs

Source: https://github.com/sahlberg/libnfs/archive/refs/tags/libnfs-%{version}.tar.gz

Provides: lib = %{version}

Prefix: /usr
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
LibNFS is a NFS client library

#######################################################################



%prep
%setup -q -n %{name}-%{name}-%{version}
# setup the init script and sysconfig file
#%setup -T -D -n %{name}-%{name}-%{version} -q

%build

## check for ccache
if ccache -h >/dev/null 2>&1 ; then
	CC="ccache gcc"
else
	CC="gcc"
fi

export CC

## always run autogen.sh
aclocal
autoheader
autoconf
libtoolize -c -f -i
automake --add-missing


CFLAGS="$RPM_OPT_FLAGS $EXTRA -O2 -g -D_GNU_SOURCE" %configure

%install
# Clean up in case there is trash left from a previous build
rm -rf $RPM_BUILD_ROOT

# Create the target build directory hierarchy

make DESTDIR=$RPM_BUILD_ROOT install

# Remove "*.old" files
find $RPM_BUILD_ROOT -name "*.old" -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT


#######################################################################
## Files section                                                     ##
#######################################################################

%files
%defattr(-,root,root)

%{_libdir}/libnfs.so*

%package devel
Summary: Development libraries for LibNFS
Group: Development

%description devel
development libraries for LibNFS

%files devel
%defattr(-,root,root)
%{_includedir}/nfsc/libnfs.h
%{_includedir}/nfsc/libnfs-zdr.h
%{_includedir}/nfsc/libnfs-raw.h
%{_includedir}/nfsc/libnfs-raw-mount.h
%{_includedir}/nfsc/libnfs-raw-nfs.h
%{_includedir}/nfsc/libnfs-raw-nfs4.h
%{_includedir}/nfsc/libnfs-raw-portmap.h
%{_includedir}/nfsc/libnfs-raw-rquota.h
%{_includedir}/nfsc/libnfs-raw-nlm.h
%{_includedir}/nfsc/libnfs-raw-nsm.h
%{_libdir}/libnfs.a
%{_libdir}/libnfs.la
%{_libdir}/pkgconfig/libnfs.pc

%package utils
Summary: Utility programs for LibNFS
Group: Applications/System

%description utils
Utility programs for LibNFS

%files utils
%defattr(-,root,root)
%{_bindir}/nfs-cat
%{_bindir}/nfs-cp
%{_bindir}/nfs-ls
%{_mandir}/man1/nfs-cat.1.gz
%{_mandir}/man1/nfs-cp.1.gz
%{_mandir}/man1/nfs-ls.1.gz

%changelog
* Wed Feb 13 2019 : Version 4.0.0
- Fix the versioning in makerpms.sh
- Fix some compile issues in the test programs.
- NFSv3: skip commit on close if the file has not been written to.
- Add nfs_umount() to NFSv3
- Add nfs_statvfs64()
- Fix invalid shift of pid_t when generating rpc->xid
- Compile fixes for Mac OSX
- Fix for dup2() on Windows
- NFSv4 fix for directory handling
- Improvements to configure/bulding
* Sun Jun 24 2018 : Version 3.0.0
 - NFSv4 support.
 - lockf() support (NFSv4 only).
 - fcntl() support for locking (NFSv4 only).
 - Add CMake support.
 - URL arguments to select NFS version.
 - URL argument to set nfsport. This allows NFSv4 to work for
 servers without portmapper support.
 - URL argument to set he mount port.
 - NFSv4: use getpwnam to map NFSv4 (Ganesha) when passing uid/gid
 as a user/group name insead of as a uid/gid.
 - Added nfs-fh: a simle utility to print the filehandle for a nfs file.
 - Win32 build fixes.
 - Add a new open2() function that takes a mode argument.
 - Add a testsuite for libnfs.
* Fri Jun 16 2017 : Version 2.0.0
 - Add RPC/RAW layer support for NFSv4
 - Add support for building RPC servers using libnfs
 - Add support for setting RPC timeouts for all interfaces.
 - Add O_NOFOLLOW to nfs_open()
 - Add a new mkdir2 command that also takes a mode argument.
 - Add a new readlink2 command that avoids having to preallocate the
   output buffer.
 - Build fixes for Mingw and Cygwin.
 - Use SOCK_CLOEXEC for the sockets
 - Make rpc_set{g|u}id() public
 - Performance optimization: socket: Batch pdu read in rpc_read_from_socket
 - Fix NULL pointer crash in nfs_link().
 - Clamp read/write size for servers (Ganesha) that offer very large io sizes
   instead of failing to connect to the export.
 - Tell the server to commit all data to stable storage when we close files.
 - Double free fix: don't call rpc_free_pdu() after rpc_queue_pdu() failure.
 - Fix for memory leak in rpc_allocate_*().
 - Fixes to build nfs-ls and nfs-cp on win32.
 - Abort the mount process correctly if MOUNT/MNT returns error or is cancelled.
 - Fix memory leak in error path in nfs_create_2_cb().
 - Fix leak of rpc->inbuf if we destroy the context while we still have PDUs
   in flight.
* Sun Oct 9 2016 : Version 1.11.0
 - Reduce the number of memory allocations in the ZDR layer.
 - Check both seconds and nanoseconds field when validating dir cache.
 - Invalidate the dir cache immediately if we do something that would cause
   it to become stale, such as adding/removing objects from the cache.
 - Add options to enable/disable dir caching.
 - Discard readahead cache on [p]write and truncate.
 - Android fixes
 - Windows fixes
 - Support timeouts for sync functions
 - Add an internal pagecache
 - Add nfs_rewinddir(), nfs_seekdir() and nfs_telldir()
 - Fix crash in nfs_truncate()
 - Fix segfault that can trigger if we rpc_disconnect() during the mount.
 - Add support to bind to a specific interface (linux only)
* Sun Jan 31 2016 : Version 1.10.0
 - Fix a leak where we leaked one rdpe_cb_data structure on each open_dir()
 - Make building the utils optional
 - Android: the correct define is __ANDROID__ not ANDROID
 - Win32: Use _U_ instead of ATTRIBURE((unused))
 - Win32: Fix nfs_stat declaration for Win32
 - Various fixes for mingw builds
 - Make rpc->connect_cb a one shot callback and improve documentation
 - Remove the FUSE module. It now lives in its own repo
 - Fix POLLERR/POLLHUP handling to properly handle session failures and to
   try to auto-reconnect
* Sun Aug 2 2015 : Version 1.9.8
 - Disable multithreading in fuse_nfs
 - Add -Wall and -Werror compiler flags (and fix issues found by it)
 - Add nfs-cat utility
 - Switch to using nfs_[f]stat64 instead of the deprecated nfs_[f]stat call
   in all examples
 - If the server does not return any atttributes for entries in READDIRPLUS
   then try to fetch them using lookup instead.
 - Reconnection fixes
 - Enforce the max pdu size and add sanity checks when reading PDUs from
   the socket.
 - Stop using ioctl(FIONREAD) to find out how many bytes to read, and treat
   0 as an indication of a problem. Some applications call their POLLIN handlers
   spuriosly even when there is no data to read, which breaks this check in
   libnfs.
 - Add basic support to do logging.
* Mon Feb 9 2015 : Version 1.9.7
 - Auto-traverse mounts. With this option (default to on) libnfs will
   autodiscover and handle any nested submounts.
 - Remove nfs_get_current_offset. Applications should use seek instead of this function.
 - Add umask() support.
 - Change set_tcp_sockopt() to be static.
 - Android fix for nfs-ls
 - Make S_IFLNK available on windows.
 - Fix a use after free.
 - Fix a bug where truncate() treated offset as 32bit.
* Tue Nov 25 2014 : Version 1.9.6
 - Add O_TRUNC support for nfs_create
 - Handle OOM during create
 - Return more stats fields as part of readdir since we get these for "free"
   when we use READDIRPLUS
 - Follow symlinks during path resolution
 - Add lchown, lstat and lutimes
 - Replace all [u_]quad types with [u]int types in our RPC layer
 - Solaris build fixes
* Sat Jul 19 2014 : Version 1.9.5
 - Remove old ONC-RPC symbols
* Wed Mar 19 2014 : Version 1.9.3
 - Add O_TRUNC support to nfs_open()
 - Add a simple but incomplete LD_PRELOAD tool
 - Fixes for some memory leaks and C++ compile support
 - Make ANDROID default uid/gid to 65534
 - Allow the READDIRPLUS emulation to still work if some objects
   in the direcotry can not be lookedup (NFSv4 ACL denying READ-ATTRIBUTES)
 - Have libnfs retry any read/write operations where the server responds
   with a short read/write. Some servers do this when they are overloaded?
* Thu Jan 30 2014 : Version 1.9.2
 - Remove chdir change. This needs more testing.
* Tue Jan 28 2014 : Version 1.9.1
 - Restore libnfs-raw-*.h to make install
* Mon Jan 27 2014 : Version 1.9
 - Use _stat64 on windows so file sizes become 64bit always.
 - Increase default marshalling buffer so we can marshall large PDUs.
 - RPC layer support for NFSv2
 - Win32 updates and fixes
 - Add URL parsing functions and URL argument support.
 - New utility: nfs-io
 - nfs-ls enhancements
 - RPC layer support for NSM
 - Add example FUSE filesystem.
 - Minor fixes.
* Wed Oct 30 2013 : Version 1.8
 - Fix nasty memory leak in read_from_socket
 - minor updates
* Sun Oct 20 2013 : Version 1.7
 - Allow nested eventloops so that a sync function can be called from a callback.
 - Fix a bug in unmarshalling a uint64.
 - Add PATHCONF support.
 - WIN32/64 updates
 - AROS updates
* Mon May 27 2013 : Version 1.6
 - AROS/Amiga support
 - Chose better initial xid value to reduce the probability for collissions.
 - Set default group to getgid() instead of -1. This fixes an interoperability
 problem with 3.9 linux knfsd.
* Mon Dec 3 2012 : Version 1.5
 - Switch to using our own RPC/XDR replacement ZDR instead of relying on the
   system RPC/TIRPC libraries. This allows using libnfs on platforms that lack
   RPC libraries completely.
 - Add support for Android.
* Sun Nov 25 2012 : Version 1.4
 - Add trackig of freed context and assert on using a context after it has been
   freed.
 - Windows x64 support and fixes.
 - Switch to using our own version of xdr_int64() since the one in libtirpc
   crashes on some platforms.
 - Fix memory leak in an error path for addrinfo.
 - Fix bug dereferencing a null pointer in the mount callback on error.
* Sat Mar 3 2012 : Version 1.3
 - add set/unset to portmapper
 - add mount v1
 - try to rotate to find a free port better
 - minor fixes
* Tue Dec 6 2011 : Version 1.2
 - Add support for MKNOD
 - Add support for HaneWin NFS server
 - Change all [s]size_t offset_t to be 64bit clean scalars
* Sun Nov 27 2011 : Version 1.1
 - Fix definition and use of AUTH
 - Only call the "connect" callback if non-NULL
 - make sure the callback for connect is only invoked once for the sync api
 - make file offset bits 64 bits always
* Sun Jul 31 2011 : Version 1.0
 - Initial version
