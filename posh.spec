Summary:	Policy-compliant Ordinary SHell
Summary(pl.UTF-8):	Policy-compliant Ordinary SHell - zwykła powłoka zgodna z polityką Debiana
Name:		posh
Version:	0.10
Release:	1
License:	GPL v2+
Group:		Applications/Shells
Source0:	http://ftp.debian.org/debian/pool/main/p/posh/%{name}_%{version}.tar.gz
# Source0-md5:	eea6d2bf89fe4da2a6d3636cc8caa0cf
URL:		http://packages.debian.org/unstable/source/posh
BuildRequires:	rpmbuild(macros) >= 1.462
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir			/bin
%define		_shell			%{_bindir}/%{name}

%description
posh is a stripped-down version of pdksh that aims for compliance with
Debian's policy, and few extra features.

posh contains code from pdksh 5.2.14, which is "in the public domain."

%description -l pl.UTF-8
posh to okrojona wersja pdksh, której celem jest zgodność z polityką
Debiana i kilka dodatkowych możliwości.

posh zawiera kod pdksh 5.2.14, będący własnością publiczną ("public
domain").

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

%post	-p <lua>
%lua_add_etc_shells %{_shell}

%preun	-p <lua>
if arg[2] == 0 then
	%lua_remove_etc_shells %{_shell}
end

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/posh
%{_mandir}/man1/posh.1*
