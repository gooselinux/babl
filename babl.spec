Summary:	A dynamic, any to any, pixel format conversion library
Name:		babl
Version:	0.1.2
Release:	4%{?dist}
# The gggl codes contained in this package are under the GPL, with exceptions allowing their use under libraries covered under the LGPL
License:	LGPLv3+ and GPLv3+
Group:		System Environment/Libraries
URL:		http://www.gegl.org/babl/
Source0:	ftp://ftp.gtk.org/pub/babl/0.1/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	librsvg2 w3m

%global develdocdir %{_docdir}/%{name}-devel-%{version}/html

%description
Babl is a dynamic, any to any, pixel format conversion library. It
provides conversions between the myriad of buffer types images can be
stored in. Babl doesn't only help with existing pixel formats, but also
facilitates creation of new and uncommon ones.

%package devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
# Split off devel docs from 0.1.2-2 on
Obsoletes:	%{name}-devel < 0.1.2-2%{?dist}
Conflicts:	%{name}-devel < 0.1.2-2%{?dist}

%description devel
This package contains the libraries and header files needed for
developing with %{name}.

%package devel-docs
Summary:	Documentation for developing programs that will use %{name}
Group:		Documentation
BuildArch:	noarch
Requires:	%{name}-devel = %{version}-%{release}
# Split off devel docs from 0.1.2-2 on
Obsoletes:	%{name}-devel < 0.1.2-2%{?dist}
Conflicts:	%{name}-devel < 0.1.2-2%{?dist}

%description devel-docs
This package contains documentation needed for developing with %{name}.

%prep
%setup -q

%build
# use PIC/PIE because babl is likely to deal with data coming from untrusted
# sources
CFLAGS="-fPIC %optflags -fno-strict-aliasing"
LDFLAGS="-pie"
%configure --disable-static

make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install INSTALL='install -p'

mkdir -p "%{buildroot}/%{develdocdir}"
cp -pr docs/graphics docs/*.html docs/babl.css "%{buildroot}/%{develdocdir}"
rm -rf "%{buildroot}/%{develdocdir}"/graphics/Makefile*

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%check
make check

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING README NEWS
%{_libdir}/*.so.*
%{_libdir}/babl-0.1/

%files devel
%defattr(-, root, root, -)
%{_includedir}/babl-0.1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files devel-docs
%defattr(-, root, root, -)
%doc %{develdocdir}

%changelog
* Wed Jun 23 2010 Nils Philippsen <nils@redhat.com> - 0.1.2-4
- use PIC/PIE because babl is likely to deal with data coming from untrusted
  sources

* Wed Jun 23 2010 Nils Philippsen <nils@redhat.com> - 0.1.2-3
- build with -fno-strict-aliasing

* Mon Jun 14 2010 Nils Philippsen <nils@redhat.com> - 0.1.2-2
- split off devel-docs subpackage to make package multi-lib compliant (#477807)
- let devel package require correct arch of base package

* Thu Jan 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.1.2-1
- Update to 0.1.2

* Fri Dec 18 2009 Deji Akingunola <dakingun@gmail.com> - 0.1.0-5
- Remove the *.la files

* Thu Aug 13 2009 Nils Philippsen <nils@redhat.com>
- explain patch status

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Nils Philippsen <nils@redhat.com> - 0.1.0-3
- revert using "--disable-gtk-doc" as this doesn't work with babl (#477807)

* Thu Jul 02 2009 Nils Philippsen <nils@redhat.com>
- use "--disable-gtk-doc" to avoid rebuilding documentation (#477807)
- fix source URL

* Thu Jun 25 2009 Nils Philippsen <nils@redhat.com> - 0.1.0-2
- fix timestamps of built documentation for multilib (#477807)

* Fri May 22 2009 Deji Akingunola <dakingun@gmail.com> - 0.1.0-1
- Update to latest release (0.1.0)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep  2 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.0.22-2
- Include /usr/include/babl-0.0 directory

* Thu Jul 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.0.22-1
- Update to latest release

* Thu Feb 28 2008 Deji Akingunola <dakingun@gmail.com> - 0.0.20-1
- New release

* Thu Jan 17 2008 Deji Akingunola <dakingun@gmail.com> - 0.0.18-2
- Apply patch to fix extensions loading on 64bit systems

* Thu Jan 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.0.18-1
- Update to 0.0.18

* Mon Nov 26 2007 Deji Akingunola <dakingun@gmail.com> - 0.0.16-1
- Update to 0.0.16 release 
- License change from GPLv2+ to GPLv3+

* Mon Oct 22 2007 Deji Akingunola <dakingun@gmail.com> - 0.0.15-0.5.20071011svn
- Update the License field 

* Fri Oct 12 2007 Deji Akingunola <dakingun@gmail.com> - 0.0.15-0.4.20071011svn
- Package the extension libraries in the main package
- Run 'make check' 

* Fri Oct 12 2007 Deji Akingunola <dakingun@gmail.com> - 0.0.15-0.3.20071011svn
- Ensure timestamps are kept during install

* Fri Oct 12 2007 Deji Akingunola <dakingun@gmail.com> - 0.0.15-0.2.20071011svn
- Remove the use of inexistent source url (Package reviews)
- Package the html docs

* Thu Oct 11 2007 Deji Akingunola <dakingun@gmail.com> - 0.0.15-0.1.20071011svn
- Initial packaging for Fedora
