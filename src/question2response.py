from zhipuai import ZhipuAI

def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def question2response(user_input):
    zhipu_api_key = get_api_key("data/zhipu_apikey.txt")  # 读取API密钥
    client = ZhipuAI(api_key=zhipu_api_key)  # 创建客户端实例
    response = client.chat.completions.create(  # 发送请求
        model="glm-4-flash",
        messages=[
            {"role": "system", "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},
            {"role": "user", "content": user_input}
        ],
    )
    return response.choices[0].message.content  # 返回AI的回答内容

if __name__ == "__main__":
    user_input = "你好，今天天气怎么样？"
    response = question2response(user_input)
    print(response)