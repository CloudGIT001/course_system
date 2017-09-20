#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.admin_service import admin_run
from src.student_service import student_run
from src. teacher_service import teacher_run
from src.basic_admin import initialize_admin


def admin_view():
    """
    跳转到访问管理员视图登录界面
    :return:
    """
    admin_run()


def student_view():
    """
    跳转到访问学生视图登录界面
    :return:
    """
    student_run()


def teacher_view():
    """
    跳转到访问讲师视图登录界面
    :return:
    """
    teacher_run()


def initialize():
    initialize_admin()


def logout():
    """
    退出程序
    :return:
    """
    exit("\n<----- 再见 ----->")