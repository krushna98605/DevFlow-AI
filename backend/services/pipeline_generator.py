class PipelineGenerator:

    def generate(self, project_types: list[str]):

        steps = [
            """      - name: Checkout code
        uses: actions/checkout@v4"""
        ]

        # Python
        if "Python" in project_types:
            steps.append(
                """      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12" """
            )

            steps.append(
                """      - name: Install Python dependencies
        run: |
          pip install -r backend/requirements.txt"""
            )

            steps.append(
                """      - name: Run Python tests
        run: |
          pytest"""
            )

        # Node.js
        if "Node.js" in project_types:
            steps.append(
                """      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "22" """
            )

            steps.append(
                """      - name: Install Node.js dependencies
        run: |
          npm install"""
            )

            steps.append(
                """      - name: Run Node.js tests
        run: |
          npm test"""
            )

        # Java Maven
        if "Java (Maven)" in project_types:
            steps.append(
                """      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "17" """
            )

            steps.append(
                """      - name: Build with Maven
        run: |
          mvn clean package"""
            )

        # Java Gradle
        if "Java (Gradle)" in project_types:
            steps.append(
                """      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "17" """
            )

            steps.append(
                """      - name: Build with Gradle
        run: |
          ./gradlew build"""
            )

        # Docker
        if "Docker" in project_types:
            steps.append(
                """      - name: Build Docker image
        run: |
          docker build -t devflow-app ."""
            )

        # Unknown project
        if not project_types or project_types == ["Unknown"]:
            steps.append(
                """      - name: Build
        run: echo "Build successful" """
            )

        workflow = """name: DevFlow CI

on:
  push:
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
"""

        workflow += "\n\n".join(steps)

        return workflow