%global oname   vkBasalt

Name:           vkbasalt
Version:        0.3.2.8
Release:        1
Summary:        Vulkan post processing layer
Group:          System/Libraries
License:        zlib and ASL 2.0
URL:            https://github.com/DadSchoorse/vkBasalt
Source0:        https://github.com/DadSchoorse/vkBasalt/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  glslang
BuildRequires:  pkgconfig(x11)
BuildRequires:  spirv-headers
BuildRequires:  vulkan-headers

Recommends:     goverlay

Provides:       bundled(reshade)

%description
vkBasalt is a Vulkan post processing layer to enhance the visual graphics of
games.

Currently, the build in effects are:

- Contrast Adaptive Sharpening
- Denoised Luma Sharpening
- Fast Approximate Anti-Aliasing
- Enhanced Subpixel Morphological Anti-Aliasing
- 3D color LookUp Table

It is also possible to use Reshade Fx shaders.

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%meson -Dappend_libdir_vkbasalt=true
%meson_build

%install
%meson_install

# Configuration file
install -D -m644 config/%{oname}.conf %{buildroot}%{_sysconfdir}/%{oname}.conf

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{oname}.conf
%{_datadir}/vulkan/implicit_layer.d/%{oname}.json
%{_libdir}/%{name}/
