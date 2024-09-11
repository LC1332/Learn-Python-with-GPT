while True:
    user_input = input("请输入一句话: ")

    # 去除前后的空白字符
    user_input = user_input.strip()

    # 检查末尾是否为 "吗?" 或 "?"，包括中文和英文符号
    if user_input.endswith("吗?") or user_input.endswith("吗？"):
        response = user_input[:-2] + "!"
    elif user_input.endswith("?") or user_input.endswith("？"):
        response = user_input[:-1] + "!"
    else:
        response = user_input

    print("输出:", response)
