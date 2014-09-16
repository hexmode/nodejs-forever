%define _binary_payload w9.gzdio
%define logdir /var/log
%define gitrepo https://github.com/hexmode/node-forever-rpm
%define srcgit http://github.com/nodejitsu/forever
%define git_checkout v0.11.1
%define pkgname nodejs-forever
%define instdir $RPM_BUILD_ROOT%{_libdir}/node_modules/%{pkgname}

Summary: A simple CLI tool for ensuring that a given script runs continuously (i.e. forever)
Name: %{pkgname}
Version: 0.11.1
Release: 1
URL: http://github.com/nodejitsu/forever
Vendor:  nodejitsu
Packager: Mark A. Hershberger <mah@nichework.com>
Source0: %{srcgit}
License: MIT
Group: System Environment/Daemons
BuildRoot: %buildroot
BuildArch: noarch
Requires: initscripts >= 8.36, node-forever
Requires(post): chkconfig
Requires(pre): /usr/sbin/useradd

%description
A simple CLI tool for ensuring that a given script runs continuously (i.e. forever)

%install
mkdir -p %{instdir}
if [ ! -d $RPM_SOURCE_DIR/%{pkgname} ]; then
    cd $RPM_SOURCE_DIR
    git clone %{srcgit} %{pkgname}
    cd %{pkgname}
    git checkout %{git_checkout}
    git submodule init
    git submodule update
fi

mkdir -p %{instdir}
rm -rf %{instdir}/tests
cp -pr $RPM_SOURCE_DIR/%{pkgname}/node_modules %{instdir}

%pre
# noop

%prep
# noop

%build
# noop

%clean
# noop

%post
# noop

%preun
# noop

%files
%defattr(-,root,root,-)



%changelog
* Tue Sep 16 2014 Mark A. Hershberger  <mah@nichework.com>

    Initial Version
