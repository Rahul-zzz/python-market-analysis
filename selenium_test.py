from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

print("Browser opened successfully!")

time.sleep(5)
driver.quit()