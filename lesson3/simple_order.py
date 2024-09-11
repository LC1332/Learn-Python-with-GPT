# 菜单及价格
menu = {
    '1': ('宫保鸡丁', 18),
    '2': ('麻婆豆腐', 15),
    '3': ('清蒸鲈鱼', 28),
    '4': ('糖醋排骨', 25),
    '5': ('扬州炒饭', 12)
}

# 初始化订单和状态
order = {}
state = '点餐中'
total_price = 0

# 点餐程序
while True:
    if state == '点餐中':
        print("\n欢迎光临！请选择菜品（输入对应数字）：")
        for key, (dish, price) in menu.items():
            print(f"{key}. {dish} - {price}元")
        choice = input("请选择菜品编号（输入'0'确认点餐）：")
        
        if choice == '0':
            if not order:  # 如果订单为空，提示至少点一个菜
                print("请至少点一个菜！")
                continue
            state = '确认支付'
        elif choice in menu:
            dish, price = menu[choice]
            if choice in order:
                order[choice] += 1
            else:
                order[choice] = 1
            total_price += price
            print(f"已添加 {dish} 到订单中。")
        else:
            print("无效的输入，请输入正确的菜品编号。")
    
    elif state == '确认支付':
        print("\n您的订单：")
        for key, quantity in order.items():
            dish, price = menu[key]
            print(f"{dish} x {quantity} - {price * quantity}元")
        print(f"总计：{total_price}元")
        
        confirm = input("是否确认支付？（输入'1'确认，输入'2'继续加菜）：")
        if confirm == '1':
            state = '完成支付'
        elif confirm == '2':
            state = '点餐中'
        else:
            print("无效的输入，请输入'1'确认支付或'2'继续加菜。")
    
    elif state == '完成支付':
        print("\n支付成功！感谢您的光临，祝您用餐愉快！")
        break
