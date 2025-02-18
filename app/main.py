import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from .routers import create, upload

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

app.include_router(create.router) 
app.include_router(upload.router)
# app.include_router(auth.router)







# UPLOAD_FOLDER = 'uploads'
# BASE_DIR = "notes"
# Image_path = os.path.join(UPLOAD_FOLDER, 'images')
# Pdf_path = os.path.join(UPLOAD_FOLDER, 'pdf')

# os.makedirs(BASE_DIR, exist_ok=True)
# os.makedirs(Image_path, exist_ok=True)
# os.makedirs(Pdf_path, exist_ok=True)

BASE_DIR = "notes"
os.makedirs(BASE_DIR, exist_ok=True)
DEFAULT_FOLDER_NAME = "DefaultFolder"

@app.get("/")
async def index(request: Request):
    # List folders and files in the BASE_DIR
    folders = os.listdir(BASE_DIR)
    folder_files = {}
    
    for folder in folders:
        folder_path = os.path.join(BASE_DIR, folder)
        if os.path.isdir(folder_path):
            folder_files[folder] = os.listdir(folder_path)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "folders": folder_files
    })











