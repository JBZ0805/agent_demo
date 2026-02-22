import os
from deepagents.backends import FilesystemBackend

def _safe_path(root_dir: str, file_path: str) -> str:
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

def create_file(backend: FilesystemBackend, file_path: str, content: str):
    '''创建文件'''
    safe_path = _safe_path(file_path)
    backend.write(safe_path,content)