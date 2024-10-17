%define	lib_name_orig libclanlib
%define	lib_major 2
%define	lib_name %mklibname clanlib %{lib_major}

Name:		clanlib0.6
Summary:	The ClanLib Game SDK
Version:	0.6.5
Release:	41
License:	LGPLv2+
Group:		System/Libraries
URL:		https://www.clanlib.org/
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
Patch15:	ClanLib-0.6.5-gcc4.6.patch
Patch16:	ClanLib-0.6.5-gzopen-flags.patch
Patch17:	ClanLib-0.6.5-gcc45.patch
Patch18:	ClanLib-0.6.5-libpng1.5.patch
Patch19:	ClanLib-0.6.5-link.patch
BuildRequires:	hermes-devel >= 1.3.0
BuildRequires:	libmikmod-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	mesa-common-devel
BuildRequires:	autoconf2.5
BuildRequires:	tiff-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(freetype2)
Provides:	ClanLib = %{version}-%{release}

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
Provides:	ClanLib-mikmod = %{version}-%{release} clanlib-mikmod = %{version}-%{release}
Provides:	%{lib_name_orig}-mikmod

%description -n	%{lib_name}-mikmod
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the MikMod module (clanMikMod).

%package -n	%{lib_name}-png
Summary:	ClanLib PNG module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	ClanLib-png = %{version}-%{release} clanlib-png = %{version}-%{release}
Provides:	%{lib_name_orig}-png

%description -n	%{lib_name}-png
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the PNG module (clanPNG).

%package	docs
Summary:	ClanLib documentation
Group:		Books/Computer books
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
%patch15 -p1
%patch16 -p1
%patch17 -p0
%patch18 -p0
%patch19 -p0

autoconf

%build
export COMMON_CONFIGURE_FLAGS="--enable-dyn --enable-joystick --disable-lua --disable-debug --enable-ttf --disable-directfb"
# (sb) doesn't build on PPC with this
%ifarch %ix86
# (gc) workaround g++ exception bug when -fomit-frame-pointer is set
export CFLAGS="%{optflags} -fno-omit-frame-pointer" CXXFLAGS="%{optflags} -fno-omit-frame-pointer"
%else
export COMMON_CONFIGURE_FLAGS="$COMMON_CONFIGURE_FLAGS --disable-asm386"
%endif

%configure2_5x $COMMON_CONFIGURE_FLAGS

# (gc) there can be ordering problem when using percent-make, don't use it
make all
make strip
chmod 755 Documentation/FAQ.theme
rm -f Libs/*.a
make docs

%install
%makeinstall BIN_PREFIX=%{buildroot}%{_bindir} LIB_PREFIX=%{buildroot}%{_libdir} INC_PREFIX=%{buildroot}%{_includedir} TARGET_PREFIX=%{buildroot}%{_libdir}/ClanLib
make MAN_PREFIX=%{buildroot}%{_mandir} HTML_PREFIX=%{buildroot}%{_datadir}/doc/%{name}-docs-%{version}/Docs docs_install

%files -n %{lib_name}
%doc README COPYING CREDITS
%{_libdir}/libclanCore.so.*
%{_libdir}/libclanApp.so.*
%{_libdir}/libclanDisplay.so.*

%files -n %{lib_name}-devel
%doc README COPYING CODING_STYLE ascii-logo
%{_libdir}/*.so
%{_includedir}/ClanLib
%{_bindir}/clanlib-config

%files -n %{lib_name}-static-devel
%doc README
%{_libdir}/*.a

%files docs
%{_docdir}/%{name}-docs-%{version}/*

%files -n %{lib_name}-mikmod
%doc README
%{_libdir}/libclanMikMod.so.*

%files -n %{lib_name}-png
%doc README
%{_libdir}/libclanPNG.so.*

%files -n %{lib_name}-ttf
%doc README
%{_libdir}/libclanTTF.so.*

%files -n %{lib_name}-jpeg
%doc README
%{_libdir}/libclanJPEG.so.*

%files -n %{lib_name}-network
%doc README
%{_libdir}/libclanNetwork.so.*

%files -n %{lib_name}-vorbis
%doc README
%{_libdir}/libclanVorbis.so.*

%files -n %{lib_name}-smalljpeg
%doc README
%{_libdir}/libclanSmallJPEG.so.*

%files -n %{lib_name}-sound
%doc README
%{_libdir}/libclanSound.so.*

%files -n %{lib_name}-gui
%doc README
%{_libdir}/libclanGUI.so.*

%files -n %{lib_name}-gl
%doc README
%{_libdir}/libclanGL.so.*

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-38mdv2011.0
+ Revision: 663747
- P15: fix build with gcc-4.6 (fedora)
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-37mdv2011.0
+ Revision: 603834
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-36mdv2010.1
+ Revision: 488743
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-35mdv2010.0
+ Revision: 416609
- rebuilt against libjpeg v7

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-34mdv2010.0
+ Revision: 413239
- rebuild

* Thu Apr 09 2009 Funda Wang <fwang@mandriva.org> 0.6.5-33mdv2009.1
+ Revision: 365331
- rediff gcc 4.3 patch

* Mon Aug 18 2008 Funda Wang <fwang@mandriva.org> 0.6.5-33mdv2009.0
+ Revision: 273119
- disable diretfb support as it does not like directfb 1.2.x
- rebuild for new dfb

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 0.6.5-31mdv2009.0
+ Revision: 271850
- patch for new libmikmod

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat May 31 2008 Funda Wang <fwang@mandriva.org> 0.6.5-30mdv2009.0
+ Revision: 213730
- rebuild for new directfb

* Wed May 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-29mdv2009.0
+ Revision: 209707
- bunzipped the patches
- added a gcc43 patch from fedora

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.6.5-28mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 28 2007 Crispin Boylan <crisb@mandriva.org> 0.6.5-28mdv2008.0
+ Revision: 73266
- Patch12: typename qualification on iterator for gcc 3.4+

* Tue May 22 2007 Götz Waschk <waschk@mandriva.org> 0.6.5-27mdv2008.0
+ Revision: 29787
- Import clanlib0.6



* Tue May 22 2007 Götz Waschk <waschk@mandriva.org> 0.6.5-27
- Rebuild

* Fri Aug  4 2006 Olivier Blin <blino@mandriva.com> 0.6.5-26mdv2007.0
- Patch11: fix "extra qualification 'class::' on member 'member'" errors
- BuildRequires X11-static-devel instead of XFree86-static-libs
- clean buildroot

* Fri Jun 30 2006 Stefan van der Eijk <stefan@eijk.nu> 0.6.5-25
- png rebuild

* Wed May 10 2006 Götz Waschk <waschk@mandriva.org> 0.6.5-24mdk
- update patch 10 for new directfb

* Wed Dec 21 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.6.5-23mdk
- fix conflicts with newer clanlib

* Thu Nov 03 2005 Götz Waschk <waschk@mandriva.org> 0.6.5-22mdk
- rebuild for new directfb

* Fri Jul 15 2005 Olivier Blin <oblin@mandriva.com> 0.6.5-21mdk
- rebuild for new directfb

* Tue May 10 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.5-20mdk
- rebuild against current directfb library
- remove hardcoded obsolete packager tag

* Wed Feb 16 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.6.5-19mdk
- fixes for DirectFB >= 0.9.21

* Mon Oct  4 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.6.5-18mdk
- fix freetype auto-detection, build libclanTTF everywhere

* Tue Jun 29 2004 Michael Scherer <misc@mandrake.org> 0.6.5-17mdk 
- fix typo on Requires

* Tue Jun 29 2004 Michael Scherer <misc@mandrake.org> 0.6.5-16mdk 
- fix wrong Requires

* Tue Jun 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.5-15mdk
- reenable directfb support as it's no longer in contrib
- cosmetics

* Mon Jun 28 2004 Michael Scherer <misc@mandrake.org> 0.6.5-14mdk 
- gcc3.4 fix, rebuild
- remove Packager tag
- fix Provides on static

* Fri Feb  6 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-13mdk
- gosh, remove dep on DirectFB-devel in BuildRequires as well

* Thu Jan 29 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-12mdk
- disable directfb, it's in contrib

* Sat Jan 03 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.6.5-11mdk 
- From Husson Pierre-Hugues <phh@sidenux.ath.cx>
  - Fix to make Slbd working
  - Provide support for directfb, but need directfb 0.9.20 another version aren't allowed

* Wed Oct  8 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.6.5-10mdk
- lib64 & 64-bit fixes
- some bounds checking from Debian people to avoid segfault

* Thu Sep  4 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-9mdk
- fixes invalid-build-requires libbzip2-devel

* Tue Sep  2 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-8mdk
- main lib provide a 64bit agnostic name, so that clients can require a
  specific version (needed because of binary incompatibility of datafiles
  between versions of clanlib)

* Wed Jul  9 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-7mdk
- rebuild for new devel provides

* Wed Jun 11 2003 Götz Waschk <waschk@linux-mandrake.com> 0.6.5-6mdk
- don't require the static-devel package in the devel package

* Wed Jun 11 2003 Götz Waschk <waschk@linux-mandrake.com> 0.6.5-5mdk
- fix buildrequires
- make the devel package require all lib packages
- patch4: build fix for gcc 3.3

* Tue May 20 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-4mdk
- fix distlint's DIRM: (x28) /usr/include/ClanLib/ 

* Thu Apr 24 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-3mdk
- fix buildrequires thx to stefan's robot
- use correct %%configure call (2.5x form)
- fix png lib detection

* Sat Feb 15 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-2mdk
- provide lib_name_orig-NAME in each package too, for not breaking
  BuildRequires dependencies for other packages.

* Mon Jan 20 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-1mdk
- use nice work from Crispin Boylan <viewtronix@uklinux.net>
  - New version
- makefile doesn't work properly in parallel, use make rather than %%make :(
- use %%mklibname

* Mon Oct 14 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.1-9mdk
- fix permissions
- fix doc subpackage group
- fix configure-without-libdir-spec

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.5.1-8mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.5.1-7mdk
- Automated rebuild with gcc3.2

* Wed May 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.1-6mdk
- rebuild to link against latest libstdc++

* Thu Jan 17 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.1-5mdk
- provide GL package now

* Sat Dec  1 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 0.5.1-4mdk
- patch6: cast to fix 64-bit build

* Tue Nov 13 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 0.5.1-3mdk
- apply PPC patch on all non-x86 arches
- use %%make macro
- execute autoconf during %%prep stage
- make x86-specific configure flags %%ifarch %%ix86
- simplify %%configure arch-conditional code

* Tue Nov 13 2001 Stew Benedict <sbenedict@mandrakesoft.com> 0.5.1-2mdk
- smalljpeg uses x86 assembly, even with --disable-asm386 - PPC patch

* Fri Nov  9 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.1-1mdk
- version 0.5.1 (warning, datafile is not binary compatible with 0.5.0,
  apps need to be rebuilded)

* Wed Oct 17 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.0-6mdk
- fix no-documentation
- add Joystick support

* Fri Oct 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.0-5mdk
- have good compilation option for PPC (stew)
- rebuild for libpng3
- fix invalid-spec-name 
- fix obsolete-tag Copyright
- better lib policy respect with Provides

* Mon Sep 10 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.0-4mdk
- we don't need launch_x11_clanapp anymore with 0.5

* Thu Aug 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.0-3mdk
- rebuild to fix distribution tag and provides

* Sat Jun 30 2001 Stefan van der Eijk <stefan@eijk.nu> 0.5.0-2mdk
- BuildRequires:	freetype-devel --> freetype2-devel
- Removed BuildRequires:	XFree86-devel, zlib-devel

* Tue Jun 26 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.0-1mdk
- release 0.5.0

* Thu Apr 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-25mdk
- don't block forever on a busy dsp (patch #5)

* Fri Mar 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-24mdk
- use no-omit-frame-pointer to workaround g++ exceptions bug

* Thu Mar 22 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-23mdk
- remove explicit requires on requires, silly me

* Fri Mar  9 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-22mdk
- recompile without svgalib

* Fri Feb 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-21mdk
- do not put the launch_x11_clanapp script in the lib package!
- provides devel-lib with version
- put subpackages' devel files in generic devel package

* Mon Feb 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-20mdk
- fix BuildRequires (libbzip2-devel, thx to Jeff)

* Fri Dec  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-19mdk
- fix BuildRequires

* Tue Nov 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-18mdk
- new lib policy

* Tue Nov  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-17mdk
- provides ClanLib for compatibility

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-16mdk
- rebuild to have correct deps (e.g. sucking libraries linked to themselves)
- change name to clanlib (e.g. uppercase names suck)
- rebuild against lowercased hermes

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-15mdk
- really recompile against newest libstdc++

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-14mdk
- recompile against newest libstdc++

* Mon Oct 16 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-13mdk
- fix no-newline-at-end-of-some-sourcefiles that bothers gcc-2.96

* Mon Oct 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.4.4-12mdk
- Fix gcc2.96 compilation;

* Sun Sep 17 2000 David BAUDENS <baudens@mandrakesoft.com> 0.4.4-11mdk
- Don't use i386 code on non i386 compatibles archs
- Let configure do is job on PPC (and really don't use i386 code)

* Fri Sep 15 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-10mdk
- rebuild against fixed XFree-4 by fredl

* Fri Sep  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-9mdk
- fixed BuildRequires: removed ClanLib-devel, added XFree86-static-libs,
  ImageMagick >= 5.0.0
- removed nasty static -march=pentium, /me sucks

* Wed Sep  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-8mdk
- added the optional force of x11 target (envvar CLANLIB_FORCE_X11_DISPLAY)
- added a script to launch clanlib apps with force x11 target

* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-7mdk
- added more documentation in subpackages

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-6mdk
- automatically added packager tag

* Wed Aug 23 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.4-5mdk
- corrected BuildRequires for archs other than ix86.

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.4-4mdk
- automatically added BuildRequires

* Tue Aug  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-3mdk
- not 100%% sure with the 2mdk

* Mon Jul 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-2mdk
- integrated patch to ImageMagick stuff from the clanlib-devel mailing
  list, thanks to the help of Ingo Ruhnke <grumbel@gmx.de>; it was a
  contribution from Matt Kimball <mkimball@veriomail.com>

* Mon Jul 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-1mdk
- took SRPM from ClanLib web site
- Mandrake adaptations
- ugly: take the Magick stuff from CVS to compile with ImageMagick 5
- mega headache; had to redefine CXXFLAGS to remove -mcpu=pentiumpro
