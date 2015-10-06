#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest
Version  : 2.8.1
Release  : 19
URL      : https://pypi.python.org/packages/source/p/pytest/pytest-2.8.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pytest/pytest-2.8.1.tar.gz
Summary  : pytest: simple powerful testing with Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pytest-bin
Requires: pytest-python
BuildRequires : apipkg-python
BuildRequires : argcomplete
BuildRequires : argparse-python
BuildRequires : colorama-python
BuildRequires : execnet
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pexpect
BuildRequires : pip
BuildRequires : pytest-xdist
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
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


%package python
Summary: python components for the pytest package.
Group: Default
Requires: argparse-python
Requires: colorama-python

%description python
python components for the pytest package.


%prep
%setup -q -n pytest-2.8.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || : ; py.test-3.4 --verbose || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/py.test
/usr/bin/py.test-2.7
/usr/bin/py.test-3.4

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
