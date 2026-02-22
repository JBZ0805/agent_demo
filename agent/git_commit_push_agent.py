from utils.git_commit_push_tool import git_commit_push
def create_git_commit_push_agent():
    agent = {
        "name": "create_git_commit_push_agent",
        "description": "一个专门用来提交并推送Git更改的Agent，所有Git操作必须通过工具完成。不要直接回复提交成功。",
        "system_prompt": "你是一个Git助手。所有Git操作必须通过工具完成。",
        "tools": [git_commit_push],
        "model": "gpt-5.2",
        "base_url": "https://api.vectorengine.ai/v1"
    }
    return agent
