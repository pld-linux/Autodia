Summary:	Autodia
Name:		Autodia
Version:	1.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	%{name}-%{version}.tar.gz
URL:		http://droogs.org/autodia/
BuildRequires:	perl
#Requires:	dia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoDia is a modular application that parses source code or data (if a handler
is available) and produces an XML document in Dia format. Handlers for Perl,
C++, Java and PHP are available. (This used to be called AutoDIAL.) 


%prep
%setup -q -n %{name}-%{version}

%build
perl Makefile.PL
make
make test

%install
#make install
#rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files
%defattr(644,root,root,755)
%doc README
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/*
# FIXME:
/usr/lib/perl5
