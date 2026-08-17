from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="DevFlow AI API")


class Project(BaseModel):
    name: str
    repository: str


projects = []
next_project_id = 1


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "DevFlow AI"
    }


@app.post("/projects")
def create_project(project: Project):
    global next_project_id

    new_project = {
        "id": next_project_id,
        "name": project.name,
        "repository": project.repository
    }

    projects.append(new_project)
    next_project_id += 1

    return {
        "message": "Project created successfully",
        "project": new_project
    }


@app.get("/projects")
def get_projects():
    return {
        "projects": projects
    }


@app.get("/projects/{project_id}")
def get_project(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            return project

    raise HTTPException(
        status_code=404,
        detail="Project not found"
    )


@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            projects.remove(project)

            return {
                "message": "Project deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Project not found"
    )