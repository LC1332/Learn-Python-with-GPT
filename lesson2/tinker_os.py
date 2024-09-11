import os
import tkinter as tk
from tkinter import filedialog, messagebox

def scan_directory():
    # 获取用户选择的目录
    directory = filedialog.askdirectory()
    if not directory:
        return

    # 定义一个字典来存储文件类型和对应的计数
    file_types_count = {}

    # 使用os.walk来遍历目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 获取文件扩展名
            file_extension = os.path.splitext(file)[1]

            # 仅统计有扩展名的文件
            if file_extension:
                if file_extension in file_types_count:
                    file_types_count[file_extension] += 1
                else:
                    file_types_count[file_extension] = 1

    # 清空文本框并显示结果
    result_text.delete(1.0, tk.END)
    if file_types_count:
        for file_type, count in file_types_count.items():
            result_text.insert(tk.END, f"文件类型: {file_type}, 出现次数: {count}\n")
    else:
        result_text.insert(tk.END, "没有找到任何文件类型统计信息。")

# 创建主窗口
root = tk.Tk()
root.title("文件类型统计工具")

# 创建按钮来选择目录
select_button = tk.Button(root, text="选择目录并扫描", command=scan_directory)
select_button.pack(pady=10)

# 创建文本框来显示结果
result_text = tk.Text(root, width=50, height=20)
result_text.pack(pady=10)

# 运行主循环
root.mainloop()
