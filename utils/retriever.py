def get_resume_samples():
    """
    读取优秀简历案例（知识库）
    """
    try:
        with open("data/resume_samples.txt", "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except:
        print("⚠️ 无法读取简历样本")
        return ""