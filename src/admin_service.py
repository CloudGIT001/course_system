#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import log_file
from conf import settings
from src import basic_admin
from core.basic_fun import Admin


def admin_run():
    if basic_admin.file_oper(settings.ADMIN_USER_FILE):
        print("\033[31;1m系统未初始化!\033[0m")
        input("\033[32;1m按[enter]键开始初始化\033[0m")
        basic_admin.initialize_admin()
    else:
        while True:
            admin_user = input("\033[32;1m管理员用户名\033[0m>>:").strip()
            admin_pwd = input("\033[32;1m管理员密码\033[0m>>:").strip()

            data = Admin.admin_login(admin_user,admin_pwd)
            info_str = "管理员:[%s]登陆成功"%admin_user
            log_file.admin_log(info_str)
            if data["tag"] == True:
                print(data["data"])
                while True:
                    show_msg = """\033[33;1m
            0:  退出
            1:  创建学校
            2:  查看学校
            3:  创建课程
            4:  查看课程
            5:  创建讲师
            6:  查看讲师
            7:  创建班级
            8:  查看班级
            9:  创建学员
            10: 查看学员
            11: 课程与讲师关联
            12: 查看课程与讲师关联
                    \033[0m"""
                    print(show_msg)
                    Your_choice = input("\033[32;1m请选择操作\033[0m>>:").strip()
                    if Your_choice == "0":
                        print("管理员[%s] 已经成功退出管理视图"%admin_user)
                        info_str = "管理员:[%s] 已经成功退出管理视图"%admin_user
                        log_file.admin_log(info_str)
                        exit()

                    if Your_choice == "1":
                        basic_admin.create_school()
                        info_str = "管理员:[%s]进行了创建学校!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "2":
                        basic_admin.show_school()
                        info_str = "管理员:[%s]进行了查看学校信息!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "7":
                        basic_admin.create_classes()
                        info_str = "管理员:[%s]进行了创建班级!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "8":
                        basic_admin.show_classes()
                        info_str = "管理员:[%s]进行了查看班级信息!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "5":
                        basic_admin.create_teacher()
                        info_str = "管理员:[%s]进行了创建讲师!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "6":
                        basic_admin.show_teacher()
                        info_str = "管理员:[%s]进行了查看讲师信息!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "3":
                        basic_admin.create_course()
                        info_str = "管理员:[%s]进行了创建课程!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "4":
                        basic_admin.show_course()
                        info_str = "管理员:[%s]进行了查看课程信息!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "11":
                        basic_admin.correlation_course()
                        info_str = "管理员:[%s]进行了课程与讲师关联!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "12":
                        basic_admin.show_teacher_to_course()
                        info_str = "管理员:[%s]进行了查看课程与讲师关联!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "9":
                        basic_admin.create_student()
                        info_str = "管理员:[%s]进行了创建学员!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    if Your_choice == "10":
                        basic_admin.show_student()
                        info_str = "管理员:[%s]进行了查看学员信息!" % admin_user
                        log_file.admin_log(info_str)
                        continue

                    else:
                        print("\033[31;1m选择有误，请重新选择！\033[0m")

            else:
                print("\033[31;1m用户名或密码错误请重输入\033[0m")
                info_str = "管理员:[%s] 登录错误 " % admin_user
                log_file.admin_log(info_str)
