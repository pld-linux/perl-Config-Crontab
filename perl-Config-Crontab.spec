#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Crontab
Summary:	Config::Crontab - Read/Write Vixie compatible crontab(5) files
Summary(pl.UTF-8):	Config::Crontab - odczyt/zapis plików kompatybilnych z crontab(5) dla Vixie-crona
Name:		perl-Config-Crontab
Version:	1.20
Release:	0.1
# below one is stated in readme, not perl itself
License:	Perl Artistic License
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aea282c91759472f6238dac8caa761e5
URL:		http://search.cpan.org/dist/Config-Crontab/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::Crontab provides an object-oriented interface to
Vixie-style crontab(5) files for Perl.

A Config::Crontab object allows you to manipulate an ordered set
of Event, Env, or Comment objects (also included with this
package).

In short, Config::Crontab reads and writes crontab(5) files (and
does a little pretty-printing too) using objects. The general idea is
that you create a Config::Crontab object and associate it with a
file (if unassociated, it will work over a pipe to crontab -l). From
there, you can add lines to your crontab object, change existing line
attributes, and write everything back to file.

%description -l pl.UTF-8
Config::Crontab udostępnia zorientowany obiektowo interfejs dla Perla
do plików crontab(5) w stylu Vixie-crona.

Obiekt Config::Crontab pozwala obrabiać uporządkowany zbiór obiektów
Event, Env i Comment (także zawartych w tym pakiecie).

W skrócie Config::Crontab odczytuje i zapisuje pliki crontab(5)
(zapisując je przy okazji w ładnej formie) przy użyciu obiektów.
Ogólna idea jest taka, że tworzy się obiekt Config::Crontab i wiąże go
z plikiem (jeśli nie jest związany, działa przez potok z crontab -l).
Od tego momentu można do obiektu crontab dodawać linie, zmieniać
atrybuty istniejących linii i zapisać wszystko z powrotem do pliku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Config/*.pm
#%{perl_vendorlib}/Config/Crontab
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
