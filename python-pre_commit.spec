%global pypi_name pre_commit

Name:           python-%{pypi_name}
Version:        2.19.0
Release:        1
Summary:        A framework for managing and maintaining multi-language pre-commit hooks
Group:          Development/Python
License:        MIT
URL:            https://github.com/pre-commit/pre-commit
Source0:        https://files.pythonhosted.org/packages/source/p/pre_commit/pre_commit-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A framework for managing and maintaining multi-language pre-commit hooks.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pre-commit
%{_bindir}/pre-commit-validate-config
%{_bindir}/pre-commit-validate-manifest
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
