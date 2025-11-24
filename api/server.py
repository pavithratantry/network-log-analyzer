from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os

from core.parser import parse_logs
from core.analyzer import detect_anomalies
from core.llm import summarize_anomalies

app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'), name='static')
templates = Jinja2Templates(directory='app/templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'summary': None})

@app.post('/analyze', response_class=HTMLResponse)
async def analyze(request: Request, file: UploadFile = File(...)):
    temp_path = 'uploaded_logs.txt'
    with open(temp_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)

    parsed = parse_logs(temp_path)
    anomalies = detect_anomalies(parsed)
    summary = summarize_anomalies(anomalies)

    return templates.TemplateResponse('index.html', {'request': request, 'summary': summary})