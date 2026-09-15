from github import Github


class GitHubService:

    def __init__(self):
        self.github = Github()

    def get_repository(self, repository_url: str):
        repository_name = repository_url.rstrip("/").split("github.com/")[-1]

        return self.github.get_repo(repository_name)

    def get_repository_info(self, repository_url: str):
        repo = self.get_repository(repository_url)

        return {
            "name": repo.name,
            "full_name": repo.full_name,
            "description": repo.description,
            "default_branch": repo.default_branch,
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "open_issues": repo.open_issues_count,
            "private": repo.private
        }