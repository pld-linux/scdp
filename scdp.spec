Summary:	Send CDP packets
Summary(pl.UTF-8):	Wysyłanie pakietów CDP
Name:		scdp
Version:	1.0b
Release:	6
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/scdp/%{name}-%{version}.tar.gz
# Source0-md5:	7eafaf5a422e37d04715613993ed5d95
Source1:	%{name}.cron
Source2:	%{name}.sysconfig
Source3:	%{name}.cron.sh
Patch0:		%{name}-automake.patch
Patch1:		%{name}-libnet1.patch
URL:		http://www.sourceforge.net/projects/scdp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnet1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends CDP (Cisco Discovery Protocol) packets out on
selected interfaces and tells the connected switch where the host is
connected.

%description -l pl.UTF-8
Ten program wysyła pakiety CDP (Cisco Discovery Protocol) na
wskazanych interfejsach sieciowych i informuje przyłączone switche o
miejscu podłączenia maszyny.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{cron.d,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}.cron

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(755,root,root) %{_bindir}/*
