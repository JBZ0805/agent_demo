from git import Repo
import os

def git_commit_push(branch: str, message: str) -> str:
    """提交更改并推送到远程仓库"""
    repo_path = os.getcwd()
    print(f"repo_path: {repo_path}, branch: {branch}, message: {message}")
    repo = Repo(repo_path)

    if branch not in repo.heads:
        repo.git.checkout('-b', branch)
    else:
        repo.git.checkout(branch)

    repo.git.add(A=True)
    repo.index.commit(message)
    repo.remote(name="origin").push(branch)

    return f"Changes pushed to branch {branch}"