Name:		vhba-module
Version:	20200106
Release:	1%{?dist}
Summary:	VHBA module provides a Virtual (SCSI) HBA, which is the link between userspace daemon and linux kernel.

Group:	 	System Tools	
License:	GPLv2+
URL:		http://cdemu.sourceforge.net
Source0:	https://github.com/cdemu/cdemu/archive/%{name}-%{version}.tar.gz

BuildRequires:	kernel-devel
BuildRequires:	kernel-core
BuildRequires:  elfutils-libelf-devel

Requires:       elfutils-libelf

%description
VHBA module provides a Virtual (SCSI) HBA, which is the link between userspace daemon and linux kernel.

Contrary to what some might expect due to the "userspace" part of the name, userspace CDEmu still needs a kernel module, just like the original CDEmu - the difference is that userspace CDEmu does all the processing (i.e. file reading, fake data generation, etc.) in userspace.

Kernel module takes care of device emulation in the kernel; it registers virtual device with appripriate drivers and creates corresponding device nodes. It also creates a special character device that is used for communication with userspace.

As a virtual device is accessed, requests are generated by kernel, which are in fact SCSI commands. These are passed to userspace daemon via afore-mentioned character device. Once it processes the request, the daemon returns corresponding data and status to kernel, thus completing the request.

The whole process is very similar to accessing a real device, except that requests are passed to userspace daemon instead to hardware.

Early, experimental versions of userspace-cdemu used a module that was called cdemu-module. This release is based on VHBA module, which was written by Chia-I Wu. Contrary to cdemu-module, which implemented all the interfaces (i.e. block device, uniform CD-ROM driver, etc.) manually, VHBA implements virtual SCSI host adapter and lets the kernel's SCSI layer do the rest. This approach is cleaner, faster and more robust.

%prep
cat << EOF > %{_sourcedir}/vhba.conf
# Load vhba module for cdemu
vhba
EOF
cat << EOF > %{_sourcedir}/40-vhba.rules
KERNEL=="vhba_ctl", SUBSYSTEM=="misc", TAG+="uaccess"
EOF
%setup -q -n cdemu-%{name}-%{version}/vhba-module


%build
make %{?_smp_mflags}


%install
install -d %{buildroot}/lib/modules/%(uname -r)/extra
install -d %{buildroot}/etc/udev/rules.d
install -d %{buildroot}/etc/modules-load.d
install -m 644 %{_builddir}/cdemu-%{name}-%{version}/vhba-module/vhba.ko %{buildroot}/lib/modules/%(uname -r)/extra
install -m 644 %{_sourcedir}/40-vhba.rules %{buildroot}/etc/udev/rules.d
install -m 644 %{_sourcedir}/vhba.conf %{buildroot}/etc/modules-load.d

%files
%doc

%post
depmod %(uname -r)

%changelog

