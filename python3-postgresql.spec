Name:           python3-postgresql
Version:        1.0.0
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
* Fri Apr  2 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial package

