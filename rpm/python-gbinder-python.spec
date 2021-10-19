%define _proj_name gbinder-python
%define modname %{_proj_name}
%define fedname %{modname}
%define internal_name gbinder

Name: python-%{modname}
Version: 1.0.0+git2
Release: 1
License: GPLv3
Summary: Python bindings for libgbinder

BuildRequires: gcc
BuildRequires: libgbinder-devel libglibutil-devel pkgconfig

Source: %{name}-%{version}.tar.gz

%description
Cython extension module for gbinder

%package -n python3-%{fedname}
Summary: %{summary}
BuildRequires: python3-devel python3-setuptools
BuildRequires: python3-cython
%{?python_provide:%python_provide python3-%{fedname}}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{fedname} 
%{description}

Python 3 version.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%{python3} ./setup.py build_ext --inplace --cython
env WITH_CYTHON=true %{py3_build}

%install
%{py3_install}

%files -n python3-%{fedname}
%{python3_sitearch}/%{internal_name}*.so
%{python3_sitearch}/%{internal_name}*.egg-info
