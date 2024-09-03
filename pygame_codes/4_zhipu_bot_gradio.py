import gradio as gr
from zhipuai import ZhipuAI
import json

def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def question2response(user_input, zhipu_api_key):
    client = ZhipuAI(api_key=zhipu_api_key)  # 创建客户端实例
    response = client.chat.completions.create(  # 发送请求
        model="glm-4-flash",
        messages=[
            {"role": "system", "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},
            {"role": "user", "content": user_input}
        ],
    )
    return response.choices[0].message.content  # 返回AI的回答内容

with gr.Blocks() as demo:
    zhipu_api_key = get_api_key("data/zhipu_apikey.txt")  # 读取API密钥
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = question2response(message, zhipu_api_key)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()
