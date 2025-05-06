'''
6174问题验证
令 a_0 = 1234
定义操作 my_fun 为 用a_0的四个数字组成的最大四位数减去最小四位数 得到新的四位数
操作10次并且输出每次的结果
'''

def my_fun(num):
    # 将数字转换为字符串并拆分为单个数字
    digits = [int(d) for d in str(num).zfill(4)]
    
    # 将数字列表转换为最大和最小的四位数
    max_num = int(''.join(map(str, sorted(digits, reverse=True))))
    min_num = int(''.join(map(str, sorted(digits))))
    
    # 计算差值并返回新的四位数
    new_num = max_num - min_num
    return new_num

if __name__ == "__main__":
    # 初始数字
    a_0 = 1234

    # 进行10次操作并输出结果
    current_num = a_0
    for i in range(10):
        print(f"第{i+1}次操作结果: {current_num}")
        current_num = my_fun(current_num)


        