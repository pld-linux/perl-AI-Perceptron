%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Perceptron
Summary:	AI::Perceptron - An implementation of a Perceptron
Summary(pl):	AI::Perceptron - implementacja perceptronu
Name:		perl-%{pdir}-%{pnam}
Version:	0.01
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is meant to be an introduction to the internal operations
of Neural Networks.  It lets the user create a single node in a neural
net based on the Perceptron model.

For similar functionality, see Statistics::LTU.

%description -l pl
Ten modu³ ma byæ wprowadzeniem do wewnêtrznych operacji sieci
neuronowych. Pozwala u¿ytkownikowi stworzyæ pojedynczy wêze³ w sieci
neuronowej bazuj±cej na modelu perceptronu.

Podobn± funkcjonalno¶æ mo¿na znale¼æ w module Statistics::LTU.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
