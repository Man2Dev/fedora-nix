# SPDX-License-Identifier: GPL-3.0-or-later
Name:           nix
Version:        2.22.1
Release:        1%{?dist}
Summary:        Nix package manager

License:        LGPL-2.1 AND GPL-3.0-or-later.txt
URL:            https://releases.nixos.org
Source0:        %{url}/%{name}/%{name}-%{version}/%{name}-%{version}-x86_64-linux.tar.xz
Source1:        %{url}/%{name}/%{name}-%{version}/%{name}-%{version}-aarch64-linux.tar.xz
source2:	https://github.com/NixOS/nix/archive/2.22.1.tar.gz#/nix-2.22.1.tar.gz
Source3:        GPL-3.0-or-later.txt

ExclusiveArch:  x86_64 aarch64

BuildRequires:  tar
BuildRequires:  xz
Requires:

%description


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Mon May 27 2024 Mohammadreza Hendiani <man2dev@fedoraproject.org>
- 
