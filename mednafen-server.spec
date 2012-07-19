Name:			mednafen-server
Version:		0.5.0
Release:		%mkrel 1

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

