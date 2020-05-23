
#! /bin/sh
rpmbuild -bi ~/rpmbuild/SPECS/vlc.spec
if [[ 0 -eq 0 ]]
then
    rpmbuild -bl ~/rpmbuild/SPECS/vlc.spec 2>&1| sort -u|grep '^   '|grep -v '(but unpackaged)'|tr -d ' ' > /tmp/package_files.log
    sed -i -e 's/\/usr\/bin\//%{_bindir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\/sbin\//%{_sbindir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\/lib64\//%{_libdir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\/include\//%{_includedir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\/libexec\//%{_libexecdir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\/share\/man\//%{_mandir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\/share\/info\//%{_infodir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\/share\/doc\//%{_docdir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\/share\//%{_datadir}\//g' /tmp/package_files.log
    sed -i -e 's/\/etc\//%{_sysconfdir}\//g' /tmp/package_files.log
    sed -i -e 's/\/run\//%{_rundir}\//g' /tmp/package_files.log
    sed -i -e 's/\/var\/lib\//%{_sharedstate-dir}\//g' /tmp/package_files.log
    sed -i -e 's/\/var\//%{_localstate-dir}\//g' /tmp/package_files.log
    sed -i -e 's/\/usr\//%{_exec_prefix}\//g' /tmp/package_files.log
    cat /tmp/package_files.log|egrep -v -e '*.so$|*.h$|*.pc$' > /tmp/FILES.LOG;     cat /tmp/package_files.log|egrep -e '*.so$|*.h$|*.pc$' > /tmp/DEVEL_FILES.LOG
    sed -i -e '/%files[\s]*$/r /tmp/FILES.LOG' /root/rpmbuild/SPECS/vlc.spec;     sed -i -e '/%files devel[\s]*$/r /tmp/DEVEL_FILES.LOG' /root/rpmbuild/SPECS/vlc.spec
    rpmbuild -ba ~/rpmbuild/SPECS/vlc.spec
fi

