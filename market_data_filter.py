import pandas as pd

# ==========================================================
# Market Data Filter Script
# Reads clean_jobs_200.csv
# Creates Market_Data.xlsx with 3 sheets:
#   1. Logistics Workforce
#   2. Automotive Workforce
#   3. Skilling Programs
# ==========================================================

# Read CSV file
df = pd.read_csv("clean_jobs_200.csv")

# Create a searchable text column
df["search_text"] = (
    df["Job Title"].fillna("").astype(str) + " " +
    df["Required Skills"].fillna("").astype(str)
).str.lower()

# ----------------------------------------------------------
# Keywords
# ----------------------------------------------------------

logistics_keywords = [
    "logistics",
    "supply chain",
    "warehouse",
    "inventory",
    "dispatch",
    "transport",
    "fleet",
    "shipping",
    "procurement",
    "operations"
]

automotive_keywords = [
    "automotive",
    "automobile",
    "vehicle",
    "manufacturing",
    "production",
    "mechanical",
    "quality",
    "assembly",
    "service engineer",
    "ev"
]

skilling_keywords = [
    "trainer",
    "training",
    "learning",
    "instructor",
    "faculty",
    "coach",
    "enablement",
    "l&d",
    "skill development",
    "technical trainer"
]

# ----------------------------------------------------------
# Function to filter records
# ----------------------------------------------------------

def filter_jobs(dataframe, keywords):
    pattern = "|".join(keywords)
    return dataframe[
        dataframe["search_text"].str.contains(
            pattern,
            case=False,
            na=False
        )
    ].copy()

# ----------------------------------------------------------
# Filter datasets
# ----------------------------------------------------------

logistics_df = filter_jobs(df, logistics_keywords)
automotive_df = filter_jobs(df, automotive_keywords)
skilling_df = filter_jobs(df, skilling_keywords)

# Remove helper column
logistics_df.drop(columns=["search_text"], inplace=True)
automotive_df.drop(columns=["search_text"], inplace=True)
skilling_df.drop(columns=["search_text"], inplace=True)

# ----------------------------------------------------------
# Save into one Excel workbook
# ----------------------------------------------------------

output_file = "Market_Data.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    logistics_df.to_excel(
        writer,
        sheet_name="Logistics Workforce",
        index=False
    )

    automotive_df.to_excel(
        writer,
        sheet_name="Automotive Workforce",
        index=False
    )

    skilling_df.to_excel(
        writer,
        sheet_name="Skilling Programs",
        index=False
    )

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("=" * 50)
print("Market Data Excel Created Successfully!")
print("=" * 50)

print(f"Logistics Workforce   : {len(logistics_df)} records")
print(f"Automotive Workforce  : {len(automotive_df)} records")
print(f"Skilling Programs     : {len(skilling_df)} records")

print("\nOutput File:")
print(output_file)