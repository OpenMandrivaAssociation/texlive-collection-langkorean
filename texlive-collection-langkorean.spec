%global tl_name collection-langkorean
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Korean
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langkorean
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langkorean.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(baekmuk)
Requires:	texlive(cjk-ko)
Requires:	texlive(collection-langcjk)
Requires:	texlive(kotex-oblivoir)
Requires:	texlive(kotex-plain)
Requires:	texlive(kotex-utf)
Requires:	texlive(kotex-utils)
Requires:	texlive(lshort-korean)
Requires:	texlive(nanumtype1)
Requires:	texlive(pmhanguljamo)
Requires:	texlive(uhc)
Requires:	texlive(unfonts-core)
Requires:	texlive(unfonts-extra)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Korean; additional packages in collection-langcjk.

