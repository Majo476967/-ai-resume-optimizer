import json
from utils.llm import call_llm
from utils.prompt_template import parse_resume_prompt

def parse_resume(text):
    # 1. 构造prompt
    prompt = parse_resume_prompt(text)

    # 2. 调用LLM
    result = call_llm(prompt)

    print("LLM原始输出：", result)  # 调试用

    # 3. 解析JSON
    try:
        data = json.loads(result)
        return data
    except:
        # 简单容错（处理 ```json 包裹）
        try:
            result = result.strip("```json").strip("```")
            data = json.loads(result)
            return data
        except:
            print("⚠️ JSON解析失败")
            return None