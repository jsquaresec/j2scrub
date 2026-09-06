# Contributing to J2Scrub

Thanks for helping improve J2Scrub.

## Ground rules

- Keep cleanup behavior explicit and reviewable.
- Destructive behavior must never become the default.
- New Burn modules must support previewing the target first.
- New Scrub modules should create sanitized copies instead of altering originals.
- Do not add telemetry or mandatory cloud services.
- Add or update tests when behavior changes.

## Development

```bash
python -m pip install -e '.[dev]'
pytest
```

For large changes, open an issue first so the design can be discussed before implementation.
