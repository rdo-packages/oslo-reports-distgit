%global pypi_name oslo.reports

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-oslo-reports
Version:        XXX
Release:        XXX
Summary:        Openstack common reports library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        http://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-master.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx

Requires:       python-jinja2
Requires:       python-babel
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-oslo-serialization >= 1.4.0
Requires:       python-oslo-utils >= 1.6.0
Requires:       python-psutil
Requires:       python-six >= 1.9.0


%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.


%package doc
Summary:    Documentation for OpenStack common messaging library

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx >= 2.5.0


%description doc
Documentation for the oslo.messaging library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_reports
%{python2_sitelib}/
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files doc
%license LICENSE
%doc html

%changelog
