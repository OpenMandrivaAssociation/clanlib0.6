%define	name	clanlib0.6
%define	version	0.6.5
%define release	32
%define	lib_name_orig libclanlib
%define	lib_major 2
%define	lib_name %mklibname clanlib %{lib_major}

Name:		%{name}
Summary:	The ClanLib Game SDK
Version:	%{version}
Release:	%mkrel %{release}
License:	LGPL
Group:		System/Libraries
Source0:	http://www.clanlib.org/download/files/ClanLib-%{version}-1.tar.bz2
Patch0:		ClanLib-0.6.5-display-compilation.patch
Patch1:		ClanLib-0.6.5-doc-fix.patch
Patch2:		ClanLib-0.6.5-glXGetProcAddressARB.patch
Patch3:		ClanLib-0.6.5-fix-png-detection.patch
Patch4:		ClanLib-0.6.5-gcc33.patch
Patch5:		ClanLib-0.6.5-64bit-fixes.patch
Patch6:		ClanLib-0.6.5-bounds.patch
Patch7:		ClanLib-0.6.5-directfb-ttf-fix.patch
Patch8:		ClanLib-0.6.5-gcc34.patch
Patch9:		ClanLib-0.6.5-freetype.patch
Patch10:	ClanLib-0.6.5-directfb-fixes.patch
Patch11:	ClanLib-0.6.5-extraqualif.patch
Patch12:	ClanLib-0.6.5-typename.patch
Patch13:	ClanLib-0.6.5-gcc4.3.patch
Patch14:	ClanLib-0.6.5-new-mikmod.patch
URL:		http://www.clanlib.org/
BuildRequires:	libhermes-devel >= 1.3.0 libmikmod-devel libpng-devel Mesa-common-devel autoconf2.5
BuildRequires:	libtiff-devel X11-static-devel bzip2-devel libvorbis-devel DirectFB-devel
Obsoletes:	ClanLib
Provides:	ClanLib = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The ClanLib Game SDK is a crossplatform game library designed to ease the work
for game developers. The goal is to provide a common interface to classical
game problems (loading graphics eg.), so games can share as much code as
possible. Ideally anyone with small resources should be able to write
commercial quality games.

