#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)


ADMIN_USER_FILE=BASE_DIR + "\db\\admin_user_list"


ADMIN_DIR = os.path.join(BASE_DIR,"db","admin_file")      # admin 用户文件目录
SCHOOL_DIR = os.path.join(BASE_DIR,"db","school")         # school 文件目录
CLASSES_DIR = os.path.join(BASE_DIR,"db","classes")      # classes 文件目录
COURSE_DIR = os.path.join(BASE_DIR,"db","course")        # course 文件目录
STUDENT_DIR = os.path.join(BASE_DIR,"db","student")       # student 文件目录
TEACHER_DIR = os.path.join(BASE_DIR,"db","teacher")       # teacher 文件目录
TEACHER_COURSE_DIR = os.path.join(BASE_DIR,"db","teacher_course")   # teacher与course关联信息文件目录

STUDENT_LOG = os.path.join(BASE_DIR,"logs","student_log.log")    # 学员日志文件
TEACHER_LOG = os.path.join(BASE_DIR,"logs","teacher_log.log")    # 讲师日志文件
ADMIN_LOG = os.path.join(BASE_DIR,"logs","admin_log.log")        # 管理员日志文件



