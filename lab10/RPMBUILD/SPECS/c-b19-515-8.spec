Name:       c-b19-515-8
Version:    1.0
Release:    1%{?dist}
Summary:    simple program
Group:      Testing
License:    GPL
URL:        https://github.com/Nemo-adm/OSS-2021
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-b19-515-8 c-b19-515-8.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b19-515-8 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/b19-515-8-1.0-1.el8.noarch.rpm --force
%files
%{_bindir}/c-b19-515-8

%changelog
* Fri May 20 2022 Izyurov 
- Added %{_bindir}/c-b19-515-8
