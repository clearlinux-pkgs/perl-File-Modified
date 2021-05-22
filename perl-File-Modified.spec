#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Modified
Version  : 0.10
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Modified-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Modified-0.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-modified-perl/libfile-modified-perl_0.10-1.debian.tar.xz
Summary  : 'checks intelligently if files have changed'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Modified-license = %{version}-%{release}
Requires: perl-File-Modified-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
File::Modified version 0.02
=========================
This module provides an easy way for long running processes
(like daemons) to determine whether a file was changed since
the last time it was checked. Also, some persistence now
allows you to use it as a more general caching mechanism.

%package dev
Summary: dev components for the perl-File-Modified package.
Group: Development
Provides: perl-File-Modified-devel = %{version}-%{release}
Requires: perl-File-Modified = %{version}-%{release}

%description dev
dev components for the perl-File-Modified package.


%package license
Summary: license components for the perl-File-Modified package.
Group: Default

%description license
license components for the perl-File-Modified package.


%package perl
Summary: perl components for the perl-File-Modified package.
Group: Default
Requires: perl-File-Modified = %{version}-%{release}

%description perl
perl components for the perl-File-Modified package.


%prep
%setup -q -n File-Modified-0.10
cd %{_builddir}
tar xf %{_sourcedir}/libfile-modified-perl_0.10-1.debian.tar.xz
cd %{_builddir}/File-Modified-0.10
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Modified-0.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Modified
cp %{_builddir}/File-Modified-0.10/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Modified/4b17c72c9423b73ac0db0e2ca682554614efd516
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Modified/f13ca1b4792d204a3abf16816cb1f8adabb34cba
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Modified.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Modified/4b17c72c9423b73ac0db0e2ca682554614efd516
/usr/share/package-licenses/perl-File-Modified/f13ca1b4792d204a3abf16816cb1f8adabb34cba

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/File/Modified.pm
