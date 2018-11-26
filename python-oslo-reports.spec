# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global pypi_name oslo.reports
%global pkg_name oslo-reports

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
Version:        XXX
Release:        XXX
Summary:        Openstack common reports library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python%{pyver}-%{pkg_name}
Summary:   OpenStack common reports library
%{?python_provide:%python_provide python%{pyver}-%{pkg_name}}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
# test requirements
BuildRequires:  python%{pyver}-hacking
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-oslo-config
BuildRequires:  python%{pyver}-eventlet
BuildRequires:  python%{pyver}-greenlet
BuildRequires:  python%{pyver}-oslo-utils
BuildRequires:  python%{pyver}-oslo-serialization
BuildRequires:  python%{pyver}-psutil

Requires:       python%{pyver}-jinja2
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-serialization >= 2.18.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-psutil
Requires:       python%{pyver}-six >= 1.10.0

%description -n python%{pyver}-%{pkg_name}
%{common_desc}

%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common reports library

BuildRequires: python%{pyver}-sphinx
BuildRequires: python%{pyver}-openstackdocstheme


%description -n python-%{pkg_name}-doc
Documentation for the oslo.reports library.

%package -n python%{pyver}-%{pkg_name}-tests
Summary:  Test module for OpenStack common reports library
%{?python_provide:%python_provide python%{pyver}-%{pkg_name}-tests}

Requires:  python%{pyver}-%{pkg_name} = %{version}-%{release}
Requires:  python%{pyver}-hacking
Requires:  python%{pyver}-oslotest
Requires:  python%{pyver}-oslo-config
Requires:  python%{pyver}-eventlet
Requires:  python%{pyver}-greenlet

%description -n python%{pyver}-%{pkg_name}-tests
%{common_desc2}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Let RPM handle the dependencies
%py_req_cleanup

%build
%{pyver_build}

# generate html docs
%{pyver_bin} setup.py build_sphinx -b html
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{pyver_install}

%check
# FIXME(jpena): we can enable unit tests again after a new tag including
# https://review.openstack.org/588088 is released
%{pyver_bin} setup.py test || true

%files -n python%{pyver}-%{pkg_name}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/oslo_reports
%{pyver_sitelib}/*.egg-info
%exclude %{pyver_sitelib}/oslo_reports/tests

%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html

%files -n python%{pyver}-%{pkg_name}-tests
%{pyver_sitelib}/oslo_reports/tests

%changelog
