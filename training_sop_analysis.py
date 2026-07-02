import pandas as pd

# ===============================
# LOAD ENRICHED DATA
# ===============================
df = pd.read_csv("clean_jobs_200_enriched.csv")

text_column = "job_description_clean"

# ===============================
# KEYWORDS
# ===============================
keywords = ["training", "sop", "compliance", "safety", "certification"]

# ===============================
# CLASSIFY EACH KEYWORD
# ===============================
for word in keywords:
    df[word] = df[text_column].apply(lambda x: 1 if word in x else 0)

# ===============================
# SUMMARY
# ===============================
print("\n=== SOP ANALYSIS (ENRICHED DATA) ===\n")

for word in keywords:
    print(f"{word.upper():15}: {df[word].sum()}")

# ===============================
# OVERALL COVERAGE
# ===============================
df["any_sop"] = df[keywords].sum(axis=1) > 0

print("\nTotal Jobs:", len(df))
print("SOP-related Jobs:", df["any_sop"].sum())
print("Coverage %:", round(df["any_sop"].mean() * 100, 2))

# ===============================
# SAVE FINAL FILE
# ===============================
df.to_csv("clean_jobs_200_sop_final.csv", index=False)

print("\nFinal file saved: clean_jobs_200_sop_final.csv")