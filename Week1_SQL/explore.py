import duckdb
from pathlib import Path


WEEK_ROOT = Path(__file__).parent
path = WEEK_ROOT / "data/Direct_Contributions_and_JFC_Distributions.csv"
query = f"""
    SELECT contrib as donor, count(*) as donations
    FROM '{path.absolute()}'
    GROUP BY donor
    ORDER BY donations desc
"""

results = duckdb.query(query)
print(results)

# todo: calculate levenshtein distance to collapse donor duplicates