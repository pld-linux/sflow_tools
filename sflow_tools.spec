Summary:	command line utilities analyzing sFlow data
Summary(pl):	Pokazuje pakiety przechodz�ce przez interfejsy sieciowe
Name:		sflow_tools
Version:	1.3
Release:	1
License:	custom
Group:		Applications/Networking
Source0:	http://www.inmon.com/%{name}-%{version}.tar.gz
URL:		http://www.inmon.com/sflowTools.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The core component of the sFlow toolkit is the sflowtool command line
utility. sflowtool interfaces to utilities such as tcpdump, ntop and
Snort for detailed packet tracing and analysis, NetFlow compatible
collectors for IP flow accounting, and provides text based output that
can be used in scripts to provide customized analysis and reporting
and for integrating with other tools such as MRTG or rrdtool.

%description -l pl
G��wnym komponentem zbioru narz�dzi sFlow jest program sflowtool.
sflowtool jest interfejsem pomi�dzy programami takimi jak tcpdump,
ntop oraz Snort s�u��cym dok�adnemu �ledzeniu pakiet�w oraz analizie,
narz�dziami kompatybilnymi z NetFlow do zliczania przep�ywu ruchu IP
oraz dostarcza tekstowe informacje wyj�ciowe, kt�re mog� by� u�ywane w
skryptach do tworzenia analiz oraz raport�w czy integracji z innymi
programami jak MRTG lub rrdtool.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
