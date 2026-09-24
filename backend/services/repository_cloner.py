import subprocess
from pathlib import Path


class RepositoryCloner:

    def clone_repository(self, repository_url: str, destination: str):
        destination_path = Path(destination)

        if destination_path.exists():
            raise FileExistsError(
                f"Destination already exists: {destination}"
            )

        try:
            subprocess.run(
                [
                    "git",
                    "clone",
                    repository_url,
                    str(destination_path)
                ],
                check=True,
                capture_output=True,
                text=True
            )

        except subprocess.CalledProcessError as error:
            raise RuntimeError(
                f"Failed to clone repository: {error.stderr.strip()}"
            )

        return str(destination_path)