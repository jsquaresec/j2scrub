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
[![Certifications](https://img.shields.io/badge/Verified-Credentials-168BFF?style=for-the-badge&logo=googlechrome&logoColor=white)](https://jsquaresec.github.io/jsquaresec/certifications/)
[![X](https://img.shields.io/badge/X-@j2__sec-111111?style=for-the-badge&logo=x&logoColor=white)](https://x.com/j2_sec?s=11)
[![OTD Studios](https://img.shields.io/badge/Discord-OTD%20Studios-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/nz5jE7PVh7)
[![Evolution Gaming](https://img.shields.io/badge/Discord-Evolution%20Gaming-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/rjf9ZYMARN)
[![Website](https://img.shields.io/badge/Web-onlythedemons.com-168BFF?style=for-the-badge&logo=googlechrome&logoColor=white)](https://onlythedemons.com)

## Certifications & Badges

### Google Cloud

#### Build Infrastructure with Terraform on Google Cloud
**Google Cloud** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/02751b0c-9c07-4a42-91e8-6a54c3a0192b/public_url)

#### Implement DevOps Workflows in Google Cloud
**Google Cloud** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/0f9979bc-d59f-4d16-a80b-356838a44834/public_url)

#### Build a Secure Google Cloud Network
**Google Cloud** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/087862e0-45ad-40e5-acab-1af9485822d5/public_url)

#### Implement Cloud Security Fundamentals on Google Cloud
**Google Cloud** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/3a3a7799-7310-4c39-9ff6-879ae89dd610/public_url)

### Amazon Web Services (AWS)

#### AWS Application Networking Demonstrated
**Amazon Web Services (AWS)** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/46477737-7d9e-41e7-b23b-76c5a598169e/public_url)

#### AWS Incident Response Demonstrated
**Amazon Web Services (AWS)** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/fcfbca6c-7cc7-4de2-9704-a1bdf9d7ed4b/public_url)

### Cisco

#### Ethical Hacking
**Cisco** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/cc6f57d0-015b-40d1-ad02-2afb4c1a37ac/public_url)

#### Cisco Networking
**Cisco** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/5f247425-d38a-4497-bbb6-126668af27fc/public_url)

#### Python Coding 1
**Cisco** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/6b3e909b-45d8-44f4-8a31-c878bcbd7495/public_url)

#### Python Coding 2
**Cisco** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/5c1f2234-ae0a-45de-af49-677dce570e23/public_url)

### AttackIQ

#### Intermediate Purple Teaming
**AttackIQ** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/ff5256c3-e2bc-42cb-a901-9f29d7c5e914)

#### Operationalizing MITRE ATT&CK v19
**AttackIQ** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/95934f21-c54a-4a14-9045-d325fc2e6f2f/public_url)

#### Breach & Attack Simulation
**AttackIQ** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/de4fae36-1f0a-4fad-bd2f-82c23f3fb135/public_url)

#### Foundations of Purple Teaming
**AttackIQ** • Issued September 2026  
[![Verify on Credly](https://img.shields.io/badge/Verify-Credly-168BFF?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/badges/7e67c167-c9f0-42a4-a97a-31d6a2de57ad/public_url)

### Hack The Box

#### That Was A SOCer
**Hack The Box** • September 2026  
[![View Achievement](https://img.shields.io/badge/View-Hack%20The%20Box%20Achievement-9FEF00?style=for-the-badge&logo=hackthebox&logoColor=111111)](https://labs.hackthebox.com/achievement/badge/3945090/243)

#### Investigator In The Making
**Hack The Box** • September 2026  
[![View Achievement](https://img.shields.io/badge/View-Hack%20The%20Box%20Achievement-9FEF00?style=for-the-badge&logo=hackthebox&logoColor=111111)](https://labs.hackthebox.com/achievement/badge/3945090/242)

### Other Credentials

#### Introduction to Cyber Security: Stay Safe Online
**The Open University / OpenLearn** • Issued September 2026  
[![Verify Credential](https://img.shields.io/badge/Verify-Credential-168BFF?style=for-the-badge&logo=openbadges&logoColor=white)](https://www.open.edu/openlearn/badges/badge.php?hash=3f3aaed522c2cc2d8d04c733dabbdee7f154f51e)

---

Created and maintained by **Joshua Jones / jsquaresec**.
