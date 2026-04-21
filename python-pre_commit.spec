%define module pre_commit

Name:		python-pre_commit
Version:	4.6.0
Release:	1
Summary:	A framework for managing and maintaining multi-language pre-commit hooks
Group:		Development/Python
License:	MIT
URL:		https://github.com/pre-commit/pre-commit
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)

%description
A framework for managing and maintaining multi-language pre-commit hooks.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.md
%license LICENSE
%{_bindir}/pre-commit
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.egg-info
