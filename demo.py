import requests

url = "https://www.naukri.com/fleet-supervisor-jobs"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text[:500])