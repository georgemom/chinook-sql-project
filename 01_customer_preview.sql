-- Task 1: inspect customer records. Change the sort and run again.
SELECT CustomerId, FirstName, LastName, Country
FROM Customer
ORDER BY Country, LastName
LIMIT 10;
