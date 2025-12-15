%global pypi_name pre_commit

Name:           python-%{pypi_name}
Version:        4.5.0
Release:        1
Summary:        A framework for managing and maintaining multi-language pre-commit hooks
Group:          Development/Python
License:        MIT
URL:            https://github.com/pre-commit/pre-commit
Source0:        https://files.pythonhosted.org/packages/source/p/pre_commit/pre_commit-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)

%description
A framework for managing and maintaining multi-language pre-commit hooks.

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pre-commit
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}*.egg-info
