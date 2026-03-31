import streamlit as st

from modules.resume_parser import parse_resume
from modules.jd_parser import parse_jd
from modules.analyzer import analyze_match
from modules.optimizer import optimize_resume


st.title("📄 AI简历优化助手")

# 输入区域
st.header("输入信息")

resume_text = st.text_area("请输入你的简历：", height=150)
jd_text = st.text_area("请输入岗位JD：", height=150)

# 按钮
if st.button("开始分析与优化"):

    if not resume_text or not jd_text:
        st.warning("请填写完整信息")
    else:
        st.info("正在分析，请稍等...")

        # 1. 简历解析
        resume_data = parse_resume(resume_text)

        # 2. JD解析
        jd_data = parse_jd(jd_text)

        # 3. 匹配分析
        analysis = analyze_match(resume_data, jd_data)

        # 4. 优化简历
        optimized_result = optimize_resume(resume_text, jd_data, analysis)

        # 输出结果
        st.header("📊 匹配分析结果")
        st.json(analysis)

        st.header("✨ 优化后的简历")
        st.text(optimized_result)