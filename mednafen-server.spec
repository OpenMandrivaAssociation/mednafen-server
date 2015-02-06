Name:			mednafen-server
Version:		0.5.0
Release:		2

Summary:	Mednafen Network Play Server
License:	GPLv2+
URL:		http://mednafen.sourceforge.net/
Group:		Emulators
Source0:	http://downloads.sourceforge.net/mednafen/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This CLI-driven server aims at providing multiplayer gaming over a LAN 
for mednafen emulator.

Look at the provided documentation for an example config file and usage.

%prep
%setup -q -n %{name}
#find ./src -type f -exec chmod 644 '{}' +
#find ./src -type d -exec chmod 755 '{}' +

%build
#autoreconf -i
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc ChangeLog README TODO run.sh standard.conf
%attr(0755,root,root) %{_bindir}/%{name}

%clean
rm -rf %{buildroot}



%changelog
* Thu Jul 19 2012 Zombie Ryushu <ryushu@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 810305
- Upgrade to 0.5.0

* Sat Jul 07 2012 Zombie Ryushu <ryushu@mandriva.org> 0.4.2-1
+ Revision: 808452
- Upgrade 0.4.2

* Sat Jul 30 2011 Andrey Bondrov <abondrov@mandriva.org> 0.4.1-2
+ Revision: 692340
- imported package mednafen-server


* Thu Jul 21 2010 Andrey Bondrov <bondrov@math.dvgu.ru> 0.4.1-1mdv2011.0
- Import from PLF
- Remove PLF reference

* Sat Jun  5 2010 Guillaume Bedot <littletux@zarb.org> 0.4.1-1plf2010.1
- First package for PLF
