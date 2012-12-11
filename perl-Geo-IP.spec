%define upstream_name 	 Geo-IP
%define upstream_version 1.39

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.390.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.390.0-1
+ Revision: 672847
- update to new version 1.39

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.380.0-2mdv2011.0
+ Revision: 555385
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.380.0-1mdv2010.0
+ Revision: 403196
- rebuild using %%perl_convert_version

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.38-1mdv2010.0
+ Revision: 377829
- update to new version 1.38

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.37-1mdv2009.1
+ Revision: 352912
- update to new version 1.37

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2009.1
+ Revision: 320431
- update to new version 1.36

* Mon Oct 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.35-1mdv2009.1
+ Revision: 295505
- update to new version 1.35

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.34-1mdv2009.0
+ Revision: 270508
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.31-2mdv2009.0
+ Revision: 268515
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.31-1mdv2009.0
+ Revision: 194854
- update to new version 1.31
- update to new version 1.31

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.30-2mdv2008.1
+ Revision: 152086
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2008.1
+ Revision: 121643
- update to new version 1.30

* Sat Jul 07 2007 Funda Wang <fwang@mandriva.org> 1.28-1mdv2008.0
+ Revision: 49309
- New version


* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdk
- New release 1.27
- CPAN url

* Thu Jul 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.26-1mdk
- 1.26

* Thu Feb 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.25-1mdk
- 1.25

* Thu Nov 18 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.23-1mdk
- New release 1.23
- Fix vendorarch dirs in spec; add tests

* Mon Sep 27 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.22-1mdk
- New release 1.22

* Mon Nov 10 2003 G�tz Waschk <waschk@linux-mandrake.com> 1.21-2mdk
- fix buildrequires

* Mon Sep 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.21-1mdk
- needed by w3perl

