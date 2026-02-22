from create_file_tool import create_file
def create_file_agent():
    agent = {
        "name": "create_file_agent",
        "description": "一个专门用来创建文件的Agent，所有文件操作必须通过工具完成。不要直接回复创建成功。",
        "system_prompt": "你是一个文件助手。所有文件操作必须通过工具完成。",
        "tools": [create_file],
        "model": "gpt-5.2",
        "base_url": "https://api.vectorengine.ai/v1"
    }
    return agent
