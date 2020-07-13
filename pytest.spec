#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest
Version  : 5.4.3
Release  : 140
URL      : https://files.pythonhosted.org/packages/8f/c4/e4a645f8a3d6c6993cb3934ee593e705947dfafad4ca5148b9a0fde7359c/pytest-5.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/8f/c4/e4a645f8a3d6c6993cb3934ee593e705947dfafad4ca5148b9a0fde7359c/pytest-5.4.3.tar.gz
Summary  : pytest: simple powerful testing with Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pytest-bin = %{version}-%{release}
Requires: pytest-license = %{version}-%{release}
Requires: pytest-python = %{version}-%{release}
Requires: pytest-python3 = %{version}-%{release}
Requires: atomicwrites
Requires: attrs
Requires: importlib_metadata
Requires: more-itertools
Requires: mypy
Requires: packaging
Requires: pathlib2
Requires: pluggy
Requires: py
Requires: wcwidth
BuildRequires : argcomplete
BuildRequires : atomicwrites
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : execnet
BuildRequires : more-itertools
BuildRequires : mypy
BuildRequires : nose
BuildRequires : packaging
BuildRequires : pathlib2
BuildRequires : pexpect
BuildRequires : pluggy
BuildRequires : py
BuildRequires : pytest-xdist
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : unittest2
BuildRequires : wcwidth

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

%package bin
Summary: bin components for the pytest package.
Group: Binaries
Requires: pytest-license = %{version}-%{release}

%description bin
bin components for the pytest package.


%package license
Summary: license components for the pytest package.
Group: Default

%description license
license components for the pytest package.


%package python
Summary: python components for the pytest package.
Group: Default
Requires: pytest-python3 = %{version}-%{release}

%description python
python components for the pytest package.


%package python3
Summary: python3 components for the pytest package.
Group: Default
Requires: python3-core
Provides: pypi(pytest)
Requires: pypi(attrs)
Requires: pypi(more_itertools)
Requires: pypi(packaging)
Requires: pypi(pluggy)
Requires: pypi(py)
Requires: pypi(wcwidth)

%description python3
python3 components for the pytest package.


%prep
%setup -q -n pytest-5.4.3
cd %{_builddir}/pytest-5.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591289037
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest
cp %{_builddir}/pytest-5.4.3/LICENSE %{buildroot}/usr/share/package-licenses/pytest/f9964b75e7065ad35a88c686e629c4dd0e1f3357
cp %{_builddir}/pytest-5.4.3/doc/en/_themes/LICENSE %{buildroot}/usr/share/package-licenses/pytest/d0eff60551064b040266867c393e035d747b0ae5
cp %{_builddir}/pytest-5.4.3/doc/en/license.rst %{buildroot}/usr/share/package-licenses/pytest/cfd3360ed6f322792188388b8f2f2410a2427841
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/py.test
/usr/bin/pytest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest/cfd3360ed6f322792188388b8f2f2410a2427841
/usr/share/package-licenses/pytest/d0eff60551064b040266867c393e035d747b0ae5
/usr/share/package-licenses/pytest/f9964b75e7065ad35a88c686e629c4dd0e1f3357

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
