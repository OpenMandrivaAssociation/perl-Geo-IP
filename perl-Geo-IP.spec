%define upstream_name Geo-IP
%define upstream_version 1.45

Summary:	Look up country by IP Address
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(geoip)
BuildRequires:	geoip

%description
This module uses a file based database. This database simply contains 
IP blocks as keys, and countries as values. This database should be 
more complete and accurate than reverse DNS lookups.
This module can be used to automatically select the geographically 
closest mirror, to analyze your web server logs to determine the 
countries of your visiters, for credit card fraud detection, and for 
software export controls.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes INSTALL META.json META.yml MYMETA.yml README example
%{perl_vendorarch}/Geo
%{perl_vendorarch}/auto/Geo
%{_mandir}/*/*
