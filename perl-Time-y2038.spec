%define upstream_name    Time-y2038
%define upstream_version 20100403

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Use Time::y2038's gmtime and localtime everywhere
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(JSON)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Module::Build)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
On many computers, Perl's time functions will not work past the year 2038.
This is a design fault in the underlying C libraries Perl uses. Time::y2038
provides replacements for those functions which will work accurately +/1
142 million years.

This only imports the functions into your namespace. To replace it
everywhere, see the Time::y2038::Everywhere manpage.

Replaces the following functions:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 20100403.0.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Jul 22 2011 Götz Waschk <waschk@mandriva.org> 20100403.0.0-3
+ Revision: 691051
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 20100403.0.0-2mdv2011.0
+ Revision: 556186
- rebuild for perl 5.12

* Sat May 15 2010 Guillaume Rousse <guillomovitch@mandriva.org> 20100403.0.0-1mdv2010.1
+ Revision: 544857
- import perl-Time-y2038


* Sat May 15 2010 cpan2dist 20100403-1mdv
- initial mdv release, generated with cpan2dist
