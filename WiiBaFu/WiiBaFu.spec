%define 	build_timestamp %(date +"%Y%m%d")

Name:		WiiBaFu
Version:	gitbuild
Release:	%{build_timestamp}.1%{?dist}
Summary:	Wit Tools GUI

Group:		Gaming
License:	todo
URL:		todo

BuildRequires:	qt5-qtbase-devel

Requires:	qt5-qtbase
Requires:	wit-tools


%description
The complete and simple to use backup solution for your Wii games 

%prep
rm -rf %{name}
git clone --depth 1 https://git.code.sf.net/p/wiibafu/code %{name}
cd %{name}

%build
cd %{name}
qmake-qt5 WiiBaFu.pro
make %{?_smp_mflags}
cat << EOF > org.wiibafu.pkexec.wiibafu.policy
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE policyconfig PUBLIC
 "-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
 "http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd">
<policyconfig>
    <action id="org.freedesktop.policykit.pkexec.wiibafu">
    <description>Run gedit program</description>
    <message>Authentication is required to run the wiibafu</message>
    <icon_name>WiiBaFu</icon_name>
    <defaults>
        <allow_any>auth_admin</allow_any>
        <allow_inactive>auth_admin</allow_inactive>
        <allow_active>auth_admin</allow_active>
    </defaults>
    <annotate key="org.freedesktop.policykit.exec.path">/usr/bin/WiiBaFu</annotate>
    <annotate key="org.freedesktop.policykit.exec.allow_gui">true</annotate>
    </action>
</policyconfig>
EOF
cat << EOF >> WiiBaFu
#! /bin/bash
export TERM=xterm-256color
export XDG_CURRENT_DESKTOP=GNOME
 
/usr/bin/WiiBaFu_exec ${0}
EOF

%install
cd %{name}
%make_install INSTALL_ROOT=${RPM_BUILD_ROOT}
sed -i 's/^Exec=.*/Exec=\/usr\/bin\/pkexec \/usr\/bin\/WiiBaFu/' ${RPM_BUILD_ROOT}/usr/share/applications/WiiBaFu.desktop
install -m 755 -d %{buildroot}/usr/share/polkit-1/actions
install -m 644 -t %{buildroot}/usr/share/polkit-1/actions org.wiibafu.pkexec.wiibafu.policy
mv %{buildroot}/%{_bindir}/WiiBaFu %{buildroot}/%{_bindir}/WiiBaFu_exec
install -m 755 -t %{buildroot}/%{_bindir} WiiBaFu
 
%files
%doc



%changelog
