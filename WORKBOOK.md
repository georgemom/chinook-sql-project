# Project workbook: music store analysis

Use the `queries/` files in order. Each stage introduces one new idea while
reusing earlier ones. These are questions for you to solve, so the starter
package does not contain an answer key. Use your SQL study guide when needed.

## Stage 1 - Explore the data (SELECT, aliases, ORDER BY)

**Task 1.** Run `01_customer_preview.sql`. Confirm that one row represents one
customer. Change the sort to `Country`, then `LastName`.

**Task 2.** In `02_customers_by_country.sql`, count customers per country and
sort from most to fewest. Name the count `CustomerCount`.

Check: each result row is a country. `COUNT(*)` counts customers, not invoices.
Write down the top three countries and explain what was counted.

## Stage 2 - Filter and classify (WHERE, IN, BETWEEN, CASE)

**Task 3.** In `03_invoices.sql`, list InvoiceId, InvoiceDate, CustomerId, and
Total for invoices with Total between 5 and 10 inclusive. Sort largest first.

**Task 4.** Add a CASE label to the same query: `Low` for Total < 5, `Medium`
for 5 <= Total < 10, and `High` for Total >= 10. To see all three labels,
remove the BETWEEN filter after you test it.

Check: the CASE order controls which label is chosen. State whether a Total of
exactly 10 is Medium or High.

## Stage 3 - Revenue summaries (aggregates, GROUP BY, HAVING)

**Task 5.** In `04_revenue_by_country.sql`, use **Invoice.BillingCountry** to
count invoices and sum Total by billing country. Sort by revenue descending.
Round revenue to two decimals for display.

**Task 6.** Add a HAVING condition that keeps only countries with at least five
invoices. Explain why this condition belongs after GROUP BY.

Check: a country is one output row; the sum is over its invoice rows. Customer
count and invoice count are different quantities.

## Stage 4 - Connect customers and purchases (INNER JOIN, LEFT JOIN)

**Task 7.** In `05_top_customers.sql`, join Customer to Invoice using CustomerId.
Show each customer's name, Country, invoice count, and total spending. Sort by
spending descending and show the top ten.

**Task 8.** Change to a LEFT JOIN and keep every customer. Use COUNT of
`i.InvoiceId` and COALESCE around SUM to handle customers with no invoices.

Check: one output row represents a customer. COUNT(*) on a LEFT JOIN can count
the placeholder unmatched row; COUNT(i.InvoiceId) does not.

## Stage 5 - Follow the product chain (multiple joins)

**Task 9.** In `06_artist_sales.sql`, join InvoiceLine -> Track -> Album ->
Artist. Group by ArtistId and Artist.Name. Calculate units sold using
SUM(InvoiceLine.Quantity), and line revenue using
SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity). Return the top ten artists
by line revenue.

**Task 10.** Add a COUNT of distinct TrackId to see how many different tracks
from each artist appear in sold invoice lines. Explain why units sold can be
larger than the number of distinct tracks.

Check: one InvoiceLine row can represent multiple units. This stage sums line
amounts and does not sum Invoice.Total.

## Stage 6 - Ask a nested question (subqueries)

**Task 11.** In `07_above_average.sql`, find invoices whose Total is above the
overall AVG(Total). Return InvoiceId, CustomerId, and Total.

**Task 12.** Change the query to compare each invoice with the average for its
own CustomerId. Give the inner Invoice table a different alias. Explain why
this is a correlated subquery.

## Final report

Complete `REPORT.md` with: three findings, the query behind each finding, and
one caveat. A good caveat might concern billing country versus customer
country, or the fact that the sample data are historical and not current sales.
