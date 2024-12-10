import tkinter as tk
from copy_configs import copy_configs
from db_update import db_update
from export_mysql import export_mysql

def safe_execute(func):
    def wrapper():
        try:
            func()
        except Exception as e:
            print(f"Error executing {func.__name__}: {e}")
    return wrapper

def main():
    root = tk.Tk()
    root.title("Configuration Panel")
    root.geometry("400x240")  # 窗口大小
    root.configure(bg="#162A3B")  # 窗口背景颜色

    # 美化按钮样式
    button_style = {
        "width": 23,  # 按钮宽度（字符数）
        "font": ("Arial", 13, "bold"),
        "bg":"#305D82",
        "fg": "white",
        "activebackground": "#84AED1",
        "activeforeground": "white",
    }

    # 按钮生成函数
    def create_button(text, command):
        return tk.Button(root, text=text, command=safe_execute(command), **button_style)

    # 按钮组件
    copy_configs_button = create_button("Backup Configs", copy_configs)
    export_mysql_button = create_button("Backup Database", export_mysql)
    db_update_button = create_button("db_update", db_update)
   
    copy_configs_button.pack(pady=(20, 10))
    # 布局（左右留白和上下间距）
    for button in [export_mysql_button, db_update_button]:
        button.pack(pady=8, padx=50)  # 上下间距为10，左右留白50

    # 启动主窗口
    root.mainloop()

if __name__ == "__main__":
    main()
