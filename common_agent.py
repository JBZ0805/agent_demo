from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from agent.create_file_agent import create_file_agent
from agent.create_pr_agent import create_pr_agent
from agent.git_commit_push_agent import create_git_commit_push_agent
import os

def create_agent():
    load_dotenv()
    print(os.getenv("OPENAI_API_KEY"))
    model = ChatOpenAI(
    model="gpt-5.2", base_url="https://api.vectorengine.ai/v1"
    )
    # 子agent
    file_agent  = create_file_agent()
    pr_agent = create_pr_agent()
    git_commit_push_agent = create_git_commit_push_agent()

    sub_agents = [file_agent,git_commit_push_agent,pr_agent]

    # 主agent
    agent  = create_deep_agent(
        model=model,
        system_prompt="你是一个智能助手。不要直接回复创建成功。必须调用子agent。创建文件必须调用file_agent，提交代码必须调用git_commit_push_agent，创建PR必须调用create_pr_agent。",
        subagents=sub_agents
    )

    result = agent.invoke({"messages": [{"role": "user", "content": "请创建一个markdown格式的文件，文件名为demo，里面的内容为hell world。创建完成后提交代码并推送到远程仓库feature/test，最后创建一个PR。Pr的标题为Add demo file，内容为This PR adds a demo file."}]})
    # 打印Agent的响应
    print(result)
    print("============================")
    print(result["messages"][-1].content)

create_agent()