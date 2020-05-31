#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import store


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 第一行
        frame1 = tk.Frame(self)
        self.L1 = tk.Label(frame1, text="网站名")
        self.L1.pack(side=tk.LEFT)
        value1=store.get_data("key")
        E1Vaule = tk.StringVar(value=value1)
        self.E1 = tk.Entry(frame1, bd=1, textvariable=E1Vaule)
        self.E1.pack(side=tk.RIGHT)
        frame1.pack(padx=1, pady=1)
        # self.hi_there = tk.Button(self)
        # self.hi_there["width"] = 100
        # self.hi_there["text"] = "Hello World (click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        frame2 = tk.Frame(self)
        self.save = tk.Button(frame2, text="SAVE", fg="red",
                              command=self.save_dat)
        self.save.pack(side="bottom")
        frame2.pack(padx=10, pady=10)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def save_dat(self):
        self.save.focus_set()
        store.set_data("key", self.E1.get())
        print("hi there, everyone!")


root = tk.Tk()
root.title('Python GUI Learning')
root.geometry('380x300')
root.resizable(width=False, height=True)
app = Application(master=root)
app.mainloop()

# from tkinter import Tk
# #初始化Tk()
# myWindow = Tk()
# #设置标题
# myWindow.title('Python GUI Learning')
# #设置窗口大小
# myWindow.geometry('380x300')
# #设置窗口是否可变长、宽，True：可变，False：不可变
# myWindow.resizable(width=False, height=True)
# #进入消息循环
# myWindow.mainloop()
