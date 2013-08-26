# revision 21417
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-full
Version:	20120307
Release:	2
Summary:	full scheme (everything)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-full.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-bibtexextra
Requires:	texlive-collection-binextra
Requires:	texlive-collection-context
Requires:	texlive-collection-documentation-arabic
Requires:	texlive-collection-documentation-base
Requires:	texlive-collection-documentation-bulgarian
Requires:	texlive-collection-documentation-chinese
Requires:	texlive-collection-documentation-czechslovak
Requires:	texlive-collection-documentation-dutch
Requires:	texlive-collection-documentation-english
Requires:	texlive-collection-documentation-finnish
Requires:	texlive-collection-documentation-french
Requires:	texlive-collection-documentation-german
Requires:	texlive-collection-documentation-italian
Requires:	texlive-collection-documentation-japanese
Requires:	texlive-collection-documentation-korean
Requires:	texlive-collection-documentation-mongolian
Requires:	texlive-collection-documentation-polish
Requires:	texlive-collection-documentation-portuguese
Requires:	texlive-collection-documentation-russian
Requires:	texlive-collection-documentation-serbian
Requires:	texlive-collection-documentation-slovenian
Requires:	texlive-collection-documentation-spanish
Requires:	texlive-collection-documentation-thai
Requires:	texlive-collection-documentation-turkish
Requires:	texlive-collection-documentation-ukrainian
Requires:	texlive-collection-documentation-vietnamese
Requires:	texlive-collection-fontsextra
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-fontutils
Requires:	texlive-collection-formatsextra
Requires:	texlive-collection-games
Requires:	texlive-collection-genericextra
Requires:	texlive-collection-genericrecommended
Requires:	texlive-collection-htmlxml
Requires:	texlive-collection-humanities
Requires:	texlive-collection-langafrican
Requires:	texlive-collection-langarabic
Requires:	texlive-collection-langarmenian
Requires:	texlive-collection-langcjk
Requires:	texlive-collection-langcroatian
Requires:	texlive-collection-langcyrillic
Requires:	texlive-collection-langczechslovak
Requires:	texlive-collection-langdanish
Requires:	texlive-collection-langdutch
Requires:	texlive-collection-langfinnish
Requires:	texlive-collection-langfrench
Requires:	texlive-collection-langgerman
Requires:	texlive-collection-langgreek
Requires:	texlive-collection-langhebrew
Requires:	texlive-collection-langhungarian
Requires:	texlive-collection-langindic
Requires:	texlive-collection-langitalian
Requires:	texlive-collection-langlatin
Requires:	texlive-collection-langlatvian
Requires:	texlive-collection-langlithuanian
Requires:	texlive-collection-langmongolian
Requires:	texlive-collection-langnorwegian
Requires:	texlive-collection-langother
Requires:	texlive-collection-langpolish
Requires:	texlive-collection-langportuguese
Requires:	texlive-collection-langspanish
Requires:	texlive-collection-langswedish
Requires:	texlive-collection-langtibetan
Requires:	texlive-collection-langturkmen
Requires:	texlive-collection-langenglish
Requires:	texlive-collection-langvietnamese
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
Requires:	texlive-collection-texinfo
Requires:	texlive-collection-xetex

%description
This is the full TeX Live scheme: it installs everything
available.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120307-1
+ Revision: 783110
- Import texlive-scheme-full
- Import texlive-scheme-full

