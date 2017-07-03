%global pypi_name oslo.reports
%global pkg_name oslo-reports

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pkg_name}
Version:        XXX
Release:        XXX
Summary:        Openstack common reports library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz

BuildArch:      noarch

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.

%package -n python2-%{pkg_name}
Summary:   OpenStack common reports library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  git
# test requirements
BuildRequires:  python-hacking
BuildRequires:  python-oslotest
BuildRequires:  python-oslo-config
BuildRequires:  python-eventlet
BuildRequires:  python-greenlet
BuildRequires:  python-coverage
BuildRequires:  python-oslo-utils
BuildRequires:  python-oslo-serialization
BuildRequires:  python-psutil

Requires:       python-jinja2
Requires:       python-babel
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-oslo-serialization >= 1.4.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-psutil
Requires:       python-six >= 1.9.0

%description -n python2-%{pkg_name}
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.

%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common reports library

BuildRequires: python-sphinx
BuildRequires: python-openstackdocstheme


%description -n python-%{pkg_name}-doc
Documentation for the oslo.reports library.

%package -n python-%{pkg_name}-tests
Summary:  Test module for OpenStack common reports library

Requires:  python-%{pkg_name} = %{version}-%{release}
Requires:  python-hacking
Requires:  python-oslotest
Requires:  python-oslo-config
Requires:  python-eventlet
Requires:  python-greenlet
Requires:  python-coverage

%description -n python-%{pkg_name}-tests
Test module for OpenStack common reports library

%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:        OpenStack oslo.reports library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# test requirements
BuildRequires:  python3-hacking
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-config
BuildRequires:  python3-eventlet
BuildRequires:  python3-greenlet
BuildRequires:  python3-coverage
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-psutil

Requires:       python3-jinja2
Requires:       python3-babel
Requires:       python3-oslo-i18n >= 1.5.0
Requires:       python3-oslo-serialization >= 1.4.0
Requires:       python3-oslo-utils >= 2.0.0
Requires:       python3-psutil
Requires:       python3-six >= 1.9.0

%description -n python3-%{pkg_name}
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.
%endif

%if 0%{?with_python3}
%package -n python3-%{pkg_name}-tests
Summary:  Test module for OpenStack common reports library

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-hacking
Requires:  python3-oslotest
Requires:  python3-oslo-config
Requires:  python3-eventlet
Requires:  python3-greenlet
Requires:  python3-coverage

%description -n python3-%{pkg_name}-tests
Test module for OpenStack common reports library
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -f requirements.txt

%build
%py2_build

# generate html docs
%{__python2} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif

%files -n python2-%{pkg_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_reports
%{python2_sitelib}/*.egg-info
%exclude %{python2_sitelib}/oslo_reports/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_reports
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_reports/tests
%endif

%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html

%files -n python-%{pkg_name}-tests
%{python2_sitelib}/oslo_reports/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_reports/tests
%endif

%changelog
