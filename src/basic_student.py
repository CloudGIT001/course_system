#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import time
import datetime


def show_info(obj):
    info = """\033[34;1m
    学号:{stu_num} 姓名:{stu_name} 年龄:{stu_age} 电话:{stu_phone} 学校名称:{stu_school_name} 学校地址:{stu_school_addr} 班级:{stu_class}
    \033[0m""".format(stu_num=obj.Stu_num,stu_name=obj.Stu_name,stu_age=obj.Stu_age,stu_phone=obj.Stu_phone,
                      stu_school_name=obj.school_id.get_id_file().School_name,
                      stu_school_addr=obj.school_id.get_id_file().School_addr,
                      stu_class=obj.Classes_id.get_id_file().Classes_name)
    print("学员个人详细信息:")
    print(info)


def go_to_class(obj):
    print("学生正在上课")
    t1 = datetime.datetime.now()
    input("\033[32;1m按任意键退出上课\033[0m>>:")
    time.sleep(2)
    t2 = datetime.datetime.now()
    t = t2 - t1
    print("[%s]学员本次上课用时[%s]"%(obj.Stu_name,t))

    return
