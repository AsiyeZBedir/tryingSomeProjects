# web_scraping.py
import requests
from bs4 import BeautifulSoup

def haber_basliklarini_getir(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        basliklar = soup.find_all("h2")

        for i, baslik in enumerate(basliklar, start=1):
            print(f"{i}. {baslik.text}")
    else:
        print("Haber başlıkları alınamadı.")

def main():
    url = "https://example.com"  # Scraping yapmak istediğiniz web sitesinin URL'sini buraya ekleyin.
    haber_basliklarini_getir(url)

if __name__ == "__main__":
    main()
