%define relabel_files() restorecon -R -v /usr/bin & restorecon -R -v /usr/lib/systemd/system

%define selinux_policy_version 3.13.0

Name:           ssh-monitoring
Version:        1.0
Release:        1%{?dist}
Summary:        SSH Monitoring Service
Group:          Testing
License:        GPL
URL:            https://github.com/Nemo-adm/OSS-2021/service
Source0:        %{name}-%{version}.tar.gz
Source1:        ssh_monitoring.pp
Source2:        ssh_monitoring.if
BuildRequires:  /bin/cp, /bin/mkdir, /bin/rm, /bin/sudo, libnotify-devel, selinux-policy-devel, systemd
Requires:       /bin/bash, /usr/bin/awk, /usr/bin/cut, /usr/bin/echo, /usr/bin/grep, /usr/bin/logger, /usr/bin/ps, /usr/bin/tr
Requires(post): libselinux-utils, policycoreutils, selinux-policy-base >= %{selinux_policy_version}, selinux-policy-targeted >= %{selinux_policy_version}
BuildArch:      noarch

%description
SSH Monitoring Service

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/systemd/system
mkdir -p %{buildroot}%{_mandir}/man8
install -m 755 ssh-monitoring %{buildroot}%{_bindir}
install -m 644 ssh-monitoring.service %{buildroot}/etc/systemd/system
install -m 644 ssh-monitoring.8.gz %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -d %{buildroot}/etc/selinux/targeted/contexts/users
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/selinux/devel/include/contrib

%post
semodule -n -i %{_datadir}/selinux/packages/ssh_monitoring.pp
if /usr/sbin/selinuxenabled; then
    /usr/sbin/load_policy
    %relabel_files
fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r ssh-monitoring
    if /usr/sbin/selinuxenabled; then
       /usr/sbin/load_policy
       %relabel_files
    fi;
fi;
exit 0

%files
%{_bindir}/ssh-monitoring
/etc/systemd/system/ssh-monitoring.service
%{_mandir}/man8/ssh-monitoring.8.gz
%defattr(-, root, root, 0755)
%attr(0600, root, root)
%{_datadir}/selinux/packages/ssh_monitoring.pp
%{_datadir}/selinux/devel/include/contrib/ssh_monitoring.if

%changelog
* Sun May 22 2022 Nick Izyurov
- Added %{_bindir}/ssh-monitoring.spec
