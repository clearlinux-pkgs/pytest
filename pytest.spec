#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest
Version  : 3.4.0
Release  : 59
URL      : http://pypi.debian.net/pytest/pytest-3.4.0.tar.gz
Source0  : http://pypi.debian.net/pytest/pytest-3.4.0.tar.gz
Summary  : pytest: simple powerful testing with Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pytest-bin
Requires: pytest-legacypython
Requires: pytest-python3
Requires: pytest-python
Requires: attrs
Requires: funcsigs
Requires: pluggy
Requires: py
Requires: setuptools
Requires: six
BuildRequires : argcomplete
BuildRequires : argparse
BuildRequires : attrs
BuildRequires : colorama
BuildRequires : execnet
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pexpect
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest-xdist
BuildRequires : python-dev
BuildRequires : python-mock
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

%description bin
bin components for the pytest package.


%package legacypython
Summary: legacypython components for the pytest package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pytest package.


%package python
Summary: python components for the pytest package.
Group: Default
Requires: pytest-legacypython
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
%setup -q -n pytest-3.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518557992
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || : ; py.test-3.5 --verbose || :
%install
export SOURCE_DATE_EPOCH=1518557992
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/py.test
/usr/bin/pytest

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
