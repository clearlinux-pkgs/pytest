#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest
Version  : 5.3.1
Release  : 125
URL      : https://files.pythonhosted.org/packages/58/76/45329365ccc901e954cbc6d4c4a7cb6162600a34ed060a6b7b4f127d8183/pytest-5.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/76/45329365ccc901e954cbc6d4c4a7cb6162600a34ed060a6b7b4f127d8183/pytest-5.3.1.tar.gz
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

%description python3
python3 components for the pytest package.


%prep
%setup -q -n pytest-5.3.1
cd %{_builddir}/pytest-5.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575281718
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest
cp %{_builddir}/pytest-5.3.1/LICENSE %{buildroot}/usr/share/package-licenses/pytest/27e1a44d6dd35f55d274aa6f5767f5ad27d94752
cp %{_builddir}/pytest-5.3.1/doc/en/_themes/LICENSE %{buildroot}/usr/share/package-licenses/pytest/d0eff60551064b040266867c393e035d747b0ae5
cp %{_builddir}/pytest-5.3.1/doc/en/license.rst %{buildroot}/usr/share/package-licenses/pytest/c760b98ad5625c2bde208b9ab0df18dbbc23a6d1
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
/usr/share/package-licenses/pytest/27e1a44d6dd35f55d274aa6f5767f5ad27d94752
/usr/share/package-licenses/pytest/c760b98ad5625c2bde208b9ab0df18dbbc23a6d1
/usr/share/package-licenses/pytest/d0eff60551064b040266867c393e035d747b0ae5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
