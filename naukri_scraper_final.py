from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

job_titles = [
    "fleet supervisor",
    "dispatch executive",
    "warehouse coordinator",
    "logistics trainer"
]

jobs_data = []

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

for job in job_titles:

    url = f"https://www.naukri.com/{job.replace(' ', '-')}-jobs"
    print("\nSearching:", job)

    driver.get(url)
    time.sleep(5)

    job_cards = driver.find_elements(By.CLASS_NAME, "cust-job-tuple")

    print("Jobs found:", len(job_cards))

    for card in job_cards:

        if len(jobs_data) >= 50:
            break

        try:
            title = card.find_element(By.CSS_SELECTOR, "a.title").text
            company = card.find_element(By.CSS_SELECTOR, "a.comp-name").text
            location = card.find_element(By.CSS_SELECTOR, "span.locWdth").text
            job_url = card.find_element(By.CSS_SELECTOR, "a.title").get_attribute("href")

            skills_elements = card.find_elements(By.CSS_SELECTOR, "li.tag-li")
            skills = ", ".join([s.text for s in skills_elements])

            jobs_data.append({
                "Job Title": title,
                "Company": company,
                "Location": location,
                "Skills": skills,
                "URL": job_url
            })

        except:
            continue

    if len(jobs_data) >= 50:
        break

driver.quit()

df = pd.DataFrame(jobs_data)
df.to_csv("jobs.csv", index=False, encoding="utf-8-sig")

print("\nCompleted Successfully!")
print("Total Jobs Saved:", len(df))
print("File saved as jobs.csv")