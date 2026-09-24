from pathlib import Path


class RepositoryAnalyzer:

    def detect_project_type(self, repository_path: str):
        path = Path(repository_path)

        # Python
        if list(path.rglob("requirements.txt")):
            return "Python"

        # Node.js
        if list(path.rglob("package.json")):
            return "Node.js"

        # Java Maven
        if list(path.rglob("pom.xml")):
            return "Java (Maven)"

        # Java Gradle
        if list(path.rglob("build.gradle")):
            return "Java (Gradle)"

        # Docker
        if list(path.rglob("Dockerfile")):
            return "Docker"

        return "Unknown"