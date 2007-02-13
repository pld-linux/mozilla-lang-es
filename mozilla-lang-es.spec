Summary:	Spanish resources for Mozilla
Summary(es.UTF-8):	Recursos españoles para Mozilla
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Mozilli
Name:		mozilla-lang-es
Version:	1.7.12
%define		mozversion	1.7.13
%define		shortversion	1.712
# use "a", "b", or undefined
#%%define	bver	b
# use "Alpha", "Beta" or %{nil}
%define	fver	%{nil}
Release:	%{?bver:0.%{bver}.}2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/mozilla/l10n/lang/moz%{shortversion}/mozilla-%{version}.es-ES.langpack.xpi
# Source0-md5:	2bea0532bf5268fa550e420f69383520
Source1:	http://ftp.mozilla.org/pub/mozilla.org/mozilla/l10n/lang/moz%{shortversion}/mozilla-%{version}.es-ES.regpack.xpi
# Source1-md5:	90278f390bcc455bf3293da47acc7257
Source2:	%{name}-installed-chrome.txt
URL:		http://nave.hispalinux.es/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 5:%{mozversion}%{?bver}
Requires(post,postun):	mozilla <= 5:%{mozversion}
Requires(post,postun):	textutils
Requires:	mozilla >= 5:%{mozversion}%{?bver}
Requires:	mozilla <= 5:%{mozversion}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# %{_libdir}/mozilla/chrome is symlink pointing to the following
%define	_chromedir	%{_datadir}/mozilla/chrome

%description
Spanish resources for Mozilla.

%description -l es.UTF-8
Recursos españoles para Mozilla.

%description -l pl.UTF-8
Hiszpańskie pliki językowe dla Mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_datadir}/mozilla/searchplugins}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_datadir}
unzip -o %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}
mv -f $RPM_BUILD_ROOT%{_datadir}/bin/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_datadir}/bin/searchplugins/* \
	$RPM_BUILD_ROOT%{_datadir}/mozilla/searchplugins
# entries already in mozilla
rm -f $RPM_BUILD_ROOT%{_datadir}/mozilla/searchplugins/{Net,bug,dmoz,goo,jee,lxr,moz}*

install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun
umask 022
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/es-ES.jar
%{_chromedir}/es-unix.jar
%{_chromedir}/ES.jar
%{_chromedir}/%{name}-installed-chrome.txt
%{_datadir}/mozilla/searchplugins/*
