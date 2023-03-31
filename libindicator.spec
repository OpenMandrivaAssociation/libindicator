%define api 3
%define major 7
%define libname %mklibname indicator %{major}
%define devname %mklibname indicator -d

%define libname3 %mklibname indicator %{api} %{major}
%define devname3 %mklibname indicator %{api} -d

%define _disable_rebuild_configure 1

Summary:	Panel indicator applet libraries
Name:		libindicator
Version:	16.10.0
Release:	2
License:	GPLv3+
Group:		System/Libraries
Url:		https://launchpad.net/libindicator
Source0:	https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/libindicator/%{version}+18.04.20180321.1-0ubuntu5/libindicator_%{version}+18.04.20180321.1.orig.tar.gz
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libido3-0.1)

%description
Panel indicator applet library.

This library contains information to build indicators to go into the indicator
applet.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Panel indicator applet - shared library files - gtk+2
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library files - gtk+2.

%files -n %{libname}
#{_libexecdir}/indicator-loader
%{_libdir}/libindicator.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Panel indicator applet - library development files - gtk+2
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains files that are needed to build applications gtk+2.

%files -n %{devname}
%dir %{_datadir}/%{name}
%{_includedir}/libindicator-0.4/
%{_libdir}/pkgconfig/indicator-0.4.pc
%{_libdir}/libindicator.so

#----------------------------------------------------------------------------

%package -n %{libname3}
Summary:	Panel indicator applet - shared library files - gtk+3
Group:		System/Libraries
Conflicts:	%{name}-tools < 0.5.0-2

%description -n %{libname3}
This package contains the shared library files - gtk+3.

%files -n %{libname3}
%{_libexecdir}/indicator-loader%{api}
%{_libdir}/libindicator%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname3}
Summary:	Panel indicator applet - library development files - gtk+3
Group:		Development/C
Requires:	%{libname3} = %{EVRD}
Obsoletes:	%{name}-tools < 0.5.0-2

%description -n %{devname3}
This package contains files that are needed to build applications - gtk+3.

%files -n %{devname3}
%doc ChangeLog AUTHORS COPYING
%{_includedir}/libindicator%{api}-0.4/
%{_datadir}/%{name}/80indicator-debugging
%{_libdir}/pkgconfig/indicator%{api}-0.4.pc
%{_libdir}/libindicator%{api}.so

#----------------------------------------------------------------------------

%prep
%setup -q -c

#sed -i 's/\$LIBM/ \$LIBM/' configure

mkdir ../gtk3
cp -a . ../gtk3/
mv ../gtk3 .

%build
%global optflags %{optflags} -Wno-error=deprecated-declarations -Wno-error=gnu-designator
autoreconf -vfi
%configure \
	--disable-static \
	--with-gtk=2 \
	--disable-tests

%make

pushd gtk3
autoreconf -vfi
%configure \
	--disable-static \
	--with-gtk=3 \
	--disable-tests

%make
popd

%install
%makeinstall_std
%makeinstall_std -C gtk3

