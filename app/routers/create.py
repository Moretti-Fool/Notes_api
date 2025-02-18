import os
from fastapi import APIRouter, HTTPException, status, Form, Query
from app.schemas import NoteRequest, NoteEdit





router = APIRouter(
    prefix="/create",
    tags=['Create New File'] # it groups the post function under posts in documention
)


def get_base_dir():
    from app.main import BASE_DIR
    return BASE_DIR


@router.post("/")
async def create_file(
    folder_name: str = Form(),
    file_name: str = Form(...),
    content: str = Form(...),
):
    # Ensure folder exists
    note = NoteRequest(folder_name=folder_name, file_name=file_name, content=content)
    folder_path = os.path.join(get_base_dir(), note.folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Define file path
    file_path = os.path.join(folder_path, f"{note.file_name}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
            f.write(note.content)


    return {"message": "Note created successfully", "file_path": file_path}



@router.get("/read")
def read_file(folder_name: str = Query(...), file_name: str = Query(...)):
    folder_path = os.path.join(get_base_dir(), folder_name)
    file_path = os.path.join(folder_path, f"{file_name}.txt")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    return content



@router.post("/edit")
def edit_file(note: NoteEdit):
    folder_path = os.path.join(get_base_dir(), note.folder_name)
    file_path = os.path.join(folder_path, f"{note.file_name}.txt")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")


    if note.edit == False:
        with open(file_path, "a", encoding="utf-8") as f:  # Append new content to the existing file
            f.write("\n" + note.content)
    elif note.edit == True:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(note.content)


    return {"message": "Note edited successfully", "file_path": file_path}

@router.post("/rename_file")
async def rename_file(Folder_name: str = Form(), old_file_name: str = Form(...), new_file_name: str = Form(...)):
    folder_path = os.path.join(get_base_dir(), Folder_name)
    old_file_path = os.path.join(folder_path, f'{old_file_name}.txt')
    new_file_path = os.path.join(folder_path, f'{new_file_name}.txt')

    if not os.path.exists(old_file_path):
        raise HTTPException(status_code=404, detail="The file does not exist.")

    # Rename the file
    os.rename(old_file_path, new_file_path)

    return {"message": f"File renamed from {old_file_name} to {new_file_name}"}