import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ARK_API_KEY")

def call_llm(prompt):
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "doubao-1-5-lite-32k-250115",  # 可以后面升级
        "messages": [
            {"role": "system", "content": "你是一个专业的简历优化助手"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        print("请求失败：", response.text)
        return None

    result = response.json()
    return result["choices"][0]["message"]["content"]