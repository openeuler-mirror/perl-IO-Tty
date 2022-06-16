Name:           perl-IO-Tty
Version:        1.16
Release:        1
Summary:        A interface to pseudo tty's for perl
License:        (GPL+ or Artistic) and BSD
URL:            https://metacpan.org/release/IO-Tty
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Tty-%{version}.tar.gz
BuildRequires:  coreutils findutils make perl-interpreter perl-devel perl-generators
BuildRequires:  perl(Config) perl(Cwd) perl(Exporter) perl(ExtUtils::MakeMaker)
BuildRequires:  gcc perl(Carp) perl(DynaLoader) perl(IO::File) perl(IO::Handle) perl(POSIX)
BuildRequires:  perl(strict) perl(vars) perl(Test::More) perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
Supply an interface to pseudo tty's with IO::Tty and IO::Pty.

%package help
Summary:        Help documents for perl-IO-Tty package

%description help
Help documents for perl-IO-Tty package.

%prep
%autosetup -n IO-Tty-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/

%files help
%{_mandir}/man3/{IO::Pty.3*,IO::Tty.3*,IO::Tty::Constant.3*}

%changelog
* Tue Jun 14 2022 SimpleUpdate Robot <tc@openeuler.org> - 1.16-1
- Upgrade to version 1.16

* Wed Jun 02 2021 zhaoyao<zhaoyao32@huawei.com> - 1.12-15
- fixs faileds: /bin/sh: gcc: command not found.

* Wed Feb 19 2020 wutao <wutao61@huawei.com> - 1.12-14
- Package init
