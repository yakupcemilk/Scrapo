from nicegui import ui
import requests

def fetch_data(url, tag):
    try:
        response = requests.get(f"http://localhost:8000/scrape", params={"url": url, "tag": tag})
        response.raise_for_status()
        data = response.json().get("data", [])
        return data
    except requests.exceptions.RequestException as e:
        return [f"Error: {str(e)}"]

def on_submit(url, tag):
    ui.clear()
    with ui.card():
        ui.label(f'Scraping URL: {url}')
        ui.label(f'Searching for HTML tag: {tag}')
        results = fetch_data(url, tag)
        with ui.column():
            for item in results:
                ui.label(item)

with ui.row():
    url_input = ui.input(label='Enter URL').classes('w-full')
    tag_input = ui.input(label='Enter HTML tag').classes('w-full')
    ui.button('Scrape', on_click=lambda: on_submit(url_input.value, tag_input.value)).classes('w-full')

ui.run(port=8080)
