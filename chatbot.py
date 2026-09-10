import os
from dotenv import load_dotenv
from openai import OpenAI

# 读取 .env
load_dotenv()

# 创建客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

# 对话历史，第一条是系统提示词
messages = [
    {"role": "system", "content": "你是一个友好的中文助手，回答尽量简洁。"}
]

print("输入 exit 退出")

while True:
    user_input = input("你：")
    if user_input.lower() in ["exit", "quit"]:
        break

    # 加入用户消息
    messages.append({"role": "user", "content": user_input})

    # 只保留最近 20 条，避免超出上下文窗口
    messages = messages[-20:]

    # 调用 API
    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=messages,
    )

    # 取出回复
    answer = resp.choices[0].message.content
    print("AI：", answer)

    # 加入 AI 回复
    messages.append({"role": "assistant", "content": answer})