%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Perceptron
Summary:	AI::Perceptron - An implementation of a Perceptron
Summary(pl):	AI::Perceptron - implementacja perceptronu
Name:		perl-%{pdir}-%{pnam}
Version:	0.01
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e0be7c652e4b9931b94927fb602a6350
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is meant to be an introduction to the internal operations
of Neural Networks.  It lets the user create a single node in a neural
net based on the Perceptron model.

For similar functionality, see Statistics::LTU.

%description -l pl
Ten modu� ma by� wprowadzeniem do wewn�trznych operacji sieci
neuronowych. Pozwala u�ytkownikowi stworzy� pojedynczy w�ze� w sieci
neuronowej bazuj�cej na modelu perceptronu.

Podobn� funkcjonalno�� mo�na znale�� w module Statistics::LTU.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
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
%{perl_vendorlib}/%{pdir}/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
