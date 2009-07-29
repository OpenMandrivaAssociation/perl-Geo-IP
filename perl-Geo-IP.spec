%define upstream_name 	 Geo-IP
%define upstream_version 1.38

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Look up country by IP Address
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:  libgeoip-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Geo
%{perl_vendorarch}/auto/Geo
%{_mandir}/*/*
