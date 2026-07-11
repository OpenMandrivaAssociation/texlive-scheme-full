%global tl_name scheme-full
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	full scheme (everything)
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-full
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-full.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(collection-basic)
Requires:	texlive(collection-bibtexextra)
Requires:	texlive(collection-binextra)
Requires:	texlive(collection-context)
Requires:	texlive(collection-fontsextra)
Requires:	texlive(collection-fontsrecommended)
Requires:	texlive(collection-fontutils)
Requires:	texlive(collection-formatsextra)
Requires:	texlive(collection-games)
Requires:	texlive(collection-humanities)
Requires:	texlive(collection-langarabic)
Requires:	texlive(collection-langchinese)
Requires:	texlive(collection-langcjk)
Requires:	texlive(collection-langcyrillic)
Requires:	texlive(collection-langczechslovak)
Requires:	texlive(collection-langenglish)
Requires:	texlive(collection-langeuropean)
Requires:	texlive(collection-langfrench)
Requires:	texlive(collection-langgerman)
Requires:	texlive(collection-langgreek)
Requires:	texlive(collection-langitalian)
Requires:	texlive(collection-langjapanese)
Requires:	texlive(collection-langkorean)
Requires:	texlive(collection-langother)
Requires:	texlive(collection-langpolish)
Requires:	texlive(collection-langportuguese)
Requires:	texlive(collection-langspanish)
Requires:	texlive(collection-latex)
Requires:	texlive(collection-latexextra)
Requires:	texlive(collection-latexrecommended)
Requires:	texlive(collection-luatex)
Requires:	texlive(collection-mathscience)
Requires:	texlive(collection-metapost)
Requires:	texlive(collection-music)
Requires:	texlive(collection-pictures)
Requires:	texlive(collection-plaingeneric)
Requires:	texlive(collection-pstricks)
Requires:	texlive(collection-publishers)
Requires:	texlive(collection-texworks)
Requires:	texlive(collection-xetex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the full TeX Live scheme: it installs everything available.

