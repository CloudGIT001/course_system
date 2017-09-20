#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.main import admin_view
from core.main import student_view
from core.main import teacher_view
from core.main import initialize
from core.main import logout


def start():
    """
    程序启动函数. 管理员视图、学生视图、讲师视图的登录操作界面
    :return:
    """
    print("\033[32;1m <---- 欢迎使用选课系统程序 ---->\033[0m")
    menu = """\033[33;1m
    0:  退出选课系统程序
    1:  管理员视图
    2:  学生视图
    3:  讲师视图
    \033[0m"""

    while True:
        print(menu)
        user_choice = input("\033[32;1m请选择操作视图\033[0m>>:").strip()
        if user_choice == "0":
            print("退出选课系统程序")
            logout()

        if user_choice == "4":
            initialize()
            continue

        if user_choice == "1":
            print("管理员视图")
            admin_view()
            continue

        if user_choice == "2":
            print("学生视图")
            student_view()
            continue

        if user_choice == "3":
            print("教师视图")
            teacher_view()
            continue

        else:
            print("\n\t\033[31;1m <---输入错误，请重新输入---> \033[0m")

if __name__ == "__main__":
    start()
