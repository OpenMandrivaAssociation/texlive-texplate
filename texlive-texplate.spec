%global tl_name texplate
%global tl_revision 71963
%global tl_bin_links texplate:%{_texmfdistdir}/scripts/texplate/texplate.sh

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.6
Release:	%{tl_revision}.1
Summary:	A tool for creating document structures based on templates
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texplate
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texplate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texplate.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texplate.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texplate.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
TeXplate is a tool for creating document structures based on templates.
The application name is a word play on TeX and template, so the purpose
seems quite obvious: we want to provide an easy and straightforward
framework for reducing the typical code boilerplate when writing TeX
documents. Also note that one can easily extrapolate the use beyond
articles and theses: the application is powerful enough to generate any
text-based structure, given that a corresponding template exists.

