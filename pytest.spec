#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest
Version  : 3.6.1
Release  : 65
URL      : http://pypi.debian.net/pytest/pytest-3.6.1.tar.gz
Source0  : http://pypi.debian.net/pytest/pytest-3.6.1.tar.gz
Summary  : pytest: simple powerful testing with Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pytest-bin
Requires: pytest-python3
Requires: pytest-license
Requires: pytest-python
Requires: atomicwrites
Requires: attrs
Requires: funcsigs
Requires: more-itertools
Requires: pluggy
Requires: py
Requires: setuptools
Requires: six
BuildRequires : argcomplete
BuildRequires : argparse
BuildRequires : atomicwrites
BuildRequires : attrs
BuildRequires : colorama
BuildRequires : execnet
BuildRequires : more-itertools
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pexpect
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest-xdist
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : six
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
Requires: pytest-license

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
Requires: pytest-python3

%description python
python components for the pytest package.


%package python3
Summary: python3 components for the pytest package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest package.


%prep
%setup -q -n pytest-3.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529117039
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pytest
cp LICENSE %{buildroot}/usr/share/doc/pytest/LICENSE
cp doc/en/license.rst %{buildroot}/usr/share/doc/pytest/doc_en_license.rst
cp doc/en/_themes/LICENSE %{buildroot}/usr/share/doc/pytest/doc_en__themes_LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
%defattr(-,root,root,-)
/usr/share/doc/pytest/LICENSE
/usr/share/doc/pytest/doc_en__themes_LICENSE
/usr/share/doc/pytest/doc_en_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
