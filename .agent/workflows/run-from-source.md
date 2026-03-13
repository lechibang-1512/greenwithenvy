---
description: How to run EnvyControl from source
---

# Run EnvyControl from Source

1. Query the current graphics mode (no root required):

```bash
python3 ./envycontrol.py --query
```

2. Switch graphics mode (requires root — **do not run without user confirmation**):

```bash
sudo python3 ./envycontrol.py -s <MODE>
```

Where `<MODE>` is one of: `integrated`, `hybrid`, `nvidia`.

3. Enable verbose output by appending `--verbose`:

```bash
sudo python3 ./envycontrol.py -s hybrid --rtd3 --verbose
```

4. Reboot after switching modes for changes to take effect.
