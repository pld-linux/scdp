Summary:	send CDP packets
Summary(pl):	wysy³a pakiety CDP
Name:		scdp
Version:	1.0b
Release:	1
License:	GPL
Group:		Networking
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7eafaf5a422e37d04715613993ed5d95
Patch0:		%{name}-automake.patch
URL:		http://www.sf.net/projects/scdp/
BuildRequires:	libnet-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends CDP (Cisco Discovery Protocol) packets out on selected
interfaces and tells the connected switch where the host is connected.

%description -l pl
Ten program wysy³a pakiety CDP (Cisco Discovery Protocol) na wskazanych
interfejsach sieciowych i informuje przy³±czone switche o miejscu
pod³±czenia maszyny.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
