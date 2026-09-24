from pathlib import Path


class RepositoryAnalyzer:

    def detect_project_type(self, repository_path: str):
        path = Path(repository_path)

        if (path / "requirements.txt").exists():
            return "Python"

        if (path / "package.json").exists():
            return "Node.js"

        if (path / "pom.xml").exists():
            return "Java (Maven)"

        if (path / "build.gradle").exists():
            return "Java (Gradle)"

        if (path / "Dockerfile").exists():
            return "Docker"

        return "Unknown"