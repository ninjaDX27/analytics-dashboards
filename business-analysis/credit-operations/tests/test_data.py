"""Testes determinísticos com biblioteca-padrão. Executar: python tests/test_data.py"""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
db = sqlite3.connect(":memory:")
db.executescript((ROOT / "sql" / "setup.sql").read_text(encoding="utf-8"))

def one(q):
    return db.execute(q).fetchone()[0]

assert one("SELECT COUNT(*) FROM lead") == 40
assert one("SELECT COUNT(DISTINCT lead_id) FROM lead") == 40
assert one("SELECT COUNT(*) FROM channel_spend") == 2
assert one("SELECT SUM(qualified_at IS NOT NULL) FROM lead") == 25
assert one("SELECT SUM(submitted_at IS NOT NULL) FROM lead") == 18
assert one("SELECT SUM(funded_at IS NOT NULL) FROM lead") == 10
assert one("SELECT SUM(contacted_at IS NOT NULL AND (julianday(contacted_at)-julianday(created_at))*24 <= 24.00001) FROM lead") == 32
assert one("SELECT COUNT(*) FROM lead WHERE qualified_at IS NOT NULL AND contacted_at IS NULL") == 0
assert one("SELECT COUNT(*) FROM lead WHERE submitted_at IS NOT NULL AND qualified_at IS NULL") == 0
assert one("SELECT COUNT(*) FROM lead WHERE funded_at IS NOT NULL AND submitted_at IS NULL") == 0
assert one("SELECT COUNT(*) FROM lead WHERE funded_at IS NOT NULL AND status != 'won'") == 0
assert one("SELECT COUNT(*) FROM lead WHERE contacted_at < created_at") == 0

# Validar que o ficheiro CSV reproduz os mesmos 40 registos.
import csv
with (ROOT / "data" / "leads_sinteticas.csv").open(encoding="utf-8", newline="") as f:
    records = list(csv.DictReader(f))
assert len(records) == 40
for r in records:
    x = db.execute(
        "SELECT source, created_at, contacted_at, qualified_at, submitted_at, funded_at, status FROM lead WHERE lead_id=?",
        (int(r["lead_id"]),),
    ).fetchone()
    assert x == tuple(r[k] or None for k in ["source","created_at","contacted_at","qualified_at","submitted_at","funded_at","status"])

# Verificar se as consultas analíticas executam sem falhas.
db.executescript((ROOT / "sql" / "analysis.sql").read_text(encoding="utf-8"))
print("PASS: 40 leads, 25 qualificadas, 18 submetidas, 10 financiadas, SLA 24h=80%; CSV/SQL consistentes.")
