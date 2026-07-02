import pandas as pd

# Load dataset
df = pd.read_csv("clean_jobs_200_with_desc.csv")

# Combine Description + Skills
df["Search_Text"] = (
    df["Job Description"].fillna("") + " " +
    df["Required Skills"].fillna("")
)

# Keywords
keywords = [
    "fresher",
    "freshers",
    "will train",
    "training provided",
    "no experience"
]

results = []

print("\nFreshers & Training Analysis")
print("=" * 50)

for keyword in keywords:

    count = df["Search_Text"].str.contains(
        keyword,
        case=False,
        na=False
    ).sum()

    print(f"{keyword}: {count}")

    results.append({
        "Keyword": keyword,
        "Count": count
    })

# Save results
results_df = pd.DataFrame(results)

results_df.to_excel(
    "freshers_training_analysis.xlsx",
    index=False
)

print("\nExcel File Created Successfully")
print("Output File: freshers_training_analysis.xlsx")