# 第七课 背单词软件

# 使用的prompt

## 1

```
我想制作一个Python背单词软件， 用List存储每个单词(english_word)和对应的中文意思(chinese_meaning)

这里List的每个元素用什么类型的结构会比较好？
```

## 2

```
什么是Python中的Dict字典？
```

## 3

```
我正在设计一个背单词的程序

我希望构造word_datas, 一组长度为30的List of Dict, 每个元素有字段 english 和 chinese_meaning

english是单词，chinese_meaning是单词的中文示意

请帮助我用word_datas= [...]的形式生成一组单词表
```

## 4

```
请帮我实现一个WordManager类，包含下面的方法

__init__( word_datas )， 可以通过一个List of Dict初始化，其中每个元素有english和chinese_meaning字段

并且我希望每个单词有一个熟练度"score"，所有的单词初始熟练度定义为20 （可以建立一个english2score的map）

同时定义save()和load( file_name = None ) 的方法，默认把english到熟练度的映射存储在data/word2score.jsonl中，第一次初始化的时候如果没有这个文件，则新建。

定义get_word_data( ) 方法，返回熟练度最低的word_data，如果有数个熟练度相同的单词，随机返回其中一个

定义add_score( english_word , delta = 1) 方法，将word的熟练度增加delta，delta默认为1
定义minus_score( english_word, delta = 1 ) 方法，将word的熟练度减少delta，
同时注意保持熟练度最小值是0 最大值是100

定义get_alternative( english_word, n = 3 )方法，返回一个list of string，返回n个不是word的chinese_meaning

请帮助我实现这个python类，并编写合适的测试。
```

## 5

```
我已经实现了WordManger类，这个类可以用

from WordManager import WordManager
word_datas = [...] # word_datas的赋值语句
word_manager = WordManager(word_datas)

这样的方式载入，对应的功能如下

__init__( word_datas )， 初始化

get_word_data( ) 方法，返回熟练度最低的word （dict形式，有english和chinese_meaning字段）

add_score( english_word , delta = 1) 方法，将word的熟练度增加delta，delta默认为1

minus_score( english_word, delta = 1 ) 方法，将word的熟练度减少delta，

get_alternative( english_word, n = 3 )方法，返回一个list of string，返回n个不是word的chinese_meaning

现在我希望实现一个tinker demo

这个demo每次会用get_word_data()获得一个单词，并渲染在第一个textbox上，label为"选择这个单词的中文意思"

然后使用get_alternative()方法，获得三个额外的chinese_meaning

然后混淆三个备选项和本身word的chinese_meaning，随机显示在4个选项上

当用户选择的时候，如果选择正确，则调用add_score(word)方法，否则，调用minus_score(word)方法

在修改分数之后，调用word_manager.save()保存，然后重新获取一个新的单词进行渲染
```

## 6

```
{复制WordManager.py的代码}

这段python代码可以成功运行，我希望对WordManager类进行修改

将get_word_data() 改为get_word_data(K = 4)

会先从所有数据中，找到K个分数最低的单词，再从中随机挑选一个，返回对应的dict

另外实现一个get_M_words(M = 4)的方法，先从所有数据中，找出2M个分数最低的单词，

再从中随机挑选M个，以list of string的形式返回

并修改对应的测试代码
```

## 7

```
from utils import word_datas
from WordManager import WordManager
manager = WordManager(word_datas)
words = manager.get_M_words()

这段代码可以顺利返回M个 我最不熟悉的单词

我希望实现一个函数words2prompt，输入是words，输出是形如

"""
我正在学习英语，我对下列单词不是很熟悉:

'grape', 'elephant', 'jacket', 'ice'

请帮我用这些单词，生成一个包含这些单词的简短的故事，再将生成的结果翻译回中文
"""

的字符串prompt，把中间的单词替换为对应的words
```

## 8

```
{复制word_mem_simple.py}的代码

这段python代码可以正确运行。我希望在当前界面下方，增加一块新的功能

增加一个一定高度的文本框，再加一个按钮“陌生词造句”

这个按钮会先调用
words = word_manager.get_M_words()

再调用
from words2prompt import words2prompt
prompt = words2prompt(words)

再调用
from question2response import question2response
response = question2response(prompt)

这里的response就是针对M个最不熟悉的词语进行的造句。
```

# Comments

背单词本身是一个不错的案例。但是界面部分5、6的prompt使用的成功率有一点低。这点在录课的时候有一点不流畅。以及后台的部分一次写出所有的需求感觉对同学会有一些难。这部分可能需要整体进行一些修改。
