from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from deepagents.backends import FilesystemBackend
from agent.create_file_agent import create_file_agent
from agent.create_pr_agent import create_pr_agent
from agent.git_commit_push_agent import create_git_commit_push_agent
import os

load_dotenv()

root_dir ="D:\\workspace\\PythonWorkSpace\\study\\test"

backend=FilesystemBackend(root_dir=root_dir,virtual_mode=False)

def create_agent():
    model = ChatOpenAI(
    model="gpt-5.2", base_url="https://api.vectorengine.ai/v1"
    )
    # 子agent
    create_file_agent  = create_file_agent()
    create_pr_agent = create_pr_agent()
    create_git_commit_push_agent = create_git_commit_push_agent()

    sub_agents = [create_file_agent, create_pr_agent, create_git_commit_push_agent]

    # 主agent
    agent  = create_deep_agent(
        model=model,
        system_prompt="你是一个智能助手。用来创建文件并将文件提交到远程GIT仓库并创建PR等操作。",
        backend=backend,
        subagents=sub_agents
    )

    result = agent.invoke({"messages": [{"role": "user", "content": "请创建一个markdown格式的文件，文件名为demo，里面的内容为hell world。然后提交到远程仓库，并创建一个PR"}]})
    # 打印Agent的响应
    print(result)
    print("============================")
    print(result["messages"][-1].content)

create_agent()