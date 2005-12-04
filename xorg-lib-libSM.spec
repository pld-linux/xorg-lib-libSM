Summary:	Session Management library
Summary(pl):	Biblioteka zarz±dzania sesj±
Name:		xorg-lib-libSM
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/lib/libSM-%{version}.tar.bz2
# Source0-md5:	4b26938eac1763e4674ad8786025af65
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libSM
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Session Management library.

%description -l pl
Biblioteka zarz±dzania sesj±.

%package devel
Summary:	Header files for libSM library
Summary(pl):	Pliki nag³ówkowe biblioteki libSM
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libICE-devel
Obsoletes:	libSM-devel

%description devel
Session Management library.

This package contains the header files needed to develop programs that
use libSM.

%description devel -l pl
Biblioteka zarz±dzania sesj±

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libSM.

%package static
Summary:	Static libSM library
Summary(pl):	Biblioteka statyczna libSM
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libSM-static

%description static
Session Management library.

This package contains the static libSM library.

%description static -l pl
Biblioteka zarz±dzania sesj±.

Pakiet zawiera statycz± bibliotekê libSM.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libSM.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSM.so
%{_libdir}/libSM.la
%dir %{_includedir}/X11/SM
%{_includedir}/X11/SM/*.h
%{_pkgconfigdir}/sm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSM.a
