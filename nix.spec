Name:           nix
Version:        2.22.1
Release:        1%{?dist}
Summary:        Nix package manager

License:        
URL:            https://releases.nixos.org/nix/nix-2.22.1/nix-2.22.1-x86_64-linux.tar.xz
Source0:        %{name}-%{version}-x86_64-linux.tar.xz
Source1: 	GPL-3.0-or-later.txt

BuildRequires:  
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
