#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ioc-cbc-tools
Version  : 2018ww34.5
Release  : 4
URL      : https://github.com/intel/ioc-cbc-tools/archive/2018ww34.5.tar.gz
Source0  : https://github.com/intel/ioc-cbc-tools/archive/2018ww34.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ioc-cbc-tools-bin
Requires: ioc-cbc-tools-config
Requires: ioc-cbc-tools-autostart
Requires: ioc-cbc-tools-data
Requires: ioc-cbc-tools-license
BuildRequires : acrn-hypervisor-dev
BuildRequires : pkgconfig(fuse)

%description
# ioc-cbc-tools
IOC stands for IO controller which is used for automotive system.
CBC stands for carrier board communiction protocol.

%package autostart
Summary: autostart components for the ioc-cbc-tools package.
Group: Default

%description autostart
autostart components for the ioc-cbc-tools package.


%package bin
Summary: bin components for the ioc-cbc-tools package.
Group: Binaries
Requires: ioc-cbc-tools-data
Requires: ioc-cbc-tools-config
Requires: ioc-cbc-tools-license

%description bin
bin components for the ioc-cbc-tools package.


%package config
Summary: config components for the ioc-cbc-tools package.
Group: Default

%description config
config components for the ioc-cbc-tools package.


%package data
Summary: data components for the ioc-cbc-tools package.
Group: Data

%description data
data components for the ioc-cbc-tools package.


%package license
Summary: license components for the ioc-cbc-tools package.
Group: Default

%description license
license components for the ioc-cbc-tools package.


%prep
%setup -q -n ioc-cbc-tools-2018ww34.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535081675
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1535081675
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ioc-cbc-tools
cp LICENSE %{buildroot}/usr/share/doc/ioc-cbc-tools/LICENSE
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../cbc_attach.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/cbc_attach.service
ln -s ../cbc_lifecycle.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/cbc_lifecycle.service
ln -s ../cbc_thermald.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/cbc_thermald.service
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/cbc_attach.service %{buildroot}/usr/share/clr-service-restart/cbc_attach.service
ln -sf /usr/lib/systemd/system/cbc_lifecycle.service %{buildroot}/usr/share/clr-service-restart/cbc_lifecycle.service
ln -sf /usr/lib/systemd/system/cbc_thermald.service %{buildroot}/usr/share/clr-service-restart/cbc_thermald.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/cbc_attach.service
/usr/lib/systemd/system/multi-user.target.wants/cbc_lifecycle.service
/usr/lib/systemd/system/multi-user.target.wants/cbc_thermald.service

%files bin
%defattr(-,root,root,-)
/usr/bin/cbc_attach
/usr/bin/cbc_lifecycle
/usr/bin/cbc_thermal
/usr/bin/cbc_thermal_chart.py
/usr/bin/cbc_thermald_start

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/cbc_attach.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/cbc_lifecycle.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/cbc_thermald.service
/usr/lib/systemd/system/cbc_attach.service
/usr/lib/systemd/system/cbc_lifecycle.service
/usr/lib/systemd/system/cbc_thermald.service

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/cbc_attach.service
/usr/share/clr-service-restart/cbc_lifecycle.service
/usr/share/clr-service-restart/cbc_thermald.service
/usr/share/ioc-cbc-tools/cbc_match.txt
/usr/share/ioc-cbc-tools/thermal-conf.xml

%files license
%defattr(-,root,root,-)
/usr/share/doc/ioc-cbc-tools/LICENSE
