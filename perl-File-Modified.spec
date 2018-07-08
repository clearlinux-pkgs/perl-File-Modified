#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Modified
Version  : 0.10
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Modified-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Modified-0.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-modified-perl/libfile-modified-perl_0.10-1.debian.tar.xz
Summary  : 'checks intelligently if files have changed'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Modified-license
Requires: perl-File-Modified-man

%description
File::Modified version 0.02
=========================
This module provides an easy way for long running processes
(like daemons) to determine whether a file was changed since
the last time it was checked. Also, some persistence now
allows you to use it as a more general caching mechanism.

%package license
Summary: license components for the perl-File-Modified package.
Group: Default

%description license
license components for the perl-File-Modified package.


%package man
Summary: man components for the perl-File-Modified package.
Group: Default

%description man
man components for the perl-File-Modified package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n File-Modified-0.10
mkdir -p %{_topdir}/BUILD/File-Modified-0.10/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Modified-0.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-File-Modified
cp LICENSE %{buildroot}/usr/share/doc/perl-File-Modified/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-File-Modified/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/File/Modified.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-File-Modified/LICENSE
/usr/share/doc/perl-File-Modified/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/File::Modified.3
