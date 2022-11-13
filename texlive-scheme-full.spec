Name:		texlive-scheme-full
Version:	54074
Release:	1
Summary:	full scheme (everything)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-full.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-bibtexextra
Requires:	texlive-collection-binextra
Requires:	texlive-collection-context
Requires:	texlive-collection-fontsextra
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-formatsextra
Requires:	texlive-collection-fontutils
Requires:	texlive-collection-games
Requires:	texlive-collection-genericextra
Requires:	texlive-collection-genericrecommended
Requires:	texlive-collection-htmlxml
Requires:	texlive-collection-humanities
Requires:	texlive-collection-langafrican
Requires:	texlive-collection-langarabic
Requires:	texlive-collection-langchinese
Requires:	texlive-collection-langcjk
Requires:	texlive-collection-langcyrillic
Requires:	texlive-collection-langczechslovak
Requires:	texlive-collection-langenglish
Requires:	texlive-collection-langeuropean
Requires:	texlive-collection-langfrench
Requires:	texlive-collection-langgerman
Requires:	texlive-collection-langgreek
Requires:	texlive-collection-langindic
Requires:	texlive-collection-langitalian
Requires:	texlive-collection-langjapanese
Requires:	texlive-collection-langkorean
Requires:	texlive-collection-langother
Requires:	texlive-collection-langpolish
Requires:	texlive-collection-langportuguese
Requires:	texlive-collection-langspanish
Requires:	texlive-collection-latex
Requires:	texlive-collection-latexextra
Requires:	texlive-collection-latexrecommended
Requires:	texlive-collection-luatex
Requires:	texlive-collection-mathextra
Requires:	texlive-collection-metapost
Requires:	texlive-collection-music
Requires:	texlive-collection-omega
Requires:	texlive-collection-pictures
Requires:	texlive-collection-plainextra
Requires:	texlive-collection-pstricks
Requires:	texlive-collection-publishers
Requires:	texlive-collection-science
Requires:	texlive-collection-xetex

%description
This is the full TeX Live scheme: it installs everything
available.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
