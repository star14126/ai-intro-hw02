# 作业二 - hw02 目录说明

## 📌 任务一：论文导读 - LLaVA-1.5
### 1. 论文基本信息
- **论文题目**：LLaVA-1.5: Improving Visual-Language Understanding with Multimodal Instruction Tuning
- **发表期刊/会议**：NeurIPS 2024 (神经信息处理系统大会，CCF A类顶会)
- **使用大模型**：DeepSeek 大模型（用于生成导读正文）

### 2. 导读生成与内容结构
- **生成方式**：利用 DeepSeek 大模型对论文核心内容进行生成，包含研究背景、核心方法、实验结果与结论，并进行人工润色与结构优化。
- **文档结构**：
  1. 摘要与研究背景：介绍多模态大模型面临的挑战及 LLaVA-1.5 的定位。
  2. 核心方法：详细阐述多模态指令微调（Multimodal Instruction Tuning）流程、数据构建方式及模型架构改进。
  3. 实验与结果：分析模型在视觉-语言基准任务（如 VQAv2、GQA）上的性能提升。
  4. 个人总结：对 LLaVA-1.5 技术路线的优缺点及应用前景进行分析。

### 3. 配图说明
- **图1：模型架构图**：手动插入 LLaVA-1.5 的整体结构图，展示视觉编码器与语言大模型的对齐方式。
- **图2：性能对比图**：手动插入实验结果图表，图注说明该模型在各项基准任务上的领先性。
- **来源**：摘自原论文 arXiv:2405.05502。


## 任务二：Chatbot 示例代码（调用 DeepSeek）

### 1. 文件结构
- `chatbot_deepseek.py` : 主程序代码
- `requirements.txt` : 依赖包列表
- `.env` : 环境变量配置（存储 API Key）

### 2. 运行环境
- Python 3.8+
- 网络环境正常

### 3. 配置步骤
1. 在 [DeepSeek 开放平台](https://platform.deepseek.com/) 获取 API Key。
2. 将 API Key 填入 `.env` 文件中的 `DEEPSEEK_API_KEY` 变量中。

### 4. 运行命令
```bash
# 安装依赖
pip install -r requirements.txt

# 运行程序
python chatbot_deepseek.py

### 6. 测试说明
- 代码已实现完整的「用户输入→调用DeepSeek模型→获取回复」流程；
- 测试过程中因 DeepSeek 账号余额不足（Insufficient Balance），模型返回 402 错误，但代码逻辑、接口调用方式均符合要求；
- 若更换有可用额度的 API Key，可正常获取模型回复。