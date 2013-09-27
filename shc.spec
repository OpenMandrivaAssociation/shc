#disabling debuginfo
%global debug_package %{nil}
%global _enable_debug_packages %{nil}

%define version 3.8.9

# packages
%define name shc

Name:              %{name}
Version:           %{version}
Release:		   %mkrel 1
Summary:           Generic Shell Compiler
License:           GPLv2
Group:             Development/Other
URL:               http://oem.mandriva.com.br
BuildRoot:         %{_tmppath}/%{name}-root
BuildRequires:     gcc 
Requires:          bash
Provides:          shc = %{version}
Source0:           shc-%{version}.tar.gz
Patch0:            0001-makefile.patch

%description
shc is a generic Shell Script compiler developed by
Francisco Javier Rosales García (http://www.datsi.fi.upm.es/~frosal/)

%prep
%setup -q %SOURCE0
%patch0 -p1

%build
make

%install
# create dirs
export DONT_STRIP=1
rm -rf %buildroot
install -d -m 0755 %buildroot
install -d -m 0755 %buildroot/usr
install -d -m 0755 %buildroot/usr/bin

#copying binary file
cp -fv shc-%{version} %buildroot/usr/bin/

%post
# linking executable file to an alias
ln -sf /usr/bin/shc-%{version} /usr/bin/shc

%files
%defattr(-,root,root)
/usr/bin/shc-%{version}

%changelog
* Thu Sep 12 2013 Marco A Benatto <benatto@mandriva.com.br> 3.8.9
- Package creation
