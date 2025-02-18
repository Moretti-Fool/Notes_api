from pydantic import BaseModel


class NoteRequest(BaseModel):
    folder_name: str
    file_name: str
    content: str



class NoteEdit(NoteRequest):
    edit: bool 