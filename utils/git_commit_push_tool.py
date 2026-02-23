from git import Repo
import os
from agent.create_file_agent import root_dir

def git_commit_push(branch: str, message: str) -> str:
    """提交更改并推送到远程仓库"""
    repo_path = root_dir
    print(f"repo_path: {repo_path}, branch: {branch}, message: {message}")
    repo = Repo(repo_path)
    # try:
    #     repo.git.fetch("origin")
    # except Exception as e:
    #     repo.git.fetch("origin")

    if branch not in repo.heads:
        repo.git.checkout(
        "-b",
        branch,
        f"origin/{os.getenv('GITHUB_BASE_BRANCH')}"
)
    else:
        repo.git.checkout(branch)

    repo.git.add(A=True)
    repo.index.commit(message)
    repo.remote(name="origin").push(branch)

    return f"Changes pushed to branch {branch}"