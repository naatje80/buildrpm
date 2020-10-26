Name:           gstreamer1-plugins-bad-nonfree
Version:        1.16.1
Release:        3%{?dist}
Summary:        GStreamer streaming media framework "bad" plugins

License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/
Source0:		http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz

BuildRequires:  python38
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains nonfree plug-ins that aren't tested well enough, or the code
is not of good enough quality.

%prep
%setup -q -n gst-plugins-bad-%{version}


%build
%configure --disable-silent-rules --disable-fatal-warnings \
	--with-package-name="GStreamer-plugins-bad-free package" \
	--with-package-origin="https://nm8.repo.xs4all.nl" \
	--disable-accurip --disable-adpcmdec --disable-adpcmenc \
	--disable-aiff --disable-videoframe_audiolevel --disable-asfmux \
	--disable-audiofxbad --disable-audiomixer --disable-compositor \
	--disable-audiovisualizers --disable-autoconvert --disable-bayer \
	--disable-camerabin2 --disable-cdxaparse --disable-coloreffects \
	--disable-dataurisrc --disable-dccp --disable-debugutils \
	--disable-dvbsuboverlay --disable-faceoverlay --disable-static \
	--disable-festival --disable-fieldanalysis --disable-freeverb \
	--disable-frei0r --disable-gaudieffects --disable-geometrictransform \
	--disable-gdp --disable-hdvparse --disable-id3tag --disable-inter \
	--disable-interlace --disable-ivfparse --disable-ivtc \
	--disable-jp2kdecimator --disable-jpegformat --disable-librfb \
	--disable-midi --disable-mpegdemux --disable-mpegtsdemux \
	--disable-mpegtsmux --disable-mpegpsmux --disable-mve --disable-mxf \
	--disable-netsim --disable-nuvdemux --disable-onvif --disable-patchdetect \
	--disable-pcapparse --disable-pnm --disable-rawparse --disable-removesilence \
	--disable-sdi --disable-sdp --disable-segmentclip --disable-siren \
	--disable-smooth --disable-speed --disable-subenc --disable-stereo \
	--disable-timecode --disable-tta --disable-videofilters --disable-videomeasure \
	--disable-videoparsers --disable-videosignal --disable-vmnc --disable-y4m \
	--disable-yadif --disable-directsound --disable-wasapi --disable-direct3d \
	--disable-winscreencap --disable-winks --disable-android_media \
	--disable-apple_media --disable-bluez --disable-avc --disable-shm --disable-vcd \
	--disable-opensles --disable-uvch264 --disable-nvenc --disable-tinyalsa \
	--disable-assrender --disable-voamrwbenc --disable-voaacenc --disable-apexsink \
	--disable-bs2b --disable-bz2 --disable-chromaprint --disable-curl --disable-dash \
	--disable-dc1394 --disable-directfb --disable-wayland --disable-webp \
	--disable-daala --disable-dts --disable-resindvd --disable-faac --disable-faad \
	--disable-fbdev --disable-fdk_aac --disable-flite --disable-gsm --disable-fluidsynth \
	--disable-kate --disable-kms --disable-ladspa --disable-lv2 --disable-libde265 \
	--disable-libmms --disable-srtp --disable-dtls --disable-linsys --disable-modplug \
	--disable-mimic --disable-mpeg2enc --disable-mplex --disable-musepack --disable-nas \
	--disable-neon --disable-ofa --disable-openal --disable-opencv --disable-openexr \
	--disable-openh264 --disable-openjpeg --disable-openni2 --disable-opus --disable-pvr \
	--disable-rsvg --disable-gl --disable-gtk3 --disable-qt --disable-vulkan \
	--disable-libvisual --disable-timidity --disable-teletextdec --disable-wildmidi \
	--disable-sdl --disable-sdltest --disable-smoothstreaming --disable-sndfile \
	--disable-soundtouch --disable-spc --disable-gme --disable-xvid --disable-dvb \
	--disable-wininet --disable-acm --disable-vdpau --disable-sbc --disable-schro \
	--disable-zbar --disable-rtmp --disable-spandsp --disable-sndio --disable-hls \
	--enable-gtk-doc-html=no --disable-x265 --disable-webrtcdsp --disable-decklink \
	--enable-dvdspu
make %{?_smp_mflags}

%install
install ./gst/dvdspu/.libs/libgstdvdspu.so -D $RPM_BUILD_ROOT/%{_libdir}/gstreamer-1.0/libgstdvdspu.so -m 644

%files
%doc

%changelog

