# 在程序中调用大模型

## 1

```
{复制lesson2/idiot_AI.py的代码}

我希望重构这段程序，将字符串处理的部分分离成一个函数question2response，保持程序的整体功能不变
```

## 2

```
给我举一些python中函数实现的例子，并向我介绍关于函数的基础概念
```

## 3

```
我希望实现一个get_api_key函数，这个函数接受一个文件路径作为输入，

读取文本中的内容后，输出一个字符串。

去掉字符串前后的空格和空行

并编写一个例子，读取data/zhipu_apikey.txt的apikey，打印前4和后4个字符
```

## 4

```
ans变量print之后为

"""
CompletionMessage(content='农夫过河的问题是一个经典的逻辑谜题。为了确保狼、羊和白菜都能安全过河，同时满足不能单独相处的条件，可以按照以下步骤进行：\n\n1. 农夫先将羊带到对岸，然后将自己带回来。\n2. 农夫将狼带到对岸，留下狼和羊在另一边。\n3. 农夫再次回到起点，带白菜到对岸。\n4. 农夫放下白菜，然后带羊回到起点。\n5. 最后，农夫将狼带到对岸。\n\n这样，农夫就成功地将狼、羊和白菜都安全地过河了，并且每次过河都满足了不能单独相处的条件。', role='assistant', tool_calls=None)
"""

我要怎么获取ans中的content的字符串
```

## 5


```
{复制刚才能够正常运行的代码}
ans = response.choices[0].message
response_str = ans.content

这段python代码可以正确的运行。response_str可以成功获取到回答的字符串

我希望参考这段代码，实现一个 question2response 函数

这个函数可以接收user_input 字符串

输出回答的字符串
```

## 6

```
{在连续聊天中或者复制正确的question2response调用大语言模型的代码}

这段程序可以正常运行并调用zhipuai的语言模型，对于下面这段代码

{复制之前人工智障聊天的代码}

我希望用zhipuai对应的函数替换掉简易的question2response函数

实现一个真正的打字聊天机器人
```

## 7

```
{复制4_real_zhipu_bot.py的代码，或者使用之前连续对话中确认可以运行的代码}

这段程序可以正常运行。我希望实现一个界面，参考gradio的例子代码

"""
import gradio as gr
import random
import time

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()
"""

为我实现
```

## 8

```
{复制某段能够正确运行的聊天机器人代码}

这段程序可以正常运行，但是我发现聊天机器人不能很好地获得上下文信息

我希望在请求模型response的时候，加入至多一组的上一次的历史问答，请帮我修改
```

## 9

```
{复制question2response以及关联的get_api_key函数的代码}

对于question2response函数，我想放到特定的question2response.py文件中，再在main.py中调用

具体要如何实现。请分别给出question2response.py和main.py同目录或者放在src目录下的情况
```

# Comments

我们知道整套课会有一些人工智能、强交互的内容来吸引学生的注意。但是由于排期的原因

我们需要把前七课放在前半册。这样使用大语言模型和做个背单词软件作为前半册的核心大项目。

所以调用大语言模型和函数定义这两节课就被合并在了一起。如果老师觉得这样有一些难的话，我想可以把函数定义和语言模型调用拆开成两节课来完成。