Name:		kernel-mod-logitech		
Version:	4.18.0
Release:	1%{?dist}
Summary:	Logitech Gamepad and Joystick support

# Ensure these valius reflect the latest kernel and el release
%define subversion 240.22
%define el_subversion 3

Group:		kernel modules
License:	??
URL:		http://rocky-linux.org	
Source0:	https://download.rockylinux.org/pub/rocky/8.3/BaseOS/source/tree/Packages/kernel-%{version}-%{subversion}.%{release}.src.rpm	

BuildRequires: elfutils-libelf-devel
BuildRequires: bc
BuildRequires: openssl-devel

%description
Updated kernel modules for Logitech Gamepad and Joystick support

%prep
%setup -q -T -c %{name}
rpm2cpio %{SOURCE0}|cpio -ivd
tar -xvf linux-%{version}-%{subversion}.%{release}_%{el_subversion}.tar.xz

%build
cd linux-%{version}-%{subversion}.%{release}_%{el_subversion}
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
cd linux-%{version}-%{subversion}.%{release}_%{el_subversion}
mkdir -p %{_buildroot}/etc/modprobe.d/
cat << EOF > %{_buildroot}/etc/modprobe.d/logitech.conf
# Fix for hid_logitech -1 error
blacklist joydev
EOF
mkdir -p %{_buildroot}/lib/modules/%{version}-%{subversion}.%{release}_%{el_subversion}/extra
cp  drivers/hid/hid-logitech.ko %{_buildroot}/lib/modules/%{version}-%{subversion}.%{release}_%{el_subversion}/extra
exit 1

%files



%changelog

