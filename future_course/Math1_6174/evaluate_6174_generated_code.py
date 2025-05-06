'''
# 验证6174问题
我们已经实现了my_fun，可以from first_try import my_fun 载入
my_fun( num )可以进行一次操作
帮我实现一段python代码，遍历所有的四位数，检查是否所有的数字都在有限操作内会到达6174
'''
from first_try import my_fun

def verify_6174():
    max_iterations = 10  # 最大迭代次数
    
    # 遍历所有四位数
    for num in range(1000, 10000):
        current_num = num
        iterations = 0
        
        # 跳过所有数字相同的四位数
        if len(set(str(current_num))) == 1:
            continue
            
        # 进行迭代直到达到6174或超过最大迭代次数
        while current_num != 6174 and iterations < max_iterations:
            current_num = my_fun(current_num)
            iterations += 1
            
        # 如果超过最大迭代次数仍未达到6174，输出错误信息
        if current_num != 6174:
            print(f"验证失败！数字 {num} 在 {max_iterations} 次迭代后未达到6174")
            return
            
    print("验证成功！所有符合条件的四位数都可在 {max_iterations} 次迭代内达到6174")

if __name__ == "__main__":
    verify_6174()