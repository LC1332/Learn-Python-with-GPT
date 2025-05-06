from first_try import my_fun

# def my_fun(num):
#     # 将数字转换为字符串并拆分为单个数字
#     digits = [int(d) for d in str(num).zfill(4)]
    
#     # 将数字列表转换为最大和最小的四位数
#     max_num = int(''.join(map(str, sorted(digits, reverse=True))))
#     min_num = int(''.join(map(str, sorted(digits))))
    
#     # 计算差值并返回新的四位数
#     new_num = max_num - min_num
#     return new_num


max_try_times = 100

# 在所有非全同数字中验证6174问题
for num in range(1000, 10000):
    if num % 1111 == 0:  # 跳过全同数字
        continue

    passing_flag = False

    for _ in range(max_try_times):
        num = my_fun(num)
        if num == 6174:
            passing_flag = True
            break
    if not passing_flag:
        print(f"验证失败！数字 {num} 无法经过6174问题验证。")
        break

print("验证完毕")