def optimize_resume_prompt(text):
    return f"""
你是一名专业的简历优化专家。

请对用户简历进行优化，并严格按照JSON格式输出。

要求：
1. 使用更专业表达
2. 突出技术能力
3. 尽量量化成果

⚠️必须严格返回JSON，不要输出任何多余内容！

格式如下：
{{
  "optimized_text": "优化后的简历内容",
  "improvements": [
    "优化点1",
    "优化点2"
  ]
}}

原始内容：
{text}
"""

def parse_resume_prompt(text):
    return f"""
你是一名专业的HR，请从简历中提取关键信息。

请严格按照JSON格式输出，不要有任何多余内容。

字段要求：
1. education：教育经历（学校+专业）
2. skills：技能列表（⚠️每个技能必须是一个独立词，不要拆分，不要有多余空格）
3. projects：项目经历

格式如下：
{{
  "education": ["xx大学 计算机专业"],
  "skills": ["Python", "机器学习"],
  "projects": ["项目A：做了什么"]
}}

⚠️严格要求：
- skills 必须是干净的词，例如："机器学习"（不能写成"机器 学习"）
- 每个字段必须是列表
- 不要输出解释
- 不要输出markdown
- 不要编造信息
- 没有内容用 []

简历内容：
{text}
"""

def parse_jd_prompt(text):
    return f"""
你是一名专业招聘经理，请从岗位描述中提取关键信息。

请严格按照JSON格式输出，不要有任何多余内容。

字段要求：
1. skills_required：技能要求
2. keywords：关键词
3. experience：经验要求
4. core_requirements：核心技能（必须具备）
5. bonus_skills：加分技能（优先但非必须）

格式如下：
{{
  "skills_required": ["Python", "机器学习"],
  "keywords": ["RAG", "LLM"],
  "experience": "3年以上",
  "core_requirements": ["Python"],
  "bonus_skills": ["RAG"]
}}

⚠️要求：
- core_requirements：JD中明确要求或最关键技能
- bonus_skills：加分项、优先条件
- 不要编造
- 没有内容用 []
- 必须是合法JSON

岗位描述：
{text}
"""

def match_analysis_prompt(resume_data, jd_data):
    return f"""
你是一名专业HR，请根据候选人简历和岗位要求进行匹配分析。

请严格按照JSON格式输出，不要有任何多余内容。

【候选人信息】
{resume_data}

【岗位要求】
{jd_data}

请完成以下分析：

1. match_score：匹配度（0-100分）
2. score_reason：评分原因（为什么是这个分数）
3. strengths：候选人的优势
4. missing_skills：候选人缺失的关键技能

输出格式如下：
{{
  "match_score": 80,
  "score_reason": "具备核心技能但缺少部分经验",
  "strengths": ["具备Python经验"],
  "missing_skills": ["缺少深度学习"]
}}

⚠️要求：
- match_score必须是整数
- score_reason必须简洁清晰
- 不要输出解释
- 必须是合法JSON
"""

def optimize_resume_with_jd_prompt(resume_text, jd_data, analysis_data, resume_samples):
    return f"""
你是一名资深HR和职业顾问，请根据岗位要求优化候选人的简历。

【优秀简历参考】
{resume_samples}

【原始简历】
{resume_text}

【岗位要求（JD）】
{jd_data}

【匹配分析】
{analysis_data}

请完成以下任务：

1. 输出优化后的简历内容（更专业、更匹配岗位）
2. 给出优化说明（说明你做了哪些修改，以及为什么）

输出格式如下：

优化后简历：
xxx

优化说明：
- 修改点1：xxx
- 修改点2：xxx


要求：
- 优化要具体，不要泛泛而谈
- 尽量贴合JD中的关键词和技能
- 绝对不要编造任何不存在的经历或技能
- 不能新增“几年经验”等原简历中没有的信息
- 如果缺少某项技能，可以优化表达，但不能虚构掌握该技能
- 输出必须清晰分为“优化后简历”和“优化说明”
- 参考优秀案例的表达方式
- 不要照抄案例内容
- 不能凭空添加具体数据（如“提升30%”“提高20%”）
- 如果原简历没有量化结果，可以使用“显著提升”“有效优化”等描述
"""