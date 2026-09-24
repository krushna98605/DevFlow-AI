from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.repository_service import RepositoryService


router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)


class RepositoryRequest(BaseModel):
    repository_url: str


repository_service = RepositoryService()


@router.post("/analyze")
def analyze_repository(request: RepositoryRequest):
    try:
        result = repository_service.clone_and_analyze(
            request.repository_url,
            "workspace/repository"
        )

        return result

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )