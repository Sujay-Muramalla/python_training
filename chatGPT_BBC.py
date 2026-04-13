import requests
from bs4 import BeautifulSoup

# URL of BBC homepage
url = "https://www.bbc.com"

# Get page content
response = requests.get(url)
if response.status_code != 200:
    print("Failed to fetch page:", response.status_code)
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Collect all headlines (usually h1, h2, h3 are used)
headlines = []
for tag in soup.find_all(["h1", "h2", "h3"]):
    text = tag.get_text(strip=True)
    if text:  # Avoid empty strings
        headlines.append(text)

# Print results
print("BBC Headlines:")
for i, hl in enumerate(headlines, 1):
    print(f"{i}. {hl}")