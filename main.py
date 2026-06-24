from langchain.messages import (HumanMessage, AIMessage, SystemMessage)
from langchain_google_genai import ChatGoogleGenerativeAI
import load_dotenv
import os

load_dotenv.load_dotenv()

messages = [
    SystemMessage("你是一个问答助手"),
    HumanMessage("我叫小荔枝"),
    AIMessage("你好，小荔枝"),
    HumanMessage("我叫什么名字？")
]

llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemma-4-31b-it"
)
response = llm.invoke(messages)
print(response)