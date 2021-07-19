%define kernel_version %(uname -r|cut -d- -f1)
%define subversion     %(uname -r|cut -d- -f2|cut -d. -f 1-2)
%define el_subversion  %(uname -r|cut -d- -f2|cut -d. -f 3)
%define el_release     %(cat /etc/redhat-release|grep -o '[0-9]*\\.[0-9]*')
%define file_release   el%(echo %el_release|sed 's/\\./_/')

Name:		kernel-mod-logitech		
Version:	%{kernel_version}
Release:	1%{?dist}
Summary:	Logitech Gamepad and Joystick support

Group:		kernel modules
License:	??
URL:		http://rocky-linux.org	
Source0:	https://download.rockylinux.org/pub/rocky/%{el_release}/BaseOS/source/tree/Packages/kernel-%{version}-%{subversion}.%{el_subversion}.%{file_release}.src.rpm	

BuildRequires: elfutils-libelf-devel
BuildRequires: bc
BuildRequires: openssl-devel
BuildRequires: python3

%description
Updated kernel modules for Logitech Gamepad and Joystick support

%prep
%setup -q -T -c %{name}
rpm2cpio %{SOURCE0}|cpio -ivd
tar -xvf linux-%{version}-%{subversion}.%{el_subversion}.%{file_release}.tar.xz

%build
cd linux-%{version}-%{subversion}.%{el_subversion}.%{file_release}
cp %{_builddir}/%{name}-%{version}/kernel-x86_64.config .config
sed -i 's/# CONFIG_LOGITECH_FF is not set/CONFIG_LOGITECH_FF=y/g' .config
sed -i 's/# CONFIG_LOGIRUMBLEPAD2_FF is not set/CONFIG_LOGIRUMBLEPAD2_FF=y/g' .config
sed -i 's/# CONFIG_LOGIG940_FF is not set/CONFIG_LOGIG940_FF=y/g' .config
sed -i 's/# CONFIG_LOGIWHEELS_FF is not set/CONFIG_LOGIWHEELS_FF=y/g' .config
make -j $(nproc) olddefconfig 
make -j $(nproc) prepare
make -j $(nproc) modules_prepare
make -j $(nproc) M=drivers/hid

%install
cd linux-%{version}-%{subversion}.%{el_subversion}.%{file_release}
mkdir -p %{_buildroot}/etc/modprobe.d/
cat << EOF > %{_buildroot}/etc/modprobe.d/logitech.conf
# Fix for hid_logitech -1 error
blacklist joydev
EOF
mkdir -p %{buildroot}/lib/modules/%{version}-%{subversion}.%{release}_%{el_subversion}/extra
cp  drivers/hid/hid-logitech.ko %{buildroot}/lib/modules/%{version}-%{subversion}.%{release}_%{el_subversion}/extra

%files

%post
depmod -a
dracut -f /boot/initramfs-$(uname -r).img $(uname -r)

%changelog

