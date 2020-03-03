#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : plotly
Version  : 4.1.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/3b/26/d68b3042f22ccff4156670dff167c086a94331fe32111d5972aeac0579d4/plotly-4.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/26/d68b3042f22ccff4156670dff167c086a94331fe32111d5972aeac0579d4/plotly-4.1.1.tar.gz
Summary  : An open-source, interactive graphing library for Python
Group    : Development/Tools
License  : MIT
Requires: plotly-data = %{version}-%{release}
Requires: plotly-license = %{version}-%{release}
Requires: plotly-python = %{version}-%{release}
Requires: plotly-python3 = %{version}-%{release}
Requires: retrying
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : retrying
BuildRequires : six
Patch1: 0001-Fix-notebook-extension-install-path.patch

%description
The main plotly distribution package

%package data
Summary: data components for the plotly package.
Group: Data

%description data
data components for the plotly package.


%package license
Summary: license components for the plotly package.
Group: Default

%description license
license components for the plotly package.


%package python
Summary: python components for the plotly package.
Group: Default
Requires: plotly-python3 = %{version}-%{release}

%description python
python components for the plotly package.


%package python3
Summary: python3 components for the plotly package.
Group: Default
Requires: python3-core
Provides: pypi(plotly)

%description python3
python3 components for the plotly package.


%prep
%setup -q -n plotly-4.1.1
cd %{_builddir}/plotly-4.1.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583202572
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
mkdir -p %{buildroot}/usr/share/package-licenses/plotly
cp %{_builddir}/plotly-4.1.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/plotly/c340b1b30a740d882e192d6d38588465417cfdc4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbextensions/nbconfig/notebook.d/plotlywidget.json
/usr/share/jupyter/nbextensions/plotlywidget/extension.js
/usr/share/jupyter/nbextensions/plotlywidget/index.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plotly/c340b1b30a740d882e192d6d38588465417cfdc4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
