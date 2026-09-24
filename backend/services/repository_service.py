from services.repository_cloner import RepositoryCloner
from services.repository_analyzer import RepositoryAnalyzer


class RepositoryService:

    def __init__(self):
        self.cloner = RepositoryCloner()
        self.analyzer = RepositoryAnalyzer()

    def clone_and_analyze(
        self,
        repository_url: str,
        destination: str
    ):
        # Step 1: Clone repository
        repository_path = self.cloner.clone_repository(
            repository_url,
            destination
        )

        # Step 2: Analyze repository
        project_types = self.analyzer.detect_project_types(
            repository_path
        )

        return {
            "repository_url": repository_url,
            "repository_path": repository_path,
            "project_types": project_types
        }