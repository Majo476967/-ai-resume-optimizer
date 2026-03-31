import json
from utils.llm import call_llm
from utils.prompt_template import match_analysis_prompt


def analyze_match(resume_data, jd_data):
    """
    简历与岗位匹配分析
    """

    #   构造Prompt
    prompt = match_analysis_prompt(resume_data, jd_data)

    #   调用LLM
    result = call_llm(prompt)

    print("匹配分析 LLM原始输出：", result)

    #   JSON解析
    try:
        data = json.loads(result)
    except:
        try:
            result = result.strip("```json").strip("```")
            data = json.loads(result)
        except:
            print("⚠️ 匹配分析解析失败")
            return None

    return data