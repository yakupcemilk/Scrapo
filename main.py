import multiprocessing

def run_fastapi():
    import uvicorn
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000)

def run_nicegui():
    import ui.window  # window.py dosyasını çalıştırır, bu da NiceGUI arayüzünü başlatır

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_fastapi)
    p2 = multiprocessing.Process(target=run_nicegui)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
