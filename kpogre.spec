# $Revision: 1.9 $Date: 2007-07-08 10:02:30 $
Summary:	PostgreSQL grafical frontend for KDE
Summary(pl.UTF-8):	Graficzny frontend do PostgreSQL-a dla KDE 
Name:		kpogre
Version:	1.5.2
Release:	1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://dl.sourceforge.net/kpogre/%{name}-%{version}.tar.gz
# Source0-md5:	a5fe7384608e7322ecf19593357f0608
URL:		http://kpogre.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	libpqxx-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPoGre is grafical client for PostgreSQL Database for KDE. It uses
libpqxx library.

%description -l pl.UTF-8
KPoGre jest graficznym klientem bazy PostgreSQL dla KDE. Używa
biblioteki libpqxx.

%prep
%setup -q

%build
%configure \
	--disable-debug \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
echo 'Categories=Qt;KDE;Office;Database;' >> kpogre/kpogre.desktop

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/kpogre.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/kpogre.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kpogre
%{_desktopdir}/kde/kpogre.desktop
%{_iconsdir}/hicolor/*/*/kpogre.png
