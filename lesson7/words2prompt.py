def words2prompt(words):
    # 将单词列表转换为字符串，每个单词用单引号包围，并用逗号和空格分隔
    words_str = "', '".join(["'{}'".format(word) for word in words])
    
    # 构建prompt字符串
    prompt = (
        "我正在学习英语，我对下列单词不是很熟悉:\n\n"
        f"{words_str}\n\n"
        "请帮我用这些单词，生成一个包含这些单词的简短的故事，再将生成的结果翻译回中文"
    )
    
    return prompt

if __name__ == "__main__":
    from utils import word_datas
    from WordManager import WordManager

    word_manager = WordManager(word_datas)
    words = word_manager.get_M_words()
    
    prompt = words2prompt(words)
    print(prompt)

    from question2response import question2response
    response = question2response(prompt)
    print("---\n",response)

