Name:           python3-postgresql
Version:        1.0.2
Release:        1%{?dist}
Summary:        Connect to PostgreSQL with Python 3

Group:          Applications/Databases
License:        BSD
URL:            http://python.projects.postgresql.org/
Source0:        http://python.projects.postgresql.org/files/py-postgresql-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python3-devel

%description
py-postgresql is a Python 3 package providing modules to work with PostgreSQL.
This includes a high-level driver, and many other tools that support a
developer working with PostgreSQL databases.

%prep
%setup -q -n py-postgresql-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README
%{python3_sitearch}/*


%changelog
* Mon Aug 29 2011 David Malcolm <dmalcolm@redhat.com> - 1.0.2-1
- 1.0.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-4
- rebuild for newer python3

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.0.0-3
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Apr  2 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial package

