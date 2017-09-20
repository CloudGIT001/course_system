#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys
import pickle

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.basic_fun import Student
from core import log_file
from src.basic_student import show_info
from src.basic_student import go_to_class


def student_run():
    while True:
        print("学生登陆视图")
        student_user = input("\033[32;1m学生登陆用户名\033[0m>>:").strip()
        student_pwd = input("\033[32;1m学生登陆密码\033[0m>>:").strip()

        data = Student.stu_login(student_user,student_pwd)
        if data["tag"] == True:
            print("\033[34;1m[%s]学生登陆成功!"%student_user)
            info_str = "[%s]学生登陆成功!"%student_user
            log_file.student_log(info_str)
            file_dir = data["data"]
            while True:
                show_msg = """\033[33;1m
            0:  退出
            1:  查看个人信息
            2:  上课
                \033[0m"""
                print(show_msg)
                Your_choice = input("\033[32;1m请选择操作\033[0m>>:").strip()
                obj = pickle.load(open(file_dir, "rb"))
                if Your_choice == "0":
                    print("学生[%s] 已经成功退出学生视图" % student_user)
                    info_str = "学生员[%s] 已经成功退出学生视图" % student_user
                    log_file.student_log(info_str)
                    exit()

                if Your_choice == "1":
                    show_info(obj)
                    info_str = "%s 学员进行个人信息查询!" % (student_user)
                    log_file.student_log(info_str)
                    continue

                if Your_choice == "2":
                    print("学生上课")
                    go_to_class(obj)
                    info_str = "%s 学员正在上课!" % (student_user)
                    log_file.student_log(info_str)
                    continue

                else:
                    print("\033[31;1m输入错误，请重新输入\033[0m")
                    continue
        else:
            print("\033[31;1m账号或密码错误，请重新输入\033[0m")
            info_str = "%s学生登陆错误"%student_user
            log_file.student_log(info_str)