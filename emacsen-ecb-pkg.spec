# TODO
# - build for xemacs
#
# Conditional build:
%bcond_with	xemacs	# Build without XEmacs support
%bcond_without	emacs	# Build without GNU Emacs support
#
%define		_the_name ecb
Summary:	Emacs Code Browser IDE
Summary(pl.UTF-8):	Środowisko programistyczne dla Emacsa
Name:		emacsen-%{_the_name}-pkg
Version:	2.26
Release:	0.1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://dl.sourceforge.net/ecb/%{_the_name}-%{version}.tar.gz
# Source0-md5:	89bea4c856b96a943e83f14ef650e753
URL:		http://ecb.sourceforge.net/
BuildRequires:	emacsen-cedet-pkg
%if %{with emacs}
BuildRequires:	emacs
%endif
%if %{with xemacs}
BuildRequires:	xemacs
%endif
Requires:	cedet-elisp-code = %{version}-%{release}
Conflicts:	xemacs-cedet-pkg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ECB is a global minor-mode which offers a couple of ECB-windows for
browsing your sources comfortable with the mouse and the keyboard.

This package contains files common to both GNU Emacs and XEmacs.

%description -l pl.UTF-8
ECB jest globalnym minor mode wyświetlającym kilka własnych okienek
ułatwiających przeglądanie kodu myszą i klawiaturą.

Ten pakiet zawiera pliki wspólne dla GNU Emacsa i XEmacsa.

%package emacs
Summary:	ECB compiled elisp files for GNU Emacs
Summary(pl.UTF-8):	Skompilowany kod elisp ECB dla GNU Emacsa
Group:		Applications/Editors/Emacs
Requires:	%{name} = %{version}-%{release}
Provides:	cedet-elisp-code = %{version}-%{release}
%requires_eq emacs

%description emacs
This package contains compiled elisp files needed to run ECB on GNU Emacs

%description emacs -l pl.UTF-8
Pakiet zawiera skompilowane pliki elisp z kodem ECB dla GNU Emacsa.

%package emacs-el
Summary:	ECB elisp files for GNU Emacs
Summary(pl.UTF-8):	Kod elisp ECB dla GNU Emacsa
Group:		Applications/Editors/Emacs
Requires:	%{name}-emacs = %{version}-%{release}

%description emacs-el
This package contains ECB source elisp files for GNU Emacs

%description emacs-el -l pl.UTF-8
Pakiet zawiera źródłowe pliki elisp z kodem ECB dla GNU Emacsa.

%package xemacs
Summary:	ECB elisp files for XEmacs
Summary(pl.UTF-8):	Kod elisp ECB dla XEmacsa
Group:		Applications/Editors/Emacs
Requires:	%{name} = %{version}-%{release}
Provides:	cedet-elisp-code = %{version}-%{release}
%requires_eq xemacs

%description xemacs
This package contains compiled elisp files needed to run ECB on XEmacs

%description xemacs -l pl.UTF-8
Pakiet zawiera skompilowane pliki elisp z kodem ECB dla XEmacsa.

%package xemacs-el
Summary:	ECB elisp source files for XEmacs
Summary(pl.UTF-8):	Kod źródłowy elisp ECB dla XEmacsa
Group:		Applications/Editors/Emacs
Requires:	%{name}-xemacs = %{version}-%{release}

%description xemacs-el
This package contains source ECB elisp files for XEmacs

%description xemacs-el -l pl.UTF-8
Pakiet zawiera pliki źródłowe elisp z kodem ECB dla XEmacsa.

%prep
%setup -q -n %{_the_name}-%{version}

%build
%if %{with xemacs}
mkdir _xemacs
%endif

%if %{with emacs}
mkdir _emacs
cp -a [!_]* _emacs
%{__make} -C _emacs \
	EMACS=emacs \
	CEDET=%{_datadir}/emacs/cedet
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%if %{with xemacs}
%endif

%if %{with emacs}
install -d $RPM_BUILD_ROOT%{_emacs_lispdir}
install _emacs/*.{el,elc} $RPM_BUILD_ROOT%{_emacs_lispdir}
rm _emacs/ecb-images/klaus.sh
cp -a _emacs/ecb-images $RPM_BUILD_ROOT%{_emacs_lispdir}
%endif

install info-help/* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README RELEASE_NOTES html-help
%{_infodir}/*.info*

%if %{with emacs}
%files emacs
%defattr(644,root,root,755)
%{_emacs_lispdir}/*.elc
%{_emacs_lispdir}/ecb-images
%{_emacs_lispdir}/ecb-autoloads.el

%files emacs-el
%defattr(644,root,root,755)
# All except ecb-autoloads.el
%{_emacs_lispdir}/[!e]*.el
%{_emacs_lispdir}/ecb-[!a]*.el
%{_emacs_lispdir}/ecb-autogen.el
%endif

%if %{with xemacs}
%files xemacs
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/lisp/%{_the_name}
%{_datadir}/xemacs-packages/lisp/%{_the_name}/*.elc
%{_datadir}/xemacs-packages/etc/%{_the_name}

%files xemacs-el
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/%{_the_name}/*.el
%endif
