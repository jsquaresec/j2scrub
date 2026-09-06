# J2Scrub

**Sanitize what you share. Burn what you leave behind.**

J2Scrub is an open-source, offline-first privacy utility for security professionals, developers, researchers, and anyone who wants tighter control over the traces they share or leave on their own machine.

It has two jobs:

- **Scrub** creates cleaner copies of files and directories before you share them.
- **Burn** previews and removes selected local traces such as shell history, temporary files, thumbnails, recent-item data, and clipboard contents.

J2Scrub does not upload your files, require an account, or depend on a hosted scanning service.

## Status

J2Scrub is currently **v0.1 alpha**. The CLI foundation is usable, but the project is intentionally conservative while more sanitizers and cleanup modules are added.

## Features

### Scrub

- Scan source trees and common text/config formats for exposed secrets
- Detect API-key/token/password-style assignments
- Detect private keys, GitHub-style tokens, JWTs, email addresses, and IPv4 addresses
- Inspect common image formats for EXIF metadata
- Create metadata-stripped image copies
- Preserve originals by default
- Recursively create sanitized directory copies

### Burn

- Dry-run is the default
- Preview cleanup targets before anything is removed
- Shell-history cleanup on supported platforms
- Temporary-directory cleanup
- Thumbnail/cache cleanup targets
- Recent-items cleanup targets on Windows
- Clipboard clearing when a supported local command is available
- Requires `--apply` before destructive cleanup runs

## Install

```bash
python -m pip install -e .
```

For development:

```bash
python -m pip install -e '.[dev]'
pytest
```

## Usage

Scan a file or directory:

```bash
j2scrub scan ./project
```

Create a sanitized copy:

```bash
j2scrub scrub screenshot.jpg
j2scrub scrub ./incident-notes --output ./incident-notes-clean
```

Preview local cleanup targets:

```bash
j2scrub burn
```

Apply the displayed cleanup actions:

```bash
j2scrub burn --apply
```

## Safety model

J2Scrub is designed around predictable behavior:

1. **Originals stay untouched by Scrub.** Sanitization creates a new copy.
2. **Burn previews first.** Cleanup is a dry run unless `--apply` is explicitly passed.
3. **Targets are visible.** Burn reports what it intends to clean.
4. **Local-first.** J2Scrub does not need to transmit your files to a third party.
5. **No “wipe everything” logic.** Cleanup modules target defined user-owned artifacts instead of deleting arbitrary system paths.

Before using Burn on important systems, review its output and keep appropriate backups.

## Roadmap

- Rich terminal output and JSON reports
- Office/PDF metadata inspection and sanitization
- Archive inspection and safe rebuilds
- Configurable redaction rules for logs and source trees
- Browser-specific cleanup modules
- Application cleanup plugins
- Cleanup profiles
- Windows Explorer and Linux file-manager integration
- Desktop GUI
- Signed release binaries

## Contributing

J2Scrub is intentionally modular. New scrubbers and burn targets should be small, testable, and explicit about what they inspect or modify.

Please open an issue before large architectural changes. Pull requests should include tests for new cleanup or detection behavior.

## Privacy

J2Scrub is intended to run locally. The project does not include telemetry or a cloud dependency.

## License

MIT License. See [LICENSE](LICENSE).

## Links

[![GitHub](https://img.shields.io/badge/GitHub-jsquaresec-111111?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jsquaresec)
[![X](https://img.shields.io/badge/X-@j2__sec-111111?style=for-the-badge&logo=x&logoColor=white)](https://x.com/j2_sec?s=11)
[![OTD Studios](https://img.shields.io/badge/Discord-OTD%20Studios-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/nz5jE7PVh7)
[![Evolution Gaming](https://img.shields.io/badge/Discord-Evolution%20Gaming-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/rjf9ZYMARN)
[![Website](https://img.shields.io/badge/Web-onlythedemons.com-168BFF?style=for-the-badge&logo=googlechrome&logoColor=white)](https://onlythedemons.com)

## Certifications & Badges

### Introduction to Cyber Security: Stay Safe Online
**The Open University / OpenLearn** • Issued September 2026  
[![Verify Credential](https://img.shields.io/badge/Verify-Credential-168BFF?style=for-the-badge&logo=openbadges&logoColor=white)](https://www.open.edu/openlearn/badges/badge.php?hash=3f3aaed522c2cc2d8d04c733dabbdee7f154f51e)

### Cisco Networking
**Cisco** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/5f247425-d38a-4497-bbb6-126668af27fc/public_url)

### Python Coding 1
**Cisco** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/6b3e909b-45d8-44f4-8a31-c878bcbd7495/public_url)

---

Created and maintained by **Joshua Jones / jsquaresec**.
