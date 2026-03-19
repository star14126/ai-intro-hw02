# 作业二 - hw02 目录说明

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