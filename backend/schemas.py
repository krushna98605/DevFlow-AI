from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    repository: str


class ProjectResponse(BaseModel):
    id: int
    name: str
    repository: str

    class Config:
        from_attributes = True