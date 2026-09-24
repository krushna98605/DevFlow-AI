from pathlib import Path


class RepositoryAnalyzer:

    def detect_project_types(self, repository_path: str):
        path = Path(repository_path)

        project_types = []

        if list(path.rglob("requirements.txt")):
            project_types.append("Python")

        if list(path.rglob("package.json")):
            project_types.append("Node.js")

        if list(path.rglob("pom.xml")):
            project_types.append("Java (Maven)")

        if list(path.rglob("build.gradle")):
            project_types.append("Java (Gradle)")

        if list(path.rglob("Dockerfile")):
            project_types.append("Docker")

        if not project_types:
            project_types.append("Unknown")

        return project_types