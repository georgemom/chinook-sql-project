"""Run one SELECT statement from a .sql file against Chinook SQLite."""
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "Chinook.sqlite"


def print_rows(cursor, limit=30):
    headers = [col[0] for col in cursor.description]
    rows = cursor.fetchmany(limit + 1)
    shown = rows[:limit]
    widths = [min(35, max(len(str(h)), *(len(str(r[i] if r[i] is not None else "NULL"))
                                       for r in shown))) for i, h in enumerate(headers)]
    def line(vals):
        return " | ".join(str(x if x is not None else "NULL")[:w].ljust(w)
                          for x, w in zip(vals, widths))
    print(line(headers))
    print("-+-".join("-" * w for w in widths))
    for row in shown:
        print(line(row))
    if len(rows) > limit:
        print(f"... showing first {limit} rows")
    else:
        print(f"{len(shown)} row(s)")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/run_query.py queries/FILE.sql")
        raise SystemExit(2)
    query_file = Path(sys.argv[1])
    if not query_file.is_file():
        print(f"Query file not found: {query_file}")
        raise SystemExit(2)
    if not DB.is_file():
        print("Database missing. Run: python3 scripts/setup.py")
        raise SystemExit(2)
    sql = query_file.read_text(encoding="utf-8").strip()
    if not sql or all(not line.strip() or line.lstrip().startswith("--")
                      for line in sql.splitlines()):
        print(f"Add your SELECT query to {query_file}, then run it again.")
        raise SystemExit(2)
    try:
        with sqlite3.connect(f"file:{DB}?mode=ro", uri=True) as con:
            cursor = con.execute(sql)
            if cursor.description is None:
                print("Query ran; no result columns.")
            else:
                print_rows(cursor)
    except sqlite3.Error as exc:
        print(f"SQL error: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
