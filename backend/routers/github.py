from fastapi import APIRouter, HTTPException

from services.github_service import GitHubService


router = APIRouter(
    prefix="/github",
    tags=["GitHub"]
)

github_service = GitHubService()


@router.get("/repository")
def get_repository_info(url: str):
    try:
        return github_service.get_repository_info(url)

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="GitHub repository not found or is not accessible"
        )