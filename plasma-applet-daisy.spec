%define name	plasma-applet-daisy
%define version	0.0.4.22
%define release	%mkrel 1
%define Summary	 "Daisy" is a simple application launcher for Plasma


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://daisyplasma.freehostia.com/downloads/%{name}-%{version}.tar.gz
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		http://daisyplasma.freehostia.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	plasma-devel
BuildRequires:	kdebase4-workspace-devel
Provides:	plasma-applet

%description
Daisy is a  free open-source widget for Plasma/KDE released under the
GNU General Public License version 3.
Main features:
    * Three types of roles: circular dock, media controller and linear
      dock;
    * Can dock in any screen position and be used in Horizontal or
      Vertical mode (linear dock role);
    * Configuration tools to access all configurable options;
    * Launchers can be edited with a simple right-click;
    * Hybrid launchers to launch applications and control running
      tasks;
    * Plugins to provide information and execute several tasks;
    * Various backgrounds available.

%files -f plasma_applet_daisy.lang
%defattr(-,root,root)
%doc README AUTHORS CHANGELOG COPYING INSTALL TODO
%_kde_libdir/kde4/plasma_applet_daisy.so
%_kde_services/plasma-applet-daisy.desktop
%{_datadir}/apps/desktoptheme/default/widgets/

#---------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang plasma_applet_daisy

%clean
%__rm -rf %{buildroot}
