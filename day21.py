import requests
from bs4 import BeautifulSoup

url = 'https://towardsdatascience.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
headlines = soup.find_all('h2')

print("📰 Headlines from Towards Data Science:\n")
for i, headline in enumerate(headlines[:10], 1):
    print(f"{i}. {headline.get_text(strip=True)}")
