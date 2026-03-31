import json
from utils.llm import call_llm
from utils.prompt_template import parse_jd_prompt


def parse_jd(text):
    """
    解析岗位描述（JD）
    """

    #  构造Prompt
    prompt = parse_jd_prompt(text)

    #  调用LLM
    result = call_llm(prompt)

    #  打印原始结果
    print("JD LLM原始输出：", result)

    #  尝试解析JSON
    try:
        data = json.loads(result)
    except:
        #  处理 ```json 包裹情况
        try:
            result = result.strip("```json").strip("```")
            data = json.loads(result)
        except:
            print("⚠️ JD解析失败")
            return None

    return data