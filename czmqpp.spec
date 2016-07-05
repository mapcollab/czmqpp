Name:           czmqpp
Version:        1.2.0
Release:        1
Summary:        C++ wrapper for czmq
Group:          Development/Libraries
License:        MPLv2.0
URL:            http://czmq.zeromq.org/
Source0:        %{name}-%{version}.tar.gz
Requires:       czmq
BuildRequires:  czmq-devel
BuildRequires:  autoconf automake libtool

%description
C++ wrapper for czmq. Aims to be minimal, simple and consistent.


%package devel
Summary:        Development files for the czmqpp package
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       czmq-devel
Requires:       pkgconfig

%description devel
This package contains files needed to develop applications using czmqpp.


%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/libczmq++.{a,la}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc AUTHORS NEWS LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datarootdir}/doc/libczmqpp/*


%changelog
* Tue Jul 05 2016 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com.pl> 1.2.0-1
- initial version
