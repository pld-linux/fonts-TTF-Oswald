Summary:	The Oswald family of fonts
Name:		fonts-TTF-Oswald
Version:	3.0
Release:	1
License:	OFL
Group:		Fonts
Source0:	OswaldFont-%{version}.zip
# Source0-md5:	128e5acbc4e5bad45588031b0505da3c
URL:		https://github.com/vernnobile/OswaldFont
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Oswald is a reworking of the classic gothic typeface style
historically represented by designs such as 'Franklyn Gothic',
'Alternate Gothic', 'News Gothic' and more. The characters of Oswald
have been re-drawn and reformed to better fit the pixel grid of
standard digital screens. Oswald is designed to be used freely across
the internet by web browsers on desktop computers, laptops and mobile
devices.

%prep
%setup -q -n OswaldFont-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

cp -p */*/*.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/Oswald*.ttf
