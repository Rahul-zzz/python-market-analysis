import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_jobs_200.csv")

all_skills = []

for skills in df["Required Skills"].dropna():

    skill_list = skills.split("|")

    for skill in skill_list:
        all_skills.append(skill.strip().title())

skills_series = pd.Series(all_skills)

print(skills_series.value_counts())
freq_table = (
    skills_series
    .value_counts()
    .reset_index()
)

freq_table.columns = ["Skill", "Count"]

total_postings = len(df)

freq_table["Percentage"] = (
    freq_table["Count"]
    / total_postings
    * 100
).round(2)

top30 = freq_table.head(30)
def categorize(skill):

    skill = skill.lower()

    technical_skills = [
        "logistics",
        "dispatch",
        "operations",
        "warehouse",
        "transportation",
        "route planning",
        "supply chain",
        "fleet",
        "inventory",
        "shipment",
        "compliance",
        "vehicle management"
    ]

    soft_skills = [
        "communication",
        "customer service",
        "leadership",
        "team management",
        "problem solving",
        "administration"
    ]

    software_tools = [
        "excel",
        "sap",
        "erp",
        "wms",
        "power bi",
        "tally"
    ]

    language_requirements = [
        "english",
        "hindi",
        "tamil"
    ]

    if any(word in skill for word in technical_skills):
        return "Technical Skills"

    elif any(word in skill for word in soft_skills):
        return "Soft Skills"

    elif any(word in skill for word in software_tools):
        return "Software/Tools"

    elif any(word in skill for word in language_requirements):
        return "Language Requirements"

    else:
        return "Technical Skills"
top30["Category"] = top30["Skill"].apply(categorize)
top30["Must Have"] = top30["Percentage"].apply(
    lambda x: "Yes" if x > 30 else "No"
)

# Display Result
print("\nTop 30 Skills with Categories\n")
print("\nTop 30 Skills Analysis\n")
print(top30)

# Save Excel
top30.to_excel(
    "skills_frequency_table.xlsx",
    index=False
)

print("\nExcel File Created Successfully")
print("Output File: skills_frequency_table.xlsx")
top15 = top30.head(15)

plt.figure(figsize=(12, 6))

plt.bar(
    top15["Skill"],
    top15["Count"]
)

plt.title("Top 15 Skills by Frequency")

plt.xlabel("Skills")

plt.ylabel("Frequency")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.savefig("top15_skills.png")

plt.show()

print("Chart Saved: top15_skills.png")