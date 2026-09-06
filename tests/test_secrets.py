from pathlib import Path
from j2scrub.scrub.secrets import scan_text_file

def test_detects_generic_secret(tmp_path: Path):
    p = tmp_path / ".env"
    p.write_text("API_KEY=supersecretvalue123", encoding="utf-8")
    report = scan_text_file(p)
    assert any(f.kind == "generic_secret" for f in report.findings)
