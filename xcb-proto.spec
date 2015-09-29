#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xcb-proto
Version  : 1.11
Release  : 5
URL      : http://xorg.freedesktop.org/releases/individual/xcb/xcb-proto-1.11.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/xcb/xcb-proto-1.11.tar.gz
Summary  : X protocol descriptions for XCB
Group    : Development/Tools
License  : MIT
Requires: xcb-proto-python
Requires: xcb-proto-data
BuildRequires : libxml2-dev
BuildRequires : python-dev
BuildRequires : python3

%description
About xcb-proto
===============
xcb-proto provides the XML-XCB protocol descriptions that libxcb uses to
generate the majority of its code and API. We provide them separately
from libxcb to allow reuse by other projects, such as additional
language bindings, protocol dissectors, or documentation generators.

%package data
Summary: data components for the xcb-proto package.
Group: Data

%description data
data components for the xcb-proto package.


%package dev
Summary: dev components for the xcb-proto package.
Group: Development
Requires: xcb-proto-data

%description dev
dev components for the xcb-proto package.


%package python
Summary: python components for the xcb-proto package.
Group: Default

%description python
python components for the xcb-proto package.


%prep
%setup -q -n xcb-proto-1.11

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xcb/bigreq.xml
/usr/share/xcb/composite.xml
/usr/share/xcb/damage.xml
/usr/share/xcb/dpms.xml
/usr/share/xcb/dri2.xml
/usr/share/xcb/dri3.xml
/usr/share/xcb/ge.xml
/usr/share/xcb/glx.xml
/usr/share/xcb/present.xml
/usr/share/xcb/randr.xml
/usr/share/xcb/record.xml
/usr/share/xcb/render.xml
/usr/share/xcb/res.xml
/usr/share/xcb/screensaver.xml
/usr/share/xcb/shape.xml
/usr/share/xcb/shm.xml
/usr/share/xcb/sync.xml
/usr/share/xcb/xc_misc.xml
/usr/share/xcb/xcb.xsd
/usr/share/xcb/xevie.xml
/usr/share/xcb/xf86dri.xml
/usr/share/xcb/xf86vidmode.xml
/usr/share/xcb/xfixes.xml
/usr/share/xcb/xinerama.xml
/usr/share/xcb/xinput.xml
/usr/share/xcb/xkb.xml
/usr/share/xcb/xprint.xml
/usr/share/xcb/xproto.xml
/usr/share/xcb/xselinux.xml
/usr/share/xcb/xtest.xml
/usr/share/xcb/xv.xml
/usr/share/xcb/xvmc.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/*.pc

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
