"""Download and validate the official Chinook SQLite sample database."""
from pathlib import Path
import sqlite3
import sys
from urllib.request import urlopen, Request

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "Chinook.sqlite"
URL = (
    "https://raw.githubusercontent.com/lerocha/chinook-database/master/"
    "ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
)
REQUIRED = {"Customer", "Invoice", "InvoiceLine", "Track", "Album", "Artist"}


def validate(path):
    if path.read_bytes()[:16] != b"SQLite format 3\x00":
        raise ValueError("Downloaded file is not a SQLite database")
    with sqlite3.connect(f"file:{path}?mode=ro", uri=True) as con:
        tables = {row[0] for row in con.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'")}
        missing = REQUIRED - tables
        if missing:
            raise ValueError(f"Missing expected tables: {sorted(missing)}")
        n = con.execute("SELECT COUNT(*) FROM Customer").fetchone()[0]
    print(f"Ready: {path} ({n} customers)")


def main():
    DB.parent.mkdir(parents=True, exist_ok=True)
    if DB.exists():
        validate(DB)
        return
    temp = DB.with_suffix(".download")
    try:
        req = Request(URL, headers={"User-Agent": "Chinook-SQL-Learning-Project"})
        with urlopen(req, timeout=45) as response, temp.open("wb") as stream:
            while block := response.read(1024 * 1024):
                stream.write(block)
        validate(temp)
        temp.replace(DB)
        print("Database installed. Try queries/01_customer_preview.sql next.")
    except Exception as exc:
        temp.unlink(missing_ok=True)
        print(f"Setup failed: {exc}", file=sys.stderr)
        print("Download Chinook_Sqlite.sqlite from the project URL in README.md, "
              "save it as data/Chinook.sqlite, and run setup again.", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
