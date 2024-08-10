import FastAPI
import scraper

app = FastAPI()

@app.get("/scrape")
def scrape(url: str, tag: str):
    data = scraper.scrape_website(url, tag)
    return {"data": data}
