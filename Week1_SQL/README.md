# Week 1 - SQL

## :star: Featured Dataset
[https://www.opensecrets.org/featured-datasets/49](https://www.opensecrets.org/featured-datasets/49)

## :question: Where did higher-ups(and less notable employees) donate money?
- Higher-ups include Sam Bankman-Fried(CEO), Ryan Salame(Co-CEO), and Nishad Singh(Engineering Director)

## Key Takeaways
![top donors include SBF, Salame, and Singh](/images/week1/top_donors.png)

## Tools Used
- tabview, for initial exploration
- python, for levenshtein distance calculation

## Cheat Sheet
```sql
SELECT contrib, COUNT(*) as transactions from table GROUP BY transactions ORDER BY desc
```
- selects the donors name and their no. of occurrences
    - SQL has a special [order of execution](https://builtin.com/data-science/sql-order-of-execution), so the `COUNT(*)` clause runs on the unique columns generated after `GROUP BY`, and not after the non-unique data generated from the initial `SELECT`