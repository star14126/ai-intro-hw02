import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 调试：打印读取到的 API Key（运行成功后可以删掉这行）
print("读取到的 API Key：", os.getenv("DEEPSEEK_API_KEY"))

# 初始化 DeepSeek 客户端（语法完全正确）
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def chat_with_deepseek(user_input):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"调用失败：{str(e)}"

if __name__ == "__main__":
    print("🤖 DeepSeek Chatbot 已启动（输入 quit 退出）")
    while True:
        user_input = input("\n你：")
        if user_input.lower() in ["quit", "q", "退出"]:
            print("👋 再见！")
            break
        reply = chat_with_deepseek(user_input)
        print(f"🤖 DeepSeek：{reply}")