# TODO:
# - prepare special script that runs from cron and takes arguments from
#   sysconfig file
Summary:	Send CDP packets
Summary(pl):	Wysy�anie pakiet�w CDP
Name:		scdp
Version:	1.0b
Release:	2
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/scdp/%{name}-%{version}.tar.gz
# Source0-md5:	7eafaf5a422e37d04715613993ed5d95
Source1:	%{name}.cron
Patch0:		%{name}-automake.patch
Patch1:		%{name}-libnet1.patch
URL:		http://www.sf.net/projects/scdp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnet1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends CDP (Cisco Discovery Protocol) packets out on
selected interfaces and tells the connected switch where the host is
connected.

%description -l pl
Ten program wysy�a pakiety CDP (Cisco Discovery Protocol) na
wskazanych interfejsach sieciowych i informuje przy��czone switche o
miejscu pod��czenia maszyny.

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
install -d $RPM_BUILD_ROOT/etc/cron.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.d/%{name}
%attr(755,root,root) %{_bindir}/*
