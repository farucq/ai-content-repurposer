import requests
from bs4 import BeautifulSoup
from newspaper import Article

from utils.helpers import clean_text, split_sections


class ContentParser:

    def parse_url(self, url):

        try:
            # Try newspaper first
            article = Article(url)
            article.download()
            article.parse()

            text = article.text

        except Exception:

            # Fallback scraping
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }

            response = requests.get(url, headers=headers)

            soup = BeautifulSoup(response.text, "html.parser")

            paragraphs = soup.find_all("p")

            text = " ".join([p.get_text() for p in paragraphs])

        text = clean_text(text)

        sections = split_sections(text)

        return {
            "title": "Parsed Blog",
            "text": text,
            "sections": sections
        }


    def parse_text(self, text):

        clean = BeautifulSoup(text, "html.parser").get_text()

        clean = clean_text(clean)

        sections = split_sections(clean)

        return {
            "title": "User Blog",
            "text": clean,
            "sections": sections
        }