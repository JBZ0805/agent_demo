from git import Repo

def git_commit_push(repo_path: str, branch: str, message: str) -> str:
    """提交更改并推送到远程仓库"""
    repo = Repo(repo_path)

    if branch not in repo.heads:
        repo.git.checkout('-b', branch)
    else:
        repo.git.checkout(branch)

    repo.git.add(A=True)
    repo.index.commit(message)
    repo.remote(name="origin").push(branch)

    return f"Changes pushed to branch {branch}"