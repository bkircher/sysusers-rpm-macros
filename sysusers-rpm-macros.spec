Name:           sysusers-rpm-macros
Version:        1
Release:        1%{?dist}
Summary:        RPM macros for packages creating system accounts

License:        GPLv2
URL:            https://github.com/bkircher/sysusers-rpm-macros

# sysusers https://src.fedoraproject.org/rpms/systemd/c/ced9237a14d6775a98e1a2f93880990417b4ae6e
Source0:        macros.sysusers
Source1:        sysusers.attr
Source2:        sysusers.prov
Source3:        sysusers.generate-pre.sh

BuildArch:      noarch
#Provides systemd-rpm-macros, backported from Fedora systemd
Provides:       systemd-rpm-macros


%description
%{summary}.

Backport of macros.sysusers from Fedora/systemd.

%prep
%autosetup -c -D -T

%build
# Nothing to build

%install
# sysusers
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs/
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/fileattrs/
install -Dpm 0755 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/
install -Dpm 0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/

%files
# sysusers
%{_rpmconfigdir}/macros.d/macros.sysusers
%{_rpmconfigdir}/fileattrs/sysusers.attr
%{_rpmconfigdir}/sysusers.prov
%{_rpmconfigdir}/sysusers.generate-pre.sh

%changelog
* Fri Jan 7 2021 Ben Kircher <bkircher@0xadd.de> - 1-1
- Initial package
