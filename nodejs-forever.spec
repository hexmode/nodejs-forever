%define _binary_payload w9.gzdio
%define logdir /var/log
%define gitrepo https://github.com/hexmode/nodejs-forever
%define srcgit https://github.com/nodejitsu/forever.git
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
Source0: %{gitrepo}
License: MIT
Group: System Environment/Daemons
BuildRoot: %buildroot
BuildArch: noarch
BuildRequires: npm
Requires: initscripts >= 8.36, npm
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
cd $RPM_SOURCE_DIR/%{pkgname}
npm config set prefix=$RPM_BUILD_ROOT/usr
npm install -g

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

/usr/bin
%{_libdir}



%changelog
* Tue Sep 16 2014 Mark A. Hershberger  <mah@nichework.com>

    Initial Version
