from zhipuai import ZhipuAI
from src.question2response import question2response

while True:
    user_input = input("请输入一句话: ")
    response = question2response(user_input)
    print("AI输出:", response)
