#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest
Version  : 6.2.5
Release  : 167
URL      : https://files.pythonhosted.org/packages/4b/24/7d1f2d2537de114bdf1e6875115113ca80091520948d370c964b88070af2/pytest-6.2.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/4b/24/7d1f2d2537de114bdf1e6875115113ca80091520948d370c964b88070af2/pytest-6.2.5.tar.gz
Summary  : pytest: simple powerful testing with Python
Group    : Development/Tools
License  : MIT
Requires: pytest-bin = %{version}-%{release}
Requires: pytest-license = %{version}-%{release}
Requires: pytest-python = %{version}-%{release}
Requires: pytest-python3 = %{version}-%{release}
Requires: Django
Requires: atomicwrites
Requires: attrs
Requires: importlib_metadata
Requires: iniconfig
Requires: packaging
Requires: pluggy
Requires: py
Requires: toml
BuildRequires : Django
BuildRequires : argcomplete
BuildRequires : atomicwrites
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : execnet
BuildRequires : hypothesis
BuildRequires : iniconfig
BuildRequires : nose
BuildRequires : packaging
BuildRequires : pexpect
BuildRequires : pluggy
BuildRequires : py
BuildRequires : pytest-xdist
BuildRequires : setuptools_scm
BuildRequires : toml
BuildRequires : xmlschema

%description
.. image:: https://github.com/pytest-dev/pytest/raw/main/doc/en/img/pytest_logo_curves.svg
:target: https://docs.pytest.org/en/stable/
:align: center
:alt: pytest

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
Requires: pypi(iniconfig)
Requires: pypi(packaging)
Requires: pypi(pluggy)
Requires: pypi(py)
Requires: pypi(toml)

%description python3
python3 components for the pytest package.


%prep
%setup -q -n pytest-6.2.5
cd %{_builddir}/pytest-6.2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636406524
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest --verbose || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest
cp %{_builddir}/pytest-6.2.5/LICENSE %{buildroot}/usr/share/package-licenses/pytest/f9964b75e7065ad35a88c686e629c4dd0e1f3357
cp %{_builddir}/pytest-6.2.5/doc/en/license.rst %{buildroot}/usr/share/package-licenses/pytest/bbb7388178be2178c29315201a7e120e235590ea
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
/usr/share/package-licenses/pytest/bbb7388178be2178c29315201a7e120e235590ea
/usr/share/package-licenses/pytest/f9964b75e7065ad35a88c686e629c4dd0e1f3357

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
