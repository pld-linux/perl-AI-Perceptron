#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	AI
%define		pnam	Perceptron
Summary:	AI::Perceptron - an implementation of a Perceptron
Summary(pl):	AI::Perceptron - implementacja perceptronu
Name:		perl-AI-Perceptron
Version:	1.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	17c4f512664a1981ed8894d85b8eefa4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build >= 0.20
%if %{with tests}
BuildRequires:	perl-accessors
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is meant to be an introduction to the internal operations
of Neural Networks. It lets the user create a single node in a neural
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
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

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
