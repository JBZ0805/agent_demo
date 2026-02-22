import requests
import os
from dotenv import load_dotenv

def create_pr(
    head_branch: str,
    title: str,
    body: str
) -> str:
    """创建一个Pull Request"""
    load_dotenv()
    repo_owner = os.getenv("GITHUB_REPO_OWNER")
    repo_name = os.getenv("GITHUB_REPO_NAME")
    base_branch = os.getenv("GITHUB_BASE_BRANCH")
    token = os.getenv("GITHUB_TOKEN")
    print(f"repo_owner: {repo_owner}, repo_name: {repo_name}, base_branch: {base_branch}")
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "title": title,
        "head": head_branch,
        "base": base_branch,
        "body": body
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return f"PR created: {response.json()['html_url']}"
    else:
        return f"Failed to create PR: {response.text}"