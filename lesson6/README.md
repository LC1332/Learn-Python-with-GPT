# 第六课 AI李白

# 使用的prompt

## 1

```
data/李白.csv 存储了很多李白的诗

对应的格式如下
"""
Title,Content
襄阳曲四首 三,岘山临汉江，水绿沙如雪。上有堕泪碑，青苔久磨灭。
独坐敬亭山,合沓牵数峰，奔地镇平楚。中间最高顶，髣髴接天语。
"""

帮我实现一段Python程序读取这个文件，以

{Title}::{Content}的形式合并标题和诗歌内容为一个字符串

把这些数据读取为一个list
```

## 2

```
我正在学习Python中的List。请用循环的方式生成一个粒子一维布朗运动的数据

以list of float的形式输出，并进行可视化
```

## 3

```
什么是Python中的List，请给我举出基本的例子
```

## 4

```
merged_poems是一个list of string，存储着李白的诗歌

我想看看李白的诗歌中出现概率最高的三十个字是什么，请用python为我实现

去除掉标点符号，将结果用条形图可视化
```

## 5

```
我希望实现一个Python函数 search_character( character, merged_poems )

其中character是有待搜索的汉字， merged_poems是list of string存储了很多诗歌

我希望搜索character在哪几首诗歌中出现了。
```

## 6

```
我希望实现一个Python函数 search_sentence( sentence, merged_poems )

用来查询sentence中的字和那几首古诗中的字的重合度最高

其中sentence是有待搜索的句子， merged_poems是list of string存储了很多诗歌

对于sentence中的每个字 搜索和计数merged_poems中对应字是否出现来累计重合度

把重合度最高的前三首诗歌进行返回
```

## 7

```
我已经实现了search_sentence(sentence, merged_poems ) ，
会根据 sentence，搜索至多三句最接近sentence的李白的诗词，以list of string的形式进行输出

我希望实现一个sentence2prompt( sentence, merged_poems )函数，

根据输入的sentence，返回一个字符串

"""
你扮演唐朝著名诗人李白

参考李白的诗词:
{诗歌一}
{诗歌二}
{诗歌三}

请模仿李白的口吻和经历与我进行对话
"""
```

## 8

```
我已经实现了

{lesson4/libai_gradio.py的代码}

的代码

我希望把其中的system_prompt，替换为

sentence2prompt(sentence, merged_poems)函数的结果

其中sentence2prompt的代码为

{sentence2prompt的代码}

search_sentence的代码为

{search_sentence的代码}

merged_poems的获取方式为

{merged_poems的读取方法}

请为我组合出修改后的代码
```

# Comments

这节课内容上稍微有一点枯燥。其实我们希望有一个课程在项目前提下去学习List的使用，这节课的内容是能实现这个目标，但是有一点枯燥。并且整个书定位是五年级以后的同学学习，所以不适合做数学难度很高的实验。所以例子难度选取上有一点麻烦。