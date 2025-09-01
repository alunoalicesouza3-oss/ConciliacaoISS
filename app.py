from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import pandas as pd
from conciliacao import conciliar_arquivos

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload(request: Request,
                 file1: UploadFile = File(...),
                 file2: UploadFile = File(...),
                 file3: UploadFile = File(...)):

    # Ler arquivos com pandas
    df1 = pd.read_excel(file1.file)
    df2 = pd.read_excel(file2.file)
    df3 = pd.read_excel(file3.file)

    # Rodar conciliação
    divergencias = conciliar_arquivos(df1, df2, df3)

    # Aqui você pode salvar no Supabase
    # supabase.table("divergencias").insert(divergencias.to_dict('records')).execute()

    return templates.TemplateResponse("index.html", 
                                      {"request": request, 
                                       "divergencias": divergencias.to_html(index=False)})
