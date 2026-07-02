import pandas as pd

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("language_required_jobs.csv")

# ===============================
# CREATE SEARCH TEXT
# ===============================
df["Search_Text"] = (
    df["Job Title"].fillna("") + " " +
    df["Required Skills"].fillna("") + " " +
    df.get("Job Description", pd.Series([""] * len(df))).fillna("")
).str.lower()

# ===============================
# LANGUAGE LIST
# ===============================
languages = [
    "hindi",
    "tamil",
    "kannada",
    "telugu",
    "malayalam",
    "marathi",
    "gujarati"
]

# ===============================
# OUTPUT FILE WRITER
# ===============================
all_language_jobs = []

print("\n=== LANGUAGE WISE JOB DETAILS ===\n")

# ===============================
# LOOP EACH LANGUAGE
# ===============================
for language in languages:

    lang_jobs = df[
        df["Search_Text"].str.contains(language, case=False, na=False)
    ]

    print(f"\n\n================ {language.upper()} =================")
    print(f"Total Jobs: {len(lang_jobs)}")

    # Show full job details (important columns only)
    print(lang_jobs[[
        "Search City",
        "Job Title",
        "Company",
        "Location",
        "Required Skills"
    ]])

    # Add language column for export
    lang_jobs = lang_jobs.copy()
    lang_jobs["Language"] = language

    all_language_jobs.append(lang_jobs)

# ===============================
# COMBINE ALL RESULTS
# ===============================
final_df = pd.concat(all_language_jobs, ignore_index=True)

# ===============================
# SAVE OUTPUT FILE
# ===============================
final_df.to_csv("language_full_job_details.csv", index=False)

print("\n\nFile Created: language_full_job_details.csv")