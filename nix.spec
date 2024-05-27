Name:           nix
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            
Source0:        
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
