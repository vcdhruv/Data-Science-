# to fetch content from multiple websites concurrently.

import requests
import threading
from bs4 import BeautifulSoup

url_list = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://docs.smith.langchain.com/',
    'https://python.langchain.com/v0.2/docs/versions/packages/'
]

def fetch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = [threading.Thread(target=fetch,args=(url,)) for url in url_list]

# print(threads)

for thread in threads:
    thread.start()
    thread.join()
print("All web pages fetched.")