%include	/usr/lib/rpm/macros.perl
Summary:	Autodia - producing an XML documents from source code or data
Summary(pl):	Autodia - tworzenie dokumentów XML z kodu ¼ród³owego lub danych
Name:		Autodia
Version:	1.3
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://droogs.org/autodia/download/%{name}-%{version}.tar.gz
# Source0-md5:	4f3cf8c2aa81df384d961027b67a2462
URL:		http://droogs.org/autodia/
BuildRequires:	rpm-perlprov
#Requires:	dia
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoDia is a modular application that parses source code or data (if a
handler is available) and produces an XML document in Dia format.
Handlers for Perl, C++, Java and PHP are available. (This used to be
called AutoDIAL.)

%description -l pl
AutoDia to modularna aplikacja analizuj±ca kod ¼ród³owy lub dane
(je¶li dostêpna jest odpowiednia procedura obs³ugi) i generuj±ca
dokument XML w formacie Dia. Dostêpne s± procedury obs³ugi dla Perla,
C++, Javy i PHP. Ten program poprzednio nazywa³ siê AutoDIAL.

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Autodia.pm
%{perl_vendorlib}/Autodia
%{_mandir}/man3/*
