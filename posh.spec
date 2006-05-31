Summary:	Policy-compliant Ordinary SHell
Name:		posh
Version:	0.5
Release:	0.3
License:	GPL v2+
Group:		Applications/Shells
Source0:	http://ftp.debian.org/debian/pool/main/p/posh/%{name}_%{version}.tar.gz
# Source0-md5:	56ca21ffb22ab80bcaecb88df5cff2e4
URL:		http://packages.debian.org/unstable/source/posh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir			/bin
%define		_shell			%{_bindir}/%{name}

%description
posh is a stripped-down version of pdksh that aims for compliance with
Debian's policy, and few extra features.

posh contains code from pdksh 5.2.14, which is "in the public domain."

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shells ]; then
	umask 022
	echo '%{_shell}' > /etc/shells
else
	grep -q '^%{_shell}$' /etc/shells || echo '%{_shell}' >> /etc/shells
fi

%preun
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^%(echo %{_shell} | sed -e 's,/,\\/,g')$/d' /etc/shells
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/posh
%{_mandir}/man1/posh.1*
