from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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


@app.get("/")
def index():
    return {"message": "hello"}











