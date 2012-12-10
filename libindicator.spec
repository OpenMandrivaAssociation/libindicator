%define	api	3
%define	major	7
%define libname	%mklibname indicator %{major}
%define devname	%mklibname indicator -d

%define libname3	%mklibname indicator %{api} %{major}
%define devname3	%mklibname indicator %{api} -d
 
Summary:	Panel indicator applet libraries
Name:		libindicator
Version:	0.5.0
Release:	2
License:	GPLv3
Url:		https://launchpad.net/libindicator
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
 
%description
Panel indicator applet library
This library contains information to build indicators to go into the indicator
applet.
 
%package -n %{libname}
Summary:	Panel indicator applet - shared library files - gtk+2
Group:		System/Libraries
 
%description -n %{libname}
This package contains the shared library files - gtk+2.
 
%package -n %{devname}
Summary:	Panel indicator applet - library development files - gtk+2
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
 
%description -n %{devname}
This package contains files that are needed to build applications gtk+2.
 
%package -n %{libname3}
Summary:	Panel indicator applet - shared library files - gtk+3
Group:		System/Libraries
Conflicts:	%{name}-tools < 0.5.0-2
 
%description -n %{libname3}
This package contains the shared library files - gtk+3.
 
%package -n %{devname3}
Summary:	Panel indicator applet - library development files - gtk+3
Group:		Development/C
Requires:	%{libname3} = %{version}-%{release}
Obsoletes:	%{name}-tools < 0.5.0-2
 
%description -n %{devname3}
This package contains files that are needed to build applications - gtk+3.
 
%prep
%setup -q

mkdir ../gtk3
cp -a . ../gtk3/
mv ../gtk3 .
 
%build
%configure2_5x \
	--disable-static \
	--with-gtk=2

%make

pushd gtk3
%configure2_5x \
	--disable-static \
	--with-gtk=3

%make
popd

%install
%makeinstall_std
%makeinstall_std -C gtk3

%files -n %{libname}
%{_libexecdir}/indicator-loader
%{_libdir}/libindicator.so.%{major}* 
 
%files -n %{libname3}
%{_libexecdir}/indicator-loader%{api}
%{_libdir}/libindicator%{api}.so.%{major}* 
 
%files -n %{devname}
%dir %{_datadir}/%{name}
%{_includedir}/libindicator-0.4/
%{_libdir}/pkgconfig/indicator-0.4.pc
%{_libdir}/libindicator.so

%files -n %{devname3}
%doc ChangeLog AUTHORS COPYING
%{_includedir}/libindicator%{api}-0.4/
%{_datadir}/%{name}/80indicator-debugging
%{_libdir}/pkgconfig/indicator%{api}-0.4.pc
%{_libdir}/libindicator%{api}.so
%{_libdir}/libdummy-indicator-*.so



%changelog
* Wed Jun 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.5.0-2
+ Revision: 802997
- rebuild building both gtk3 and gtk2 libs
- moved loaders to lib pkgs
- moved testing libexec bins to devel
- obsoleted tools pkg

* Fri May 18 2012 Crispin Boylan <crisb@mandriva.org> 0.5.0-1
+ Revision: 799510
- Update major to 7
- New release

* Tue Nov 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.4.1-1
+ Revision: 708184
- fixed groups
- imported package libindicator

