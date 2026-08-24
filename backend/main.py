from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import Project as ProjectModel

app = FastAPI(title="DevFlow AI API")


class ProjectCreate(BaseModel):
    name: str
    repository: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "DevFlow AI"
    }


@app.post("/projects")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    new_project = ProjectModel(
        name=project.name,
        repository=project.repository
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "message": "Project created successfully",
        "project": {
            "id": new_project.id,
            "name": new_project.name,
            "repository": new_project.repository
        }
    }


@app.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(ProjectModel).all()

    return {
        "projects": [
            {
                "id": project.id,
                "name": project.name,
                "repository": project.repository
            }
            for project in projects
        ]
    }


@app.get("/projects/{project_id}")
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = (
        db.query(ProjectModel)
        .filter(ProjectModel.id == project_id)
        .first()
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "id": project.id,
        "name": project.name,
        "repository": project.repository
    }


@app.delete("/projects/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = (
        db.query(ProjectModel)
        .filter(ProjectModel.id == project_id)
        .first()
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }