import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from CrawledArticle import CrawledArticle
from datetime import datetime

class ArticleFetcher:
    def log_error(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("crawler_errors.log", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")

    def fetch(self, url, selectors):
        page_count = 0
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

        while url != "":
            page_count += 1
            if page_count > 1 and page_count % 100 == 0:
                print(f"\n[!] 100 Seiten erreicht. 3 Min Pause...")
                time.sleep(180)

            print(f"[*] Scanne Seite {page_count}: {url}")
            
            try:
                r = requests.get(url, headers=headers, timeout=15)
                r.raise_for_status()
                
                time.sleep(1.5)
                doc = BeautifulSoup(r.text, "html.parser")
                articles_found = doc.select(selectors['container'])
                
                if not articles_found:
                    break

                for card in articles_found:
                    title_elem = card.select_one(selectors.get('title'))
                    title = title_elem.text.strip() if title_elem else "N/A"
                    
                    price_elem = card.select_one(".price, .deal-price, .a-price, .item-price")
                    price = price_elem.text.strip() if price_elem else "N/A"
                    
                    brand_elem = card.select_one(".brand, .merchant, .badge, .category")
                    brand = brand_elem.text.strip() if brand_elem else title.split(' ')[0]

                    a_tag = title_elem if title_elem and title_elem.name == 'a' else (title_elem.find('a') if title_elem else None)
                    article_url = urljoin(url, a_tag.get('href')) if a_tag else "N/A"
                    
                    img_elem = card.select_one(selectors.get('image'))
                    image = urljoin(url, img_elem.attrs["src"]) if img_elem and "src" in img_elem.attrs else "N/A"

                    yield CrawledArticle(title, brand, price, image, article_url)

                next_btn = doc.select_one(selectors['next_btn'])
                url = urljoin(url, next_btn.attrs["href"]) if next_btn and "href" in next_btn.attrs else ""

            except Exception as e:
                self.log_error(f"Fehler auf Seite {page_count}: {e}")
                break