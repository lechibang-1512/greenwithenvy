---
description: How to revert all changes made by EnvyControl
---

# Reset / Revert EnvyControl Changes

1. Revert all configuration changes and delete the cache:

```bash
sudo python3 ./envycontrol.py --reset
```

This removes all generated config files (blacklists, udev rules, xorg.conf, modprobe configs) and rebuilds the initramfs.

2. If only the SDDM Xsetup file needs to be restored:

```bash
sudo python3 ./envycontrol.py --reset-sddm
```

3. Files that may need manual removal if uninstalling:

- `/var/cache/envycontrol`
- `/etc/modprobe.d/blacklist-nvidia.conf`
- `/etc/udev/rules.d/50-remove-nvidia.rules`
- `/etc/udev/rules.d/80-nvidia-pm.rules`
- `/etc/X11/xorg.conf`
- `/etc/X11/xorg.conf.d/10-nvidia.conf`
- `/etc/modprobe.d/nvidia.conf`
