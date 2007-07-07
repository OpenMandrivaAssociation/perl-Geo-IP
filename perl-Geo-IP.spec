%define module 	Geo-IP
%define version 1.28
%define release %mkrel 1

Summary:	Look up country by IP Address
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  libgeoip-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
This module uses a file based database. This database simply contains 
IP blocks as keys, and countries as values. This database should be 
more complete and accurate than reverse DNS lookups.
This module can be used to automatically select the geographically 
closest mirror, to analyze your web server logs to determine the 
countries of your visiters, for credit card fraud detection, and for 
software export controls.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Geo
%{perl_vendorarch}/auto/Geo/
%{_mandir}/*/*

