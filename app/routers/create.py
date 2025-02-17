import os
from fastapi import APIRouter, HTTPException, status
from app.schemas import NoteRequest, NoteEdit



router = APIRouter(
    prefix="/create",
    tags=['Create New File'] # it groups the post function under posts in documention
)


BASE_DIR = "notes"
os.makedirs(BASE_DIR, exist_ok=True)




@router.post("/")
def create_file(note: NoteRequest):
    # Ensure folder exists
    folder_path = os.path.join(BASE_DIR, note.folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Define file path
    file_path = os.path.join(folder_path, f"{note.file_name}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
            f.write(note.content)


    return {"message": "Note created successfully", "file_path": file_path}


@router.post("/edit")
def edit_file(note: NoteEdit):
    folder_path = os.path.join(BASE_DIR, note.folder_name)
    file_path = os.path.join(folder_path, f"{note.file_name}.txt")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")


    if note.edit == False:
        with open(file_path, "a", encoding="utf-8") as f:  # Append new content to the existing file
            f.write("\n" + note.content)
    elif note.edit == True:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(note.content)

    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Choose 'pdf', 'word', or 'txt'.")

    return {"message": "Note edited successfully", "file_path": file_path}