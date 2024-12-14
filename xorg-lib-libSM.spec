Summary:	X Session Management library
Summary(pl.UTF-8):	Biblioteka zarządzania sesją X
Name:		xorg-lib-libSM
Version:	1.2.5
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.xz
# Source0-md5:	ef6167bfcb675f65a790e0f517a87455
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libICE-devel >= 1.1.0
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRequires:	xz
Requires:	xorg-lib-libICE >= 1.1.0
Obsoletes:	libSM < 6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Session Management library.

%description -l pl.UTF-8
Biblioteka zarządzania sesją X.

%package devel
Summary:	Header files for libSM library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libSM
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libuuid-devel
Requires:	xorg-lib-libICE-devel >= 1.1.0
Obsoletes:	libSM-devel < 6.1

%description devel
X Session Management library.

This package contains the header files needed to develop programs that
use libSM.

%description devel -l pl.UTF-8
Biblioteka zarządzania sesją X.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libSM.

%package static
Summary:	Static libSM library
Summary(pl.UTF-8):	Biblioteka statyczna libSM
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libSM-static < 6.1

%description static
X Session Management library.

This package contains the static libSM library.

%description static -l pl.UTF-8
Biblioteka zarządzania sesją X.

Pakiet zawiera statyczą bibliotekę libSM.

%prep
%setup -q -n libSM-%{version}

%build
%{__libtoolize}
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libSM.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSM.so.6

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_libdir}/libSM.so
%{_libdir}/libSM.la
%dir %{_includedir}/X11/SM
%{_includedir}/X11/SM/*.h
%{_pkgconfigdir}/sm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSM.a
