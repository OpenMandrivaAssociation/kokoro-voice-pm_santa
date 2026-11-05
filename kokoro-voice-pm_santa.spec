Name:		kokoro-voice-pm_santa
Version:	1.0
Release:	1
Summary:	Brazilian Portuguese male Kokoro voice pm_santa
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-pt
Provides:	kokoro-voice-pt_BR
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/pm_santa.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Pronunciation uses espeak-ng.
Select it with: kokoro -m pm_santa

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/pm_santa.pt

%files
%{_datadir}/kokoro/voices/pm_santa.pt
