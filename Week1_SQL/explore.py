import duckdb
from Levenshtein import distance
from pathlib import Path

# return the possible matches for a string, using values from a list
# we match by seeing if levenshtein_distance(comparison, list[i]) is less than or equal to threshold
def return_possible_matches(comparison_value: str, list: list[str], threshold: int = 4) -> list[str]:
    matches: list[str] = []

    for val in list:
        if distance(comparison_value, val) <= threshold:
            matches.append(val)

    return matches

WEEK_ROOT = Path(__file__).parent
path = WEEK_ROOT / "data/Direct_Contributions_and_JFC_Distributions.csv"
query = f"""
    SELECT contrib as donor, count(*) as donations
    FROM '{path.absolute()}'
    GROUP BY donor
    ORDER BY donations desc
"""



results = duckdb.query(query).to_df()
global matches
matches: list[list[str]] = []

global total_donations
total_donations: list[list[int]] = []
for donor in results.donor:
    # values of 6 or lower seem to work for nishad singh, but we miss out on SBF matches that could be caught with threshold of 11
    # todo - write version that accounts for swapped first/last names
    found_matches = return_possible_matches(donor, results.donor.tolist(), 6)
    matches.append(found_matches)
    total_donations.append([results.donations[results.donor == match].tolist() for match in found_matches])

results["matches"] = matches
results["total_donations"] = total_donations

print(results.head(1))