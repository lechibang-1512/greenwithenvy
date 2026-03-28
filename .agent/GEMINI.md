# EnvyControl — Agent Context

## Project Overview

**EnvyControl** is a CLI tool (Python 3) that provides an easy way to switch between GPU modes on **Nvidia Optimus** laptops (hybrid Intel/AMD + Nvidia graphics) under Linux. It is a single-file Python application (`envycontrol.py`) distributed as a pip-installable package.

- **Version**: 3.5.2
- **License**: MIT
- **Author**: Victor Bayas (bayasdev)
- **Repository**: https://github.com/bayasdev/envycontrol

## Architecture

This is a **single-module** Python project. All logic resides in `envycontrol.py`.

### Key Files

| File | Purpose |
|---|---|
| `envycontrol.py` | Entire application — CLI parsing, GPU mode switching, config file management, caching |
| `setup.py` | Package definition (setuptools), registers `envycontrol` console entry point |
| `flake.nix` | Nix Flake for NixOS packaging and dev shell |
| `.envrc` | direnv configuration |
| `LICENSE` | MIT license |
| `README.md` | User-facing documentation |

### Graphics Modes

EnvyControl supports three GPU modes:

1. **`integrated`** — Uses only the Intel/AMD iGPU; Nvidia dGPU is powered off via udev rules and kernel module blacklisting.
2. **`hybrid`** — PRIME render offloading; optional RTD3 power management for Turing+ GPUs.
3. **`nvidia`** — Dedicated Nvidia dGPU only; generates X.org config, supports ForceCompositionPipeline and Coolbits.

### Core Functions

- `graphics_mode_switcher()` — Main dispatcher that delegates to per-mode helpers based on the target mode.
- `_switch_integrated()` — Handles switching to integrated mode (blacklists Nvidia, sets udev rules).
- `_switch_hybrid()` — Handles switching to hybrid mode (enables modeset, optional RTD3).
- `_switch_nvidia()` — Handles switching to nvidia mode (generates X.org config, sets up display manager).
- `_run_cmd()` — Subprocess runner that suppresses output unless verbose mode is on.
- `_manage_persistenced()` — Enables/disables the `nvidia-persistenced` systemd service.
- `cleanup()` — Removes all EnvyControl-generated config files and restores backups.
- `_parse_gpu_devices()` — Parses `lspci -Dnn` output to detect all GPUs using PCI vendor/device IDs and class codes.
- `get_nvidia_gpu_pci_bus()` — Finds Nvidia GPU by vendor ID `10de`, returns BusID in `PCI:bus:dev:fn` format.
- `get_igpu_vendor()` — Finds iGPU by vendor ID (`8086`=Intel, `1002`=AMD, `17cb`=Qualcomm), explicitly skipping Nvidia.
- `get_amd_igpu_name()` — Detects AMD iGPU provider name from `xrandr --listproviders`.
- `get_display_manager()` — Auto-detects the active display manager from systemd.
- `rebuild_initramfs()` — Rebuilds initramfs using the distro-appropriate tool.
- `create_file()` — Writes config files to the filesystem, creating parent dirs as needed.
- `CachedConfig` — Class that manages a JSON cache (`/var/cache/envycontrol/cache.json`) of the Nvidia PCI bus ID. Provides a `get_pci_bus_getter()` method for dependency injection instead of monkey-patching globals.
- `get_current_mode()` — Detects the current mode by checking for the presence of generated config files.

### Config Files Managed

- `/etc/modprobe.d/blacklist-nvidia.conf` — Nvidia module blacklist (integrated mode)
- `/etc/udev/rules.d/50-remove-nvidia.rules` — udev rules to power off dGPU (integrated mode)
- `/etc/udev/rules.d/80-nvidia-pm.rules` — RTD3 power management rules (hybrid mode)
- `/etc/X11/xorg.conf` — X.org server layout (nvidia mode)
- `/etc/X11/xorg.conf.d/10-nvidia.conf` — Extra X.org OutputClass config (nvidia mode)
- `/etc/modprobe.d/nvidia.conf` — Nvidia driver modeset options
- `/var/cache/envycontrol/cache.json` — PCI bus ID cache

### Supported Display Managers

GDM (`gdm`/`gdm3`), SDDM (`sddm`), LightDM (`lightdm`).

### Supported Distros (for initramfs rebuild)

Debian/Ubuntu, RHEL/Fedora/SUSE, Arch, EndeavourOS (dracut), ALT Linux, NixOS, and OSTree-based (Silverblue, Kinoite, Bazzite).

## Development Guidelines

- **Python version**: 3+ (no external dependencies beyond the standard library)
- **No tests exist** in the repository — changes should be verified manually
- **Root required**: Most operations (`--switch`, `--reset`, `--reset-sddm`) require root privileges
- **Single-file codebase**: All changes go into `envycontrol.py`
- **Config templates are string constants**: Defined at the top of `envycontrol.py` (e.g., `BLACKLIST_CONTENT`, `XORG_INTEL`, `UDEV_INTEGRATED`)
- **Initramfs rebuild**: Always triggered after mode switches to ensure kernel modules are correctly loaded on next boot

## Common Tasks

- **Adding a new GPU mode option**: Add the flag to `argparse` in `main()`, then handle it in `graphics_mode_switcher()`.
- **Supporting a new display manager**: Add to `SUPPORTED_DISPLAY_MANAGERS`, implement setup logic in the `nvidia` branch of `graphics_mode_switcher()`.
- **Supporting a new distro's initramfs**: Add detection logic in `rebuild_initramfs()`.
- **Modifying config file templates**: Edit the corresponding string constant at the top of `envycontrol.py`.
