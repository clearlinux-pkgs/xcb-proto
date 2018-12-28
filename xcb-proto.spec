#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xcb-proto
Version  : 1.13
Release  : 35
URL      : http://xorg.freedesktop.org/releases/individual/xcb/xcb-proto-1.13.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/xcb/xcb-proto-1.13.tar.gz
Summary  : X protocol descriptions for XCB
Group    : Development/Tools
License  : MIT
Requires: xcb-proto-python3
Requires: xcb-proto-license
Requires: xcb-proto-data
Requires: xcb-proto-python
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxml2-dev

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
Provides: xcb-proto-devel

%description dev
dev components for the xcb-proto package.


%package dev32
Summary: dev32 components for the xcb-proto package.
Group: Default
Requires: xcb-proto-data
Requires: xcb-proto-dev

%description dev32
dev32 components for the xcb-proto package.


%package license
Summary: license components for the xcb-proto package.
Group: Default

%description license
license components for the xcb-proto package.


%package python
Summary: python components for the xcb-proto package.
Group: Default
Requires: xcb-proto-python3

%description python
python components for the xcb-proto package.


%package python3
Summary: python3 components for the xcb-proto package.
Group: Default
Requires: python3-core

%description python3
python3 components for the xcb-proto package.


%prep
%setup -q -n xcb-proto-1.13
pushd ..
cp -a xcb-proto-1.13 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529093658
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1529093658
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xcb-proto
cp COPYING %{buildroot}/usr/share/doc/xcb-proto/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
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
/usr/lib64/pkgconfig/xcb-proto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32xcb-proto.pc
/usr/lib32/pkgconfig/xcb-proto.pc

%files license
%defattr(-,root,root,-)
/usr/share/doc/xcb-proto/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
