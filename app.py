from modules.resume_parser import parse_resume
from modules.jd_parser import parse_jd
from modules.analyzer import analyze_match
from modules.optimizer import optimize_resume


def main():
    #   原始简历
    resume_text = """
    张三，本科毕业于清华大学计算机专业。
    熟悉Python、机器学习。
    做过一个RAG项目，实现问答系统。
    """

    #   JD
    jd_text = """
    我们正在招聘AI工程师，要求：
    熟悉Python、机器学习、深度学习；
    有RAG或LLM项目经验优先；
    3年以上相关工作经验。
    """

    #   简历解析
    resume_data = parse_resume(resume_text)

    #   JD解析
    jd_data = parse_jd(jd_text)

    #   匹配分析
    analysis = analyze_match(resume_data, jd_data)

    #   简历优化（核心）
    optimized_result = optimize_resume(resume_text, jd_data, analysis)

    print("\n最终优化结果：\n")
    print(optimized_result)


if __name__ == "__main__":
    main()