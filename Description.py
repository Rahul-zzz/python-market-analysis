import pandas as pd

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("clean_jobs_200.csv")

# ===============================
# CLEAN TEXT FUNCTION
# ===============================
def clean_text(x):
    return str(x).lower() if pd.notnull(x) else ""

# ===============================
# CREATE FULL JOB DESCRIPTION
# ===============================
df["job_description_clean"] = (
    df["Job Title"].apply(clean_text) + " " +
    df["Company"].apply(clean_text) + " " +
    df["Location"].apply(clean_text) + " " +
    df["Required Skills"].apply(clean_text)
)

# ===============================
# SAVE NEW FILE
# ===============================
df.to_csv("clean_jobs_200_enriched.csv", index=False)

print("Enriched dataset created successfully!")