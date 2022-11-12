Name:		texlive-collection-langkorean
Version:	54074
Release:	1
Summary:	Korean
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langkorean.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-langcjk
Requires:	texlive-cjk-ko
Requires:	texlive-kotex-oblivoir
Requires:	texlive-kotex-plain
Requires:	texlive-kotex-utf
Requires:	texlive-kotex-utils
Requires:	texlive-lshort-korean
Requires:	texlive-nanumtype1
Requires:	texlive-uhc

%description
Support for Korean; additional packages in collection-langcjk.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
