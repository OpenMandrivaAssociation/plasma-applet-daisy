Summary:	A simple application launcher for Plasma
Name:		plasma-applet-daisy
Version:	0.0.4.26
Release:	2
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		http://cdlszm.org/
Source0:	http://cdlszm.org/downloads/%{name}-%{version}.tar.gz
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-workspace
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
    * Various backgrounds available

%files -f plasma_applet_daisy.lang
%doc README AUTHORS CHANGELOG COPYING INSTALL TODO
%{_kde_appsdir}/desktoptheme/default/widgets/
%{_kde_libdir}/kde4/plasma_applet_daisy.so
%{_kde_services}/plasma-applet-daisy.desktop

#---------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang plasma_applet_daisy

