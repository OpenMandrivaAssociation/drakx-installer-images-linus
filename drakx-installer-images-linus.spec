%define base_name drakx-installer-images
%define name %{base_name}-linus
%define version 1.31
%define release %mkrel 4
%define theme 	Free

%define mandriva_version %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' mandriva-release)

# disable empty debug rpms...
%define _enable_debug_packages  %{nil}
%define debug_package           %{nil}

Summary: DrakX installer images using kernel-linus series
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{base_name}-%{version}.tar.bz2
Patch0:  %{name}.patch
License: GPL
Group:   Development/Other
Url:     http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kernel-linus-latest >= 2.6.28-0.rc9.%mkrel 1
%ifarch %ix86 x86_64
BuildRequires: memtest86+
BuildRequires: grub
BuildRequires: syslinux >= 3.51-%mkrel 4
%endif
BuildRequires: drakx-installer-binaries >= 1.32-%mkrel 1
BuildRequires: ldetect-lst >= 0.1.199
BuildRequires: mandriva-theme-%{theme}
BuildRequires: pcmciautils
BuildRequires: perl-XML-Parser

BuildRequires: cdrkit-genisoimage
BuildRequires: mkdosfs-with-dir
BuildRequires: mknod-m600
BuildRequires: mtools
Buildrequires: busybox
Buildrequires: ka-deploy-source-node

%description
images needed to build Mandriva installer (DrakX) using kernel-linus series

%prep
%setup -q -n %{base_name}-%{version} 
%patch0 -p1

%build
THEME=Mandriva-%{theme} make -C images

%install
rm -rf $RPM_BUILD_ROOT

dest=$RPM_BUILD_ROOT%{_libdir}/%name
mkdir -p $dest
make -C images install ROOTDEST=$dest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/%name




