#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest
Version  : 4.0.1
Release  : 80
URL      : https://files.pythonhosted.org/packages/24/f1/0e378fa418d9ac15d2d28296be916a55e351a6ffeb74105fe333c15ea58a/pytest-4.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/24/f1/0e378fa418d9ac15d2d28296be916a55e351a6ffeb74105fe333c15ea58a/pytest-4.0.1.tar.gz
Summary  : pytest: simple powerful testing with Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pytest-bin = %{version}-%{release}
Requires: pytest-license = %{version}-%{release}
Requires: pytest-python = %{version}-%{release}
Requires: pytest-python3 = %{version}-%{release}
Requires: atomicwrites
Requires: attrs
Requires: funcsigs
Requires: more-itertools
Requires: pathlib2
Requires: pluggy
Requires: py
Requires: setuptools
Requires: six
BuildRequires : argcomplete
BuildRequires : argparse
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : execnet
BuildRequires : nose
BuildRequires : pexpect
BuildRequires : pytest-xdist
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : unittest2

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
%setup -q -n pytest-4.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543136626
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest
cp LICENSE %{buildroot}/usr/share/package-licenses/pytest/LICENSE
cp doc/en/_themes/LICENSE %{buildroot}/usr/share/package-licenses/pytest/doc_en__themes_LICENSE
cp doc/en/license.rst %{buildroot}/usr/share/package-licenses/pytest/doc_en_license.rst
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
/usr/share/package-licenses/pytest/LICENSE
/usr/share/package-licenses/pytest/doc_en__themes_LICENSE
/usr/share/package-licenses/pytest/doc_en_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
