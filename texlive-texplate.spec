Name:		texlive-texplate
Version:	61719
Release:	1
Summary:	A tool for creating document structures based on templates
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texplate
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texplate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texplate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texplate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXplate is a tool for creating document structures based on
templates. The application name is a word play on TeX and
template, so the purpose seems quite obvious: we want to
provide an easy and straightforward framework for reducing the
typical code boilerplate when writing TeX documents. Also note
that one can easily extrapolate the use beyond articles and
theses: the application is powerful enough to generate any
text-based structure, given that a corresponding template
exists.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/support/texplate
%doc %{_texmfdistdir}/texmf-dist/source/support/texplate/main/resources/org/islandoftex/texplate
%doc %{_texmfdistdir}/texmf-dist/source/support/texplate/main/kotlin/org/islandoftex/texplate
%{_texmfdistdir}/texmf-dist/scripts/texplate
%doc %{_texmfdistdir}/texmf-dist/doc/support/texplate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
