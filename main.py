from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="API de Gestión de Pedidos", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
def obtener_dashboard_visual():
    ruta_html = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(ruta_html):
        with open(ruta_html, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Error: index.html no encontrado</h1>"
