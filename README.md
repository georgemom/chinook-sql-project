# Chinook SQL Project

Analyze a digital music store while learning SQL by writing your own queries.

## What you will answer

1. Where are customers located, and where does revenue come from?
2. Which customers spend the most?
3. Which tracks and artists sell the most?
4. Which invoices are unusually large for their customer?

Your finished work is `REPORT.md`: a short evidence-based business summary with
the SQL that produced each claim. Work through `WORKBOOK.md` in order. Most query
files are intentionally blank apart from the task prompt.

## Use in GitHub Codespaces

1. Extract this ZIP on your computer.
2. Create a new GitHub repository named `chinook-sql-project`. Initialize it
   with a README so it has a branch.
3. On the repository page choose **Add file > Upload files**. Upload the
   extracted files and directories (you may replace GitHub's starter README),
   then commit the upload. Keep `scripts/` and `queries/` intact.
4. Choose **Code > Codespaces > Create codespace on main**. Open its terminal.
5. Run:

   ```bash
   python3 scripts/setup.py
   python3 scripts/run_query.py queries/01_customer_preview.sql
   ```

The setup script downloads the sample Chinook SQLite database to `data/` and
checks its tables. The project uses Python's built-in `sqlite3` module, so it
does not require pip or an extension. If you already have a Chinook database,
you can instead put it at `data/Chinook.sqlite` and run the queries.

## Your daily loop

1. Read one task in `WORKBOOK.md`.
2. Predict the number and meaning of the output rows.
3. Edit the matching file in `queries/`, keeping **one SQL statement per file**.
4. Run `python3 scripts/run_query.py queries/FILE.sql`.
5. Record the query, result, and one sentence of interpretation in `REPORT.md`.
6. Commit your progress using Codespaces Source Control.

If a query errors, check table and column names using:

```bash
python3 scripts/run_query.py queries/00_tables.sql
```

## Notes

- SQL dialect: SQLite. Dates in Chinook are stored in a form SQLite's date
  functions can parse. Table and column names may differ in other Chinook
  versions, so inspect the schema.
- `Invoice.Total` represents an invoice amount; joining Invoice to InvoiceLine
  creates multiple rows per invoice. Do not sum Invoice.Total after that join.
- Source data: https://github.com/lerocha/chinook-database
- Keep your answers in your own repository; `data/` is excluded from Git.
