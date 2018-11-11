Name:     ocaml-dtools

Version:  0.4.1
Release:  0.0%{dist}
Summary:  OCAML daemon tools
License:  GPLv2+
URL:      https://github.com/chambart/ocaml-dtools
Source0:  https://github.com/savonet/ocaml-dtools/releases/download/%{version}/ocaml-dtools-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-pcre-devel
Requires:      ocaml-pcre

%prep
%setup -q 

%build
./configure --prefix=%{_prefix}
make all

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT$(ocamlfind printconf destdir)
install -d $OCAMLFIND_DESTDIR
make install

%files
/usr/lib64/ocaml/dtools/META
/usr/lib64/ocaml/dtools/dtools.a
/usr/lib64/ocaml/dtools/dtools.cma
/usr/lib64/ocaml/dtools/dtools.cmi
/usr/lib64/ocaml/dtools/dtools.cmx
/usr/lib64/ocaml/dtools/dtools.cmxa
/usr/lib64/ocaml/dtools/dtools.mli

%description
OCaml modules for writing daemons

%changelog
* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.1-0.0
- Initial build for pcre-ocaml package bump

* Sat Apr 15 2017 Lucas Bickel <hairmare@rabe.ch> - 0.3.4-1
- Bump to next version

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.3.0-1
- initial version
