import pandas as pd

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("clean_jobs_200.csv")

text_columns = (df["Job Title"].fillna("") + " " +
                df["Required Skills"].fillna("")).str.lower()

# ===============================
# LANGUAGE KEYWORDS
# ===============================
language_keywords = [
    "hindi",
    "tamil",
    "kannada",
    "telugu",
    "english",
    "regional language",
    "bilingual",
    "multilingual"
]

# ===============================
# FILTER FUNCTION
# ===============================
def has_language(text):
    return any(lang in text for lang in language_keywords)

df["language_required"] = text_columns.apply(has_language)

# ===============================
# CREATE LANGUAGE JOBS DATASET
# ===============================
df_lang = df[df["language_required"] == True]

# ===============================
# SAVE NEW FILE
# ===============================
df_lang.to_csv("language_required_jobs.csv", index=False)

# ===============================
# OUTPUT SUMMARY
# ===============================
print("\n=== LANGUAGE REQUIREMENT FILTER ===\n")
print(f"Total Jobs: {len(df)}")
print(f"Language Required Jobs: {len(df_lang)}")
print(f"Percentage: {(len(df_lang)/len(df))*100:.2f}%")

print("\nFile saved as: language_required_jobs.csv")