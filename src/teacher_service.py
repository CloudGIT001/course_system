#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys
import pickle

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.basic_fun import Teacher
from core import log_file
from src.basic_teacher import revise_grades
from src.basic_teacher import show_classes_info
from src.basic_teacher import show_teacher_info
from src.basic_teacher import teacher_classes_list


def teacher_run():
    print("讲师视图")
    while True:
        teacher_name = input("\033[32;1m请输入讲师登陆用户名\033[0m>>:").strip()
        teacher_pwd = input("\033[32;1m请输入讲师登陆密码\033[0m>>:").strip()

        data = Teacher.teacher_login(teacher_name,teacher_pwd)

        if data["tag"] == True:
            print('\033[32;1m[%s]讲师登录讲师视图成功\033[0m'%teacher_name)
            info_str = "[%s]讲师成功登录讲师试图" %teacher_name
            log_file.teacher_log(info_str)
            file_dir = data["data"]
            while True:
                obj_teacher = pickle.load(open(file_dir, 'rb'))
                show_msg = """\033[33;1m
        0:  退出
        1:  查看班级学员信息
        2:  管理班级学员成绩
        3:  查看讲师个人信息
                \033[0m"""
                print(show_msg)
                Your_choice = input("\033[32;1m请选择操作\033[0m>>:").strip()

                if Your_choice == "0":
                    print("讲师[%s] 已经成功退出讲师视图" % teacher_name)
                    info_str = "讲师[%s] 已经成功退出讲师视图" % teacher_name
                    log_file.teacher_log(info_str)
                    exit()

                if Your_choice == "1":
                    list = teacher_classes_list(obj_teacher)
                    print("\033[34;1m讲师:[%s],教学的班级信息如下:\033[0m"%obj_teacher.Teacher_name)
                    show_classes_info(list)
                    info_str = "%s 讲师在查看了学员列表"%teacher_name
                    log_file.teacher_log(info_str)
                    continue

                if Your_choice == "2":
                    print("[%s]管理班级学员成绩"%teacher_name)
                    revise_grades()
                    info_str = "%s管理班级学员成绩" % teacher_name
                    log_file.teacher_log(info_str)
                    continue

                if Your_choice == "3":
                    show_teacher_info(obj_teacher)
                    info_str = "%s查看讲师个人信息" % teacher_name
                    log_file.teacher_log(info_str)
                    continue

                else:
                    print("\033[31;1m输入错误，请重新输入\033[0m")
                    continue
        else:
            print("\033[31;1m账号或密码错误，请重新输入\033[0m")
            info_str = "%s讲师登陆错误"%teacher_name
            log_file.teacher_log(info_str)