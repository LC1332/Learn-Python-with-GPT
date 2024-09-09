from zhipuai import ZhipuAI
import gradio as gr
import csv

rag_result = ""

# sentence2prompt函数
def sentence2prompt(sentence, merged_poems):
    similar_poems = search_sentence(sentence, merged_poems)
    prompt = "你扮演唐朝著名诗人李白\n\n参考李白的诗词:\n"
    for poem in similar_poems:
        prompt += f"{poem}\n"

    global rag_result
    rag_result = ""
    for poem in similar_poems:
        rag_result += poem.replace("::","\n") + "\n"
        
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
def question2response(user_input, zhipu_api_key, merged_poems, chat_history, use_rag_radio):
    client = ZhipuAI(api_key=zhipu_api_key)
    if use_rag_radio and use_rag_radio == "使用RAG":
        system_prompt = sentence2prompt(user_input, merged_poems)
    else:
        system_prompt = "你扮演唐朝著名诗人李白，请模仿李白的口吻和经历与我进行对话"
        global rag_result
        rag_result = ""

    messages = [
            {"role": "system", "content": system_prompt},
    ]
    if chat_history:
        for user_msg, bot_msg in chat_history[-2:]:
            if user_msg:
                messages.append({"role": "user", "content": user_msg})
            if bot_msg:
                messages.append({"role": "assistant", "content": bot_msg})

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=messages,
    )
    return response.choices[0].message.content

with gr.Blocks() as demo:
    zhipu_api_key = get_api_key("data/zhipu_apikey.txt")
    chatbot = gr.Chatbot(height = 600)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    use_rag_radio = gr.Radio(choices=["使用RAG", "不使用RAG"], value="使用RAG", label="选择模式")
    rag_search_result = gr.TextArea(label="RAG搜索结果")

    def respond(message, chat_history, use_rag_radio):
        bot_message = question2response(message, zhipu_api_key, merged_poems, chat_history, use_rag_radio)
        chat_history.append((message, bot_message))
        return "", chat_history
    
    def update_rag_result():
        return rag_result

    msg.submit(respond, [msg, chatbot, use_rag_radio], [msg, chatbot]).then(update_rag_result,[], [rag_search_result])

if __name__ == "__main__":
    demo.launch()
