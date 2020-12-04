%define debug_package %{nil}


Name:     ocaml-dtools
Version:  0.4.2
Release:  0.1%{dist}
Summary:  OCAML daemon tools

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-dtools
Source0:  https://github.com/savonet/ocaml-dtools/archive/%{version}.tar.gz?#%{name}-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-dune
Requires:      ocaml-pcre


%description
OCaml modules for writing daemons


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
dune build

%install
dune install \
  --prefix %{buildroot} \
  --libdir %{buildroot}$(ocamlfind printconf destdir)
rm -rf %{buildroot}/doc

%files
%doc README.md CHANGES
%license COPYING
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Thu Dec 3 2020 Lucas Bickel <hairmare@rabe.ch> - 0.4.2-0.1
- Bump to 0.4.2

* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.1-0.3
- Finish cleanup and add seperate -devel subpackage

* Fri Nov 23 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.1-0.2
- Start cleaning up files section
- Stomp a Tumbleweed bug

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.1-0.1
- Fix Fedora build

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.1-0.0
- Initial build for pcre-ocaml package bump

* Sat Apr 15 2017 Lucas Bickel <hairmare@rabe.ch> - 0.3.4-1
- Bump to next version

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.3.0-1
- initial version
