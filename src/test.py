#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import Tk
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#设置窗口大小
myWindow.geometry('380x300')
#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=True)
#进入消息循环
myWindow.mainloop()