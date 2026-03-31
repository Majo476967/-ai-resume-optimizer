from utils.llm import call_llm
from utils.prompt_template import optimize_resume_with_jd_prompt
from utils.retriever import get_resume_samples


def optimize_resume(resume_text, jd_data, analysis_data):
    """
    根据JD和匹配分析优化简历（RAG增强版）
    """

    # 获取优秀案例（RAG）
    samples = get_resume_samples()

    # 构造Prompt（带知识）
    prompt = optimize_resume_with_jd_prompt(
        resume_text,
        jd_data,
        analysis_data,
        samples
    )

    # 3️⃣ 调用LLM
    result = call_llm(prompt)

    print("优化模块（RAG）LLM原始输出：\n", result)

    return result