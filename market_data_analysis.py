import pandas as pd
from collections import Counter

# ==========================================================
# Market Data Analysis
# Analyzes Market_Data.xlsx
# ==========================================================

FILE_NAME = "Market_Data.xlsx"

# Read all sheets
xls = pd.ExcelFile(FILE_NAME)

print("=" * 70)
print("MARKET DATA ANALYSIS")
print("=" * 70)


def analyze_sheet(sheet_name):

    print("\n" + "=" * 70)
    print(sheet_name.upper())
    print("=" * 70)

    df = pd.read_excel(FILE_NAME, sheet_name=sheet_name)

    print(f"\nTotal Records : {len(df)}")

    # -------------------------------
    # Top Job Titles
    # -------------------------------
    print("\nTop Job Titles")
    print("-" * 30)

    print(df["Job Title"].value_counts().head(10))

    # -------------------------------
    # Top Companies
    # -------------------------------
    print("\nTop Hiring Companies")
    print("-" * 30)

    print(df["Company"].value_counts().head(10))

    # -------------------------------
    # Top Locations
    # -------------------------------
    print("\nTop Hiring Locations")
    print("-" * 30)

    print(df["Location"].value_counts().head(10))

    # -------------------------------
    # Top Skills
    # -------------------------------
    print("\nTop Required Skills")
    print("-" * 30)

    skills_counter = Counter()

    if "Required Skills" in df.columns:

        for skills in df["Required Skills"].dropna():

            for skill in str(skills).split(","):

                skill = skill.strip()

                if skill:

                    skills_counter[skill] += 1

    for skill, count in skills_counter.most_common(15):

        print(f"{skill:35} {count}")


# Analyze every sheet
for sheet in xls.sheet_names:
    analyze_sheet(sheet)

print("\n")
print("=" * 70)
print("Analysis Completed Successfully")
print("=" * 70)