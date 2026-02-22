from dotenv import load_dotenv
import os

load_dotenv()  # 自动读取当前目录下的 .env

api_key = os.getenv("OPENAI_API_KEY")
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o",base_url="https://api.vectorengine.ai/v1")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"), # 提示 content值的意思是“将英语翻译成意大利语”
    HumanMessage(content="hi!"),
]

model.invoke(messages)
print(model.ou)
