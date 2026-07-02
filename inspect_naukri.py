from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

url = "https://www.naukri.com/fleet-supervisor-jobs"
driver.get(url)

time.sleep(5)

print("Page Title:", driver.title)

job_cards = driver.find_elements(By.CLASS_NAME, "cust-job-tuple")

print("Job cards found:", len(job_cards))

if len(job_cards) > 0:
    print("Sample job text:")
    print(job_cards[0].text)

input("Press Enter to close browser...")
driver.quit()