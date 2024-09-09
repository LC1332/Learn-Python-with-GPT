from zhipuai import ZhipuAI
import gradio as gr
import csv

# sentence2prompt函数
def sentence2prompt(sentence, merged_poems):
    similar_poems = search_sentence(sentence, merged_poems)
    prompt = "你扮演唐朝著名诗人李白\n\n参考李白的诗词:\n"
    for poem in similar_poems:
        prompt += f"{poem}\n"
    prompt += "\n请模仿李白的口吻和经历与我进行对话"
    return prompt

# search_sentence函数
def search_sentence(sentence, merged_poems):
    most_similar_poems = []
    for poem in merged_poems:
        similarity = sum(1 for word in sentence if word in poem)
        most_similar_poems.append((poem, similarity))
    most_similar_poems.sort(key=lambda x: x[1], reverse=True)
    return [poem for poem, _ in most_similar_poems[:3]]

# 读取merged_poems
merged_poems = []
with open('data/李白.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        merged_str = f"{row['Title']}::{row['Content']}"
        merged_poems.append(merged_str)

# get_api_key函数
def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# question2response函数
def question2response(user_input, zhipu_api_key, merged_poems):
    client = ZhipuAI(api_key=zhipu_api_key)
    system_prompt = sentence2prompt(user_input, merged_poems)
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
    )
    return response.choices[0].message.content

with gr.Blocks() as demo:
    zhipu_api_key = get_api_key("data/zhipu_apikey.txt")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = question2response(message, zhipu_api_key, merged_poems)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()
