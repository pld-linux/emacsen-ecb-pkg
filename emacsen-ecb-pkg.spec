# TODO: build for xemacs
#
# Conditional build:
%bcond_with	xemacs	# Build without XEmacs support
%bcond_without	emacs	# Build without GNU Emacs support
#
%define		_the_name ecb
Summary:	Emacs Code Browser IDE
Summary(pl):	¦rodowisko programistyczne dla Emacsa
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

%description -l pl
ECB jest globalnym minor mode wy¶wietlaj±cym kilka w³asnych okienek
u³atwiaj±cych przegl±danie kodu mysz± i klawiatur±.

Ten pakiet zawiera pliki wspólne dla GNU Emacsa i XEmacsa.

%define version_of() %{expand:%%(rpm -q %1 --queryformat '%%%%{version}-%%%%{release}')}

%package emacs
Summary:	ECB compiled elisp files for GNU Emacs
Summary(pl):	Skompilowany kod elisp ECB dla GNU Emacsa
Group:		Applications/Editors/Emacs
Requires:	%{name} = %{version}-%{release}
Requires:	emacs = %{version_of emacs}
Provides:	cedet-elisp-code = %{version}-%{release}

%description emacs
This package contains compiled elisp files needed to run ECB on GNU Emacs

%description emacs -l pl
Pakiet zawiera skompilowane pliki elisp z kodem ECB dla GNU Emacsa.

%package emacs-el
Summary:	ECB elisp files for GNU Emacs
Summary(pl):	Kod elisp ECB dla GNU Emacsa
Group:		Applications/Editors/Emacs
Requires:	%{name}-emacs = %{version}-%{release}

%description emacs-el
This package contains ECB source elisp files for GNU Emacs

%description emacs-el -l pl
Pakiet zawiera ¼ród³owe pliki elisp z kodem ECB dla GNU Emacsa.

%package xemacs
Summary:	ECB elisp files for XEmacs
Summary(pl):	Kod elisp ECB dla XEmacsa
Group:		Applications/Editors/Emacs
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs = %{version_of xemacs}
Provides:	cedet-elisp-code = %{version}-%{release}

%description xemacs
This package contains compiled elisp files needed to run ECB on XEmacs

%description xemacs -l pl
Pakiet zawiera skompilowane pliki elisp z kodem ECB dla XEmacsa.

%package xemacs-el
Summary:	ECB elisp source files for XEmacs
Summary(pl):	Kod ¼ród³owy elisp ECB dla XEmacsa
Group:		Applications/Editors/Emacs
Requires:	%{name}-xemacs = %{version}-%{release}

%description xemacs-el
This package contains source ECB elisp files for XEmacs

%description xemacs-el -l pl
Pakiet zawiera pliki ¼ród³owe elisp z kodem ECB dla XEmacsa.

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
