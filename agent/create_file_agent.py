from deepagents.backends import FilesystemBackend
import os

root_dir ="D:\\workspace\\PythonWorkSpace\\study\\test"
backend=FilesystemBackend(root_dir=root_dir,virtual_mode=False)

def _safe_path(file_path: str) -> str:
    """
    强制所有路径限制在 root_dir 内部
    """
    # 1️⃣ 去掉开头的 / 或 \
    file_path = file_path.lstrip("/\\")
        
    # 2️⃣ 拼接 root_dir
    full_path = os.path.join(root_dir, file_path)

    # 3️⃣ 规范化路径
    full_path = os.path.normpath(full_path)

    # 4️⃣ 防止 ../ 逃逸
    root_dir_norm = os.path.normpath(root_dir)

    if not full_path.startswith(root_dir_norm):
        raise ValueError(f"非法路径访问: {file_path}")
    return full_path

def create_file(file_path: str, content: str):
    '''创建文件'''
    safe_path = _safe_path(file_path)
    backend.write(safe_path,content)

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
