import duckdb
from pathlib import Path
import pandas as pd

WEEK_ROOT = Path(__file__).parent
path = WEEK_ROOT / "data/Direct_Contributions_and_JFC_Distributions.csv"
# SBF_CONTRIB_ID = "U0000004705"

def read_with_duckdb():
    query = f"""
    SELECT ANY_VALUE(contrib) as donor, contribid, SUM(CAST(REPLACE(REPLACE(amount, '$', ''), ',', '') AS FLOAT)) as total_amount
    FROM '{path.absolute()}'
    GROUP BY contribid
    ORDER BY total_amount DESC
    """
    results = duckdb.query(query).to_df()
    print(results)

def read_with_pandas():
    df = pd.read_csv(path)
    df = df[['amount', 'contribid', 'contrib']]
    df['amount'] = df['amount'].replace('[\\$,]', '', regex=True).astype(float)

    unique_df = df.groupby('contribid', as_index=False).agg(
        total=('amount', 'sum'),
        name=('contrib', 'first')
    ).sort_values('total', ascending=False)
    print(unique_df)

read_with_pandas()