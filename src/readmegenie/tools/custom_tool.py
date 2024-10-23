from crewai_tools import BaseTool
import os
import requests
import base64
import json

class GitHubBaseTool(BaseTool):
    """Base class for GitHub tools with shared logic."""

    @staticmethod
    def _parse_repo_env() -> tuple:
        """Parse the GITHUB_REPO environment variable."""
        repo = os.getenv('GITHUB_REPO', '')
        if not repo or '/' not in repo:
            raise ValueError("GITHUB_REPO environment variable must be set to 'owner/repo'.")
        return repo.split('/')


class GitHubFileRetriever(GitHubBaseTool):
    """
        Retrieves a list of all files from the main branch of a GitHub repository.
    """
    name: str = "GitHub File Retriever"
    description: str = (
        "Retrieves all files from the main branch of a GitHub repository."
    )

    def _run(self) -> str:
        try:
            owner, repo_name = self._parse_repo_env()
            url = f"https://api.github.com/repos/{owner}/{repo_name}/git/trees/main?recursive=1"
            response = requests.get(url, headers={"Accept": "application/vnd.github+json"})

            if response.status_code == 200:
                data = response.json()
                files = [item['path'] for item in data.get('tree', []) if item['type'] == 'blob']
                return '|'.join(files)
            return f"Failed to fetch files: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error while retrieving files: {str(e)}"


class GitHubFileContentRetriever(GitHubBaseTool):
    """
        Retrieves the content of a specific file from a GitHub repository.
    """
    name: str = "GitHub File Content Retriever"
    description: str = (
        "Retrieves and returns the content of a file from a GitHub repository."
    )

    def _run(self, file_name: str) -> str:
        """
            Fetch the content of a specific file from the repository.
            file_name: The name of the file to retrieve.
        """
        try:
            owner, repo_name = self._parse_repo_env()
            return json.dumps(self._fetch_file_contents(owner, repo_name, file_name))
        except Exception as e:
            return json.dumps({"error": f"Exception occurred: {str(e)}"})

    def _fetch_file_contents(self, owner: str, repo: str, file_path: str) -> dict:
        """Fetch the content of a specific file from the repository."""
        content_dict = {}
        try:
            url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                content = base64.b64decode(data['content']).decode('utf-8')
                content_dict[file_path] = content
            else:
                content_dict[file_path] = f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            content_dict[file_path] = f"Error: {str(e)}"
        return content_dict