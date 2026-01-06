from dataclasses import dataclass

@dataclass
class CrawledArticle:
    title: str
    brand: str
    price: str
    image: str
    url: str

    def to_dict(self):
        return {
            "title": self.title,
            "brand": self.brand,
            "price": self.price,
            "image": self.image,
            "url": self.url
        }