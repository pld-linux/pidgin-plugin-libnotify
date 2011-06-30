#
# TODO: BRs
#
%define		short_name	pidgin-libnotify
Summary:	libnotify interface to pidgin
Name:		pidgin-plugin-libnotify
Version:	0.14
Release:	0.1
License:	GPL v3+
Group:		Applications
Source0:	http://downloads.sourceforge.net/gaim-libnotify/%{short_name}-%{version}.tar.gz
# Source0-md5:	bfb5368b69c02d429b2b17c00a6673c0
URL:		http://gaim-libnotify.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin adds a libnotify interface to pidgin, enabling popups much
like guifications. It has some configuration options, to show popups
when a buddy signs on, on new messages and on new conversations only.

%prep
%setup -q -n %{short_name}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/purple-2/pidgin-libnotify.so
