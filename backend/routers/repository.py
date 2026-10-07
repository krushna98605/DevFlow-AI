import uuid

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
        # Create a unique workspace for this analysis
        workspace_id = str(uuid.uuid4())
        destination = f"workspace/{workspace_id}"

        result = repository_service.clone_and_analyze(
            request.repository_url,
            destination
        )

        return result

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )