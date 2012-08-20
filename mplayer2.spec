%global         date 20120820
%global         gitcommit c62dbb8
%global         gitcommit_full c62dbb829347eaf4040fcc77b636255675d5cafc


Name:           mplayer2
Version:        2.0
Release:        1.%{date}git%{gitcommit}%{?dist}
Summary:        Movie player playing most video formats and DVDs
Epoch:          1

License:        GPLv3+
URL:            http://www.mplayer2.org/
Source0:        http://git.mplayer2.org/mplayer2-build/snapshot/mplayer2-build-2.0.git.tar.xz
Source1:        mplayer.conf
Source2:        input.conf
Source3:        mplayer2.desktop

BuildRequires:  yasm
BuildRequires:  alsa-lib-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel >= 2.0.9
BuildRequires:  libXinerama-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  lirc-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXv-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libXxf86dga-devel
BuildRequires:  aalib-devel
BuildRequires:  libcaca-devel
BuildRequires:  svgalib-devel
BuildRequires:  libmng-devel
BuildRequires:  giflib-devel
BuildRequires:  SDL-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libbluray-devel
BuildRequires:  libdvdnav-devel
BuildRequires:  cdparanoia-devel
BuildRequires:  enca-devel
BuildRequires:  libmad-devel
BuildRequires:  libvorbis-devel
BuildRequires:  speex-devel >= 1.1
BuildRequires:  libtheora-devel
BuildRequires:  libmpg123-devel
BuildRequires:  a52dec-devel
BuildRequires:  libdca-devel
BuildRequires:  faad2-devel
BuildRequires:  ladspa-devel
BuildRequires:  libbs2b-devel
BuildRequires:  libnemesi-devel
#BuildRequires:  live555-devel
BuildRequires:  libdv-devel >= 0.9.5
BuildRequires:  xvidcore-devel
BuildRequires:  libtool
#BuildRequires:  python3
#BuildRequires:  libva-devel

#BuildRequires:  em8300-devel
BuildRequires:  fribidi-devel
#BuildRequires:  lame-devel
#BuildRequires:  libjpeg-devel
#BuildRequires:  libmpeg2-devel
#BuildRequires:  lzo-devel >= 2
#BuildRequires:  schroedinger-devel
#BuildRequires:  twolame-devel
#BuildRequires:  x264-devel >= 0.0.0-0.28
#BuildRequires:  libvpx-devel


%description
MPlayer2 is an advanced general-purpose video player.
A fork of the original MPlayer project, it contains
significant further development and supports a number
of features not available in other Unix players, such
as Matroska external chapters.

%prep
%setup -q -n %{name}-build-2.0.git

echo "--prefix=%{_prefix}
--bindir=%{_bindir}
--datadir=%{_datadir}/%{name}
--mandir=%{_mandir}
--confdir=%{_sysconfdir}/%{name}
--libdir=%{_libdir}
--codecsdir=%{_libdir}/codecs
--extra-cflags=$RPM_OPT_FLAGS
--enable-radio
--enable-radio-capture
--enable-translation
--charset= utf8
--language-man=all
--enable-runtime-cpudetection
--enable-live
" >> mplayer_options

#echo "--enable-vaapi
echo "--enable-runtime-cpudetect
" >> libav_options

#sed -i -e "s|'--disable-devices', '--disable-vaapi'|'--disable-devices'|" "script/libav-config" ;

# fix man pages not being UTF8
# doconv() {
#     iconv -f $1 -t $2 -o mplayer/DOCS/man/$3/mplayer.1.utf8 mplayer/DOCS/man/$3/mplayer.1 && \
#     mv mplayer/DOCS/man/$3/mplayer.1.utf8 mplayer/DOCS/man/$3/mplayer.1
# }
# 
# for lang in de es fr it ; do doconv iso-8859-1 utf-8 $lang ; done
# for lang in hu pl ; do doconv iso-8859-2 utf-8 $lang ; done
# for lang in ru ; do doconv koi8-r utf-8 $lang ; done


%build
# mp3lib looks broken => disabling
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# move man pages and bindir
mv $RPM_BUILD_ROOT%{_bindir}/mplayer $RPM_BUILD_ROOT%{_bindir}/%{name}

find $RPM_BUILD_ROOT%{_mandir} -name "mplayer*" | while read -r file; do \
    mv $file $(echo "$file" | sed -e "s/mplayer.1/mplayer2.1/"); \
done

install -D -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/mplayer.conf
install -D -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/input.conf
install -D -m0644 %{SOURCE3} %{buildroot}%{_datadir}/applications/%{name}.desktop


%postun
update-desktop-database -q


%files
%doc mplayer/AUTHORS mplayer/Copyright mplayer/LICENSE
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_mandir}/man1/%{name}.1*
# %lang(cs) %{_mandir}/cs/man1/%{name}.1*
# %lang(de) %{_mandir}/de/man1/%{name}.1*
# %lang(es) %{_mandir}/es/man1/%{name}.1*
# %lang(fr) %{_mandir}/fr/man1/%{name}.1*
# %lang(hu) %{_mandir}/hu/man1/%{name}.1*
# %lang(it) %{_mandir}/it/man1/%{name}.1*
# %lang(pl) %{_mandir}/pl/man1/%{name}.1*
# %lang(ru) %{_mandir}/ru/man1/%{name}.1*
#%lang(zh_CN) %{_mandir}/zh_CN/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop


%changelog
* Mon Aug 20 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0-1.20120820gitc62dbb8.R
- Update to last revision

* Tue Jun 26 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0-1.20120626gite198fd0.R
- Update to last revision
- Bump epoch

* Fri May 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0-1.20120504gitab6542d.R
- Update to last revision

* Fri May 04 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0-20120504gitf64a4e9-1.R
- Update to last revision

* Tue Apr 24 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.20120424gitb711624-1.R
- Update to last revision

* Wed Mar 28 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.20120328git6c96298-1.R
- Update to last revision

* Fri Feb 24 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.20120220gitfc6a9e4-3.R
- Added desktop file

* Wed Feb 22 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.20120220gitfc6a9e4-2.R
- Added conf files

* Tue Feb 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.20120220gitfc6a9e4-1.R
- Initial release for Fedora
