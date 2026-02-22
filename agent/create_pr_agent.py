from create_pr_tool import create_pr
def create_pr_agent():
    agent = {
        "name": "create_pr_agent",
        "description": "一个专门用来创建Pull Request的Agent，所有PR操作必须通过工具完成。不要直接回复创建成功。",
        "system_prompt": "你是一个PR助手。所有PR操作必须通过工具完成。",
        "tools": [create_pr],
        "model": "gpt-5.2",
        "base_url": "https://api.vectorengine.ai/v1"
    }
    return agent
