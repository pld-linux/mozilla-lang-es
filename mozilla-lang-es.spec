Summary:	Spanish resources for Mozilla
Summary(es):	Recursos españoles para Mozilla
Summary(pl):	Hiszpañskie pliki jêzykowe dla Mozilli
Name:		mozilla-lang-es
Version:	1.7.5
%define		shortversion	1.75
# use "a", "b", or undefined
#%%define	bver	b
# use "Alpha", "Beta" or %{nil}
%define	fver	%{nil}
Release:	%{?bver:0.%{bver}.}1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/mozilla/l10n/lang/moz%{shortversion}/mozilla-%{version}.es-ES.langpack.xpi
# Source0-md5:	b738e63cc25e9c1400a78598c0aa58b9
Source1:	http://ftp.mozilla.org/pub/mozilla.org/mozilla/l10n/lang/moz%{shortversion}/mozilla-%{version}.es-ES.regpack.xpi
# Source1-md5:	bb4f053a3ffe37325ba2fdbc73d7f63a
Source2:	%{name}-installed-chrome.txt
URL:		http://mozilla.dnsalias..org/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 5:%{version}%{?bver}
Requires(post,postun):	mozilla <= 5:%{version}
Requires(post,postun):	textutils
Requires:	mozilla >= 5:%{version}%{?bver}
Requires:	mozilla <= 5:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# %{_libdir}/mozilla/chrome is symlink pointing to the following
%define	_chromedir	%{_datadir}/mozilla/chrome

%description
Spanish resources for Mozilla.

%description -l es
Recursos españoles para Mozilla.

%description -l pl
Hiszpañskie pliki jêzykowe dla Mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_datadir}/mozilla/searchplugins}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
unzip -o %{SOURCE1} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/bin/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/bin/searchplugins/* \
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
#no additional plugins (for now)
#%{_datadir}/mozilla/searchplugins/*
