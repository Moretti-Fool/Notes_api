import os
from fastapi import File, UploadFile, HTTPException, status, APIRouter
from fastapi.responses import JSONResponse



router = APIRouter(
    prefix="/upload",
    tags=['Upload File'] # it groups the post function under posts in documention
)

UPLOAD_FOLDER = 'uploads'

Image_path = os.path.join(UPLOAD_FOLDER, 'images')
Pdf_path = os.path.join(UPLOAD_FOLDER, 'pdf')

os.makedirs(Image_path, exist_ok=True)
os.makedirs(Pdf_path, exist_ok=True)




@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type.startswith("image/"):  # Any image type
        file_path = os.path.join(Image_path, file.filename)
    elif file.content_type == "application/pdf":
        file_path = os.path.join(Pdf_path, file.filename)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type")
    # print(file.content_type)
    # file_path = os.path.join(Pdf_path, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return JSONResponse(content={"message": "File upladed", "filename": file.filename, "content_type": file.content_type})