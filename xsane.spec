%define name xsane
%define version 0.996
%define release 1
%define prefix /usr

Name: %{name}
Version: %{version}
Release: %{release}
Summary: XSane is a graphical frontend for scanners. It uses the library SANE.
Group: Graphics
URL: http://www.xsane.org
Buildroot: /var/tmp/%{name}-buildroot
Requires: sane-backends
Source: ftp://ftp.mostang.com/pub/sane/xsane/%{name}-%{version}.tar.gz
Copyright: GPL
BuildRequires: gtk+ >= 1.2.0 sane-backends-devel >= 1.0.2

%description
Xsane is a grahical frontend for sane. Install this if you want a grahpical
frontend for sane for use in the X Windowing System.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
uname -a | grep -qi SMP && make -j 2 || make

%install
rm -rf %{buildroot}  
mkdir -p %{buildroot}%{prefix}
make prefix=%{buildroot}%{prefix} install
strip %{buildroot}%{prefix}/bin/* || :

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc xsane*
/usr/share/*
/usr/bin/xsane
/usr/man/man1/xsane.1*
