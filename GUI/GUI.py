import tkinter as tk
from tkinter import messagebox
import math
from caculate import sine, arcsine, cosine, arctan
# 根据选择计算值
def calculate():
    try:
        terms = int(terms_entry.get())
        angle = float(angle_entry.get())
        if angle_unit_var.get() == "Radians":
            angle = math.degrees(angle)
        if operation_var.get() == "Sine":
            result = sine(angle,terms)
        elif operation_var.get() == "Arcsine":
            result = arcsine(angle,terms)
        elif operation_var.get() == "Cosine":
            result = cosine(angle,terms)
        elif operation_var.get() == "Arctan":
            result = arctan(angle,terms)
        
        result_label.config(text=f"计算结果: {result}")
    except ValueError:
        messagebox.showerror("错误", "输入值无效")

#主窗口
root = tk.Tk()
root.title("三角函数计算器")

# 输入
angle_frame = tk.Frame(root)
angle_frame.pack(pady=10)

##
tk.Label(angle_frame, text="角度:").pack(side=tk.LEFT)
angle_entry = tk.Entry(angle_frame)
angle_entry.pack(side=tk.LEFT)
angle_entry.focus()
## 精度
precision_frame = tk.Frame(root)
precision_frame.pack(pady=10)
tk.Label(precision_frame, text="精度:").pack(side=tk.LEFT)
terms_entry = tk.Entry(precision_frame)
terms_entry.pack(side=tk.LEFT)
terms_entry.insert(tk.END, "20")

angle_unit_var = tk.StringVar()
angle_unit_var.set("Degrees")
tk.Radiobutton(angle_frame, text="角度", variable=angle_unit_var, value="Degrees").pack(side=tk.LEFT)
tk.Radiobutton(angle_frame, text="弧度", variable=angle_unit_var, value="Radians").pack(side=tk.LEFT)

# 选择计算方式
operation_frame = tk.Frame(root)
operation_frame.pack(pady=10)

operation_var = tk.StringVar()
operation_var.set("Sine")
operations = ["Sine", "Arcsine", "Cosine", "Arctan"]
for operation in operations:
    tk.Radiobutton(operation_frame, text=operation, variable=operation_var, value=operation).pack(side=tk.LEFT)

# 计算按钮
calculate_button = tk.Button(root, text="计算", command=calculate)
calculate_button.pack(pady=10)

# 结果输出
result_label = tk.Label(root, text="")
result_label.pack()
# 作者信息
author_label = tk.Label(root, text="现代软件工程第13组")
author_label.pack(side=tk.BOTTOM, pady=10)


root.mainloop()
