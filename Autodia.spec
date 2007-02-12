%include	/usr/lib/rpm/macros.perl
Summary:	Autodia - producing an XML documents from source code or data
Summary(pl.UTF-8):   Autodia - tworzenie dokumentów XML z kodu źródłowego lub danych
Name:		Autodia
Version:	2.02
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://droogs.org/autodia/download/%{name}-%{version}.tar.gz
# Source0-md5:	4c00d58dd9bbbfa386e4d03a82b7a2f8
URL:		http://droogs.org/autodia/
BuildRequires:	perl-Template-Toolkit
BuildRequires:	rpm-perlprov
Requires:	perl-Inline
Requires:	perl-Inline-Java
Requires:	perl-XML-Simple
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoDia is a modular application that parses source code or data (if a
handler is available) and produces an XML document in Dia format.
Handlers for Perl, C++, Java and PHP are available. (This used to be
called AutoDIAL.)

%description -l pl.UTF-8
AutoDia to modularna aplikacja analizująca kod źródłowy lub dane
(jeśli dostępna jest odpowiednia procedura obsługi) i generująca
dokument XML w formacie Dia. Dostępne są procedury obsługi dla Perla,
C++, Javy i PHP. Ten program poprzednio nazywał się AutoDIAL.

%prep
%setup -q

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
