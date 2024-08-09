from fastapi import FastAPI
from backend.scraper import scrape_website  # scrape_website fonksiyonu ayrı bir dosyada olabilir

app = FastAPI()

@app.get("/scrape")
def scrape(url: str, tag: str):
    data = scrape_website(url, tag)
    return {"data": data}
