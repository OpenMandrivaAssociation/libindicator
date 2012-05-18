%define	major 7
%define libname %mklibname	indicator	%{major}
%define develname %mklibname	indicator -d
 
Name:           libindicator
Version:        0.5.0
Release:        1
License:        GPLv3
Summary:        Panel indicator applet libraries
Url:            https://launchpad.net/libindicator
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
 
%description
Panel indicator applet library
This library contains information to build indicators to go into the indicator
applet.
 
%package -n %{libname}
Summary:        Panel indicator applet - shared library files
Group:          System/Libraries
 
%description -n %{libname}
Panel indicator applet - shared library files.
This library contains information to build indicators to go into the indicator
applet.
 
This package contains the shared library files.
 
%package tools
Summary:        A debugger for indicators
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
 
%description tools
Panel indicator applet - tools
This library contains information to build indicators to go into the indicator
applet.
 
This package provides some tools for debugging and development purposes.
 
%package -n %{develname}
Summary:        Panel indicator applet - library development files
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
 
%description -n %{develname}
Panel indicator applet - library development files.
This library contains information to build indicators to go into the indicator
applet.
 
This package contains files that are needed to build applications.
 
%prep
%setup -q
 
%build
%configure2_5x \
  --disable-static
%make

%install
%makeinstall_std

# Remove libtool archives
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

 
%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/*.so.%{major}* 
 
%files tools
%defattr(-,root,root)
%{_libexecdir}/indicator-loader3
%{_libdir}/libdummy-indicator-*.so
 
%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog
%dir %{_datadir}/%{name}
%{_includedir}/libindicator3-0.4/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%exclude %{_libdir}/libdummy-indicator-*.so
%{_datadir}/%{name}/80indicator-debugging
