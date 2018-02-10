%global pypi_name oslo.reports
%global pkg_name oslo-reports

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
The Oslo project intends to produce a python library containing \
infrastructure code shared by OpenStack projects. The APIs provided \
by the project should be high quality, stable, consistent and generally \
useful. \
\
OpenStack library for creating Guru Meditation Reports and other reports.

%global common_desc2 \
Test module for OpenStack common reports library

Name:           python-%{pkg_name}
Version:        1.26.0
Release:        1%{?dist}
Summary:        Openstack common reports library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python2-%{pkg_name}
Summary:   OpenStack common reports library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
# test requirements
BuildRequires:  python2-hacking
BuildRequires:  python2-oslotest
BuildRequires:  python2-oslo-config
BuildRequires:  python2-eventlet
BuildRequires:  python2-greenlet
BuildRequires:  python2-oslo-utils
BuildRequires:  python2-oslo-serialization
BuildRequires:  python2-psutil

Requires:       python2-jinja2
Requires:       python2-oslo-i18n >= 3.15.3
Requires:       python2-oslo-serialization >= 2.18.0
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-psutil
Requires:       python2-six >= 1.10.0

%description -n python2-%{pkg_name}
%{common_desc}

%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common reports library

BuildRequires: python2-sphinx
BuildRequires: python2-openstackdocstheme


%description -n python-%{pkg_name}-doc
Documentation for the oslo.reports library.

%package -n python2-%{pkg_name}-tests
Summary:  Test module for OpenStack common reports library
%{?python_provide:%python_provide python2-%{pkg_name}-tests}

Requires:  python2-%{pkg_name} = %{version}-%{release}
Requires:  python2-hacking
Requires:  python2-oslotest
Requires:  python2-oslo-config
Requires:  python2-eventlet
Requires:  python2-greenlet

%description -n python2-%{pkg_name}-tests
%{common_desc2}

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
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-psutil

Requires:       python3-jinja2
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-psutil
Requires:       python3-six >= 1.10.0

%description -n python3-%{pkg_name}
%{common_desc}
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

%description -n python3-%{pkg_name}-tests
%{common_desc2}
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Let RPM handle the dependencies
%py_req_cleanup

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

%files -n python2-%{pkg_name}-tests
%{python2_sitelib}/oslo_reports/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_reports/tests
%endif

%changelog
* Sat Feb 10 2018 RDO <dev@lists.rdoproject.org> 1.26.0-1
- Update to 1.26.0