%package -n	%{lib_name}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{lib_name}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{lib_name} = %{version}-%{release}
Requires:	%{lib_name}-gl = %{version}-%{release}
Requires:	%{lib_name}-gui = %{version}-%{release}
Requires:	%{lib_name}-jpeg = %{version}-%{release}
Requires:	%{lib_name}-mikmod = %{version}-%{release}
Requires:	%{lib_name}-network = %{version}-%{release}
Requires:	%{lib_name}-png = %{version}-%{release}
Requires:	%{lib_name}-smalljpeg = %{version}-%{release}
Requires:	%{lib_name}-sound = %{version}-%{release}
Requires:	%{lib_name}-ttf = %{version}-%{release}
Requires:	%{lib_name}-vorbis = %{version}-%{release}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Obsoletes:	ClanLib-devel clanlib-devel
Provides:	ClanLib-devel = %{version}-%{release} clanlib-devel = %{version}-%{release} %{name}-devel
Conflicts:	clanlib-devel > 0.7.0
%description -n	%{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	%{lib_name}-static-devel
Summary:	Static libraries for %{name}
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-static-devel = %{version}-%{release}
Obsoletes:	ClanLib-static-devel clanlib-static-devel
Provides:	ClanLib-static-devel = %{version}-%{release} clanlib-static-devel = %{version}-%{release}

%description -n	%{lib_name}-static-devel
This package contains the static libraries for %{name}.

%package -n	%{lib_name}-sound
Summary:	ClanLib Sound module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-sound

%description -n	%{lib_name}-sound
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Sound module (clanSound).

%package -n	%{lib_name}-vorbis
Summary:	ClanLib Vorbis module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-vorbis

%description -n	%{lib_name}-vorbis
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Vorbis module (clanVorbis).

%package -n	%{lib_name}-network
Summary:	ClanLib Network module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-network

%description -n	%{lib_name}-network
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Network module (clanNetwork).

%package -n	%{lib_name}-jpeg
Summary:	ClanLib Jpeg module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-jpeg

%description -n	%{lib_name}-jpeg
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Jpeg module (clanJPEG).

%package -n	%{lib_name}-gui
Summary:	ClanLib Gui module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-gui

%description -n	%{lib_name}-gui
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Gui module (clanGUI).

%package -n	%{lib_name}-gl
Summary:	ClanLib GL module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-gl

%description -n	%{lib_name}-gl
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the GL module (clanGL).

%package -n	%{lib_name}-ttf
Summary:	ClanLib TTF module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-ttf

%description -n	%{lib_name}-ttf
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the TTF module (clanTTF).

%package -n	%{lib_name}-smalljpeg
Summary:	ClanLib SmallJPEG module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-smalljpeg

%description -n	%{lib_name}-smalljpeg
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the SmallJPEG module
(clanSmallJPEG).

%package -n	%{lib_name}-mikmod
Summary:	ClanLib MikMod module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:	ClanLib-mikmod clanlib-mikmod
Provides:	ClanLib-mikmod = %{version}-%{release} clanlib-mikmod = %{version}-%{release}
Provides:	%{lib_name_orig}-mikmod

%description -n	%{lib_name}-mikmod
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the MikMod module (clanMikMod).

%package -n	%{lib_name}-png
Summary:	ClanLib PNG module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:	ClanLib-png clanlib-png
Provides:	ClanLib-png = %{version}-%{release} clanlib-png = %{version}-%{release}
Provides:	%{lib_name_orig}-png

%description -n	%{lib_name}-png
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the PNG module (clanPNG).

%package	docs
Summary:	ClanLib documentation
Group:		Books/Computer books
Obsoletes:	ClanLib-docs clanlib-docs
Provides:	ClanLib-docs = %{version}-%{release} clanlib-docs = %{version}-%{release}

%description	docs
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package contains the documentation.

%prep
%setup -q -n ClanLib-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1 -b .64bit-fixes
%patch6 -p1 -b .bounds
%patch7 -p1
%patch8 -p0
%patch9 -p1 -b .freetype
%patch10 -p1 -b .directfb-fixes
%patch11 -p1 -b .extraqualif
%patch12 -p1 -b .typename
%patch13 -p1 -z .gcc43
%patch14 -p1

autoconf

%build
export COMMON_CONFIGURE_FLAGS="--enable-dyn --enable-joystick --disable-lua --disable-debug --enable-ttf"
# (sb) doesn't build on PPC with this
%ifarch %ix86
# (gc) workaround g++ exception bug when -fomit-frame-pointer is set
export CFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer" CXXFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer"
%else
export COMMON_CONFIGURE_FLAGS="$COMMON_CONFIGURE_FLAGS --disable-asm386"
%endif

%ifarch ppc
# (sb) configure macro breaks PPC build - just do it manually for now
libtoolize --copy --force
./configure $COMMON_CONFIGURE_FLAGS --libdir=%_libdir
%else
%configure2_5x $COMMON_CONFIGURE_FLAGS
%endif

# (gc) there can be ordering problem when using percent-make, don't use it
make all
make strip
chmod 755 Documentation/FAQ.theme
rm -f Libs/*.a
make docs

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall BIN_PREFIX=$RPM_BUILD_ROOT%{_bindir} LIB_PREFIX=$RPM_BUILD_ROOT%{_libdir} INC_PREFIX=$RPM_BUILD_ROOT%{_includedir} TARGET_PREFIX=$RPM_BUILD_ROOT%{_libdir}/ClanLib
make MAN_PREFIX=$RPM_BUILD_ROOT%{_mandir} HTML_PREFIX=$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-docs-%{version}/Docs docs_install

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-mikmod -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-png -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-sound -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-vorbis -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-network -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-jpeg -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-gui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-ttf -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-smalljpeg -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-gl -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %{lib_name}-mikmod -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %{lib_name}-png -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-sound -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-vorbis -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-network -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-jpeg -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-gui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-ttf -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-smalljpeg -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-gl -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-, root, root)
%doc README COPYING CREDITS
%{_libdir}/libclanCore.so.*
%{_libdir}/libclanApp.so.*
%{_libdir}/libclanDisplay.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc README COPYING CODING_STYLE ascii-logo
%{_libdir}/*.so
%{_includedir}/ClanLib
%{_bindir}/clanlib-config

%files -n %{lib_name}-static-devel
%defattr(-, root, root)
%doc README
%{_libdir}/*.a

%files docs
%defattr(-, root, root)
%{_docdir}/%{name}-docs-%{version}/*

%files -n %{lib_name}-mikmod
%defattr(-, root, root)
%doc README
%{_libdir}/libclanMikMod.so.*

%files -n %{lib_name}-png
%defattr(-, root, root)
%doc README
%{_libdir}/libclanPNG.so.*

%files -n %{lib_name}-ttf
%defattr(-, root, root)
%doc README
%{_libdir}/libclanTTF.so.*

%files -n %{lib_name}-jpeg
%defattr(-, root, root)
%doc README
%{_libdir}/libclanJPEG.so.*

%files -n %{lib_name}-network
%defattr(-, root, root)
%doc README
%{_libdir}/libclanNetwork.so.*

%files -n %{lib_name}-vorbis
%defattr(-, root, root)
%doc README
%{_libdir}/libclanVorbis.so.*

%files -n %{lib_name}-smalljpeg
%defattr(-, root, root)
%doc README
%{_libdir}/libclanSmallJPEG.so.*

%files -n %{lib_name}-sound
%defattr(-, root, root)
%doc README
%{_libdir}/libclanSound.so.*

%files -n %{lib_name}-gui
%defattr(-, root, root)
%doc README
%{_libdir}/libclanGUI.so.*

%files -n %{lib_name}-gl
%defattr(-, root, root)
%doc README
%{_libdir}/libclanGL.so.*

#%files mpeg
#%defattr(-, root, root)
#%{_libdir}/libclanMPEG.so*
