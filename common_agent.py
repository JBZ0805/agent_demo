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
        system_prompt="你是一个智能助手。不要直接回复创建成功。必须要调用子agent。注意子agent的调用顺序，不要并行执行子agent。要先调用创建文件的agent，文件创建完之后再调用提交代码的agent，最后调用创建PR的agent。",
        subagents=sub_agents
    )

    result = agent.invoke({"messages": [{"role": "user", "content": "请创建一个markdown格式的文件，文件名为test2，里面的内容为hello world1。创建完成后提交代码并推送到远程仓库feature/agent_test_fix_one，最后创建一个PR。Pr的标题为AI自己生成的文件，内容为这是一个AI生成的文件。"}]})
    # 打印Agent的响应
    print(result)
    print("============================")
    print(result["messages"][-1].content)

create_agent()