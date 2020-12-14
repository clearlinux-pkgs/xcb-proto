#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCCC4F07FAC641EFF (daniel@fooishbar.org)
#
Name     : xcb-proto
Version  : 1.13
Release  : 44
URL      : http://xorg.freedesktop.org/releases/individual/xcb/xcb-proto-1.13.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/xcb/xcb-proto-1.13.tar.gz
Source1  : http://xorg.freedesktop.org/releases/individual/xcb/xcb-proto-1.13.tar.gz.sig
Summary  : XML-XCB protocol descriptions
Group    : Development/Tools
License  : MIT
Requires: xcb-proto-data = %{version}-%{release}
Requires: xcb-proto-license = %{version}-%{release}
Requires: xcb-proto-python = %{version}-%{release}
Requires: xcb-proto-python3 = %{version}-%{release}
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
Requires: xcb-proto-data = %{version}-%{release}
Provides: xcb-proto-devel = %{version}-%{release}
Requires: xcb-proto = %{version}-%{release}
Requires: xcb-proto = %{version}-%{release}

%description dev
dev components for the xcb-proto package.


%package dev32
Summary: dev32 components for the xcb-proto package.
Group: Default
Requires: xcb-proto-data = %{version}-%{release}
Requires: xcb-proto-dev = %{version}-%{release}

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
Requires: xcb-proto-python3 = %{version}-%{release}

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
cd %{_builddir}/xcb-proto-1.13
pushd ..
cp -a xcb-proto-1.13 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582901794
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1582901794
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xcb-proto
cp %{_builddir}/xcb-proto-1.13/COPYING %{buildroot}/usr/share/package-licenses/xcb-proto/1d6467e08284270291d138c7ea07f24689483068
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xcb-proto/1d6467e08284270291d138c7ea07f24689483068

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
