%define         git_ver d937de7


Name:           mplayer2
Version:        2.0
Release:        1.git%{?dist}.R
Summary:        Movie player playing most video formats and DVDs

License:        GPLv3+
URL:            http://www.mplayer2.org/
Source0:        mplayer2-build.tar.xz
#Source1:        mplayer.conf

BuildRequires:  yasm
BuildRequires:  ffmpeg-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel >= 2.0.9
BuildRequires:  libXinerama-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  lirc-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXv-devel
#BuildRequires:  libXvMC-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libXxf86dga-devel
BuildRequires:  aalib-devel
BuildRequires:  libcaca-devel
BuildRequires:  svgalib-devel
BuildRequires:  libmng-devel
BuildRequires:  giflib-devel
BuildRequires:  SDL-devel
BuildRequires:  pulseaudio-lib-devel
BuildRequires:  libbluray-devel
BuildRequires:  libdvdnav-devel
BuildRequires:  cdparanoia-devel
BuildRequires:  libass-devel
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
BuildRequires:  live555-devel
BuildRequires:  libdv-devel >= 0.9.5
BuildRequires:  xvidcore-devel

#BuildRequires:  em8300-devel
#BuildRequires:  fribidi-devel
#BuildRequires:  lame-devel
#BuildRequires:  libjpeg-devel
#BuildRequires:  libmpeg2-devel
#BuildRequires:  lzo-devel >= 2
#BuildRequires:  schroedinger-devel
#BuildRequires:  twolame-devel
#BuildRequires:  x264-devel >= 0.0.0-0.28
#BuildRequires:  libvpx-devel

#This provides mplayer
Provides: mplayer

%description
MPlayer2 is an advanced general-purpose video player.
A fork of the original MPlayer project, it contains
significant further development and supports a number
of features not available in other Unix players, such
as Matroska external chapters.

%prep
%setup -q -n mplayer2-build_0

echo "--prefix=%{_prefix}
--bindir=%{_bindir}
--datadir=%{_datadir}/mplayer2
--mandir=%{_mandir}
--confdir=%{_sysconfdir}/mplayer2
--libdir=%{_libdir}
--codecsdir=%{_libdir}/codecs
--enable-debug=3
--extra-cflags=$RPM_OPT_FLAGS
--enable-radio
--enable-radio-capture
--enable-translation
--charset= utf8
--language-man=all
--enable-runtime-cpudetection
" >> mplayer_options


%build
# mp3lib looks broken => disabling


make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc mplayer/AUTHORS mplayer/Copyright mplayer/LICENSE
%{_bindir}/mplayer
%dir %{_sysconfdir}/mplayer2
#%config(noreplace) %{_sysconfdir}/mplayer2/mplayer.conf
#%config(noreplace) %{_sysconfdir}/mplayer2/input.conf
#%config(noreplace) %{_sysconfdir}/mplayer2/menu.conf
%{_mandir}/man1/mplayer.1*
%lang(cs) %{_mandir}/cs/man1/mplayer.1*
%lang(de) %{_mandir}/de/man1/mplayer.1*
%lang(es) %{_mandir}/es/man1/mplayer.1*
%lang(fr) %{_mandir}/fr/man1/mplayer.1*
%lang(hu) %{_mandir}/hu/man1/mplayer.1*
%lang(it) %{_mandir}/it/man1/mplayer.1*
%lang(pl) %{_mandir}/pl/man1/mplayer.1*
%lang(ru) %{_mandir}/ru/man1/mplayer.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mplayer.1*


%changelog
* Sat Jul 16 2010 Martin Sourada <mso@fedoraproject.org> - 2.0-3
- Move config files as well

* Sat Jul 16 2010 Martin Sourada <mso@fedoraproject.org> - 2.0-2
- Move manual pages to mplayer2.1 to avoid clash with mplayer-common

* Wed Mar 30 2010 Martin Sourada <mso@fedoraproject.org> - 2.0-1
- MPlayer2-2.0 released
- Disable internal mp3lib as it's broken
- Include default config files, set pulse as default audio output
