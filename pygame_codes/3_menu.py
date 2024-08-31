import tkinter as tk
from tkinter import messagebox

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
total_price = 0

# 更新订单信息
def update_order(choice):
    global total_price
    dish, price = menu[choice]
    if choice in order:
        order[choice] += 1
    else:
        order[choice] = 1
    total_price += price
    update_order_list()

# 更新订单列表
def update_order_list():
    order_list.delete(0, tk.END)
    for key, quantity in order.items():
        dish, price = menu[key]
        order_list.insert(tk.END, f"{dish} x {quantity} - {price * quantity}元")

# 确认支付
def confirm_payment():
    if not order:
        messagebox.showinfo("提示", "请至少点一个菜！")
        return
    payment_window = tk.Toplevel(root)
    payment_window.title("确认支付")
    
    tk.Label(payment_window, text="您的订单：").pack()
    
    order_list_payment = tk.Listbox(payment_window, width=50, height=10)
    for key, quantity in order.items():
        dish, price = menu[key]
        order_list_payment.insert(tk.END, f"{dish} x {quantity} - {price * quantity}元")
    order_list_payment.pack()
    
    tk.Label(payment_window, text=f"总计：{total_price}元").pack()
    
    confirm_button = tk.Button(payment_window, text="确认支付", command=complete_payment)
    confirm_button.pack(side=tk.LEFT, padx=10)
    
    continue_order_button = tk.Button(payment_window, text="继续加菜", command=payment_window.destroy)
    continue_order_button.pack(side=tk.RIGHT, padx=10)

# 完成支付
def complete_payment():
    messagebox.showinfo("支付成功", "支付成功！感谢您的光临，祝您用餐愉快！")
    root.destroy()

# 创建主窗口
root = tk.Tk()
root.title("点餐系统")

# 创建菜单列表
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

tk.Label(menu_frame, text="欢迎光临！请选择菜品：").pack()

for key, (dish, price) in menu.items():
    button = tk.Button(menu_frame, text=f"{dish} - {price}元", command=lambda k=key: update_order(k))
    button.pack(fill=tk.X)

# 创建订单列表
order_frame = tk.Frame(root)
order_frame.pack(pady=10)

tk.Label(order_frame, text="您的订单：").pack()

order_list = tk.Listbox(order_frame, width=50, height=10)
order_list.pack()

# 创建支付按钮
payment_button = tk.Button(root, text="确认支付", command=confirm_payment)
payment_button.pack(pady=10)

# 运行主循环
root.mainloop()
