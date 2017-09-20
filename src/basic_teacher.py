#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

from core.basic_fun import Student
from core.basic_fun import Classes


def revise_grades():
    print("\033[31;1m修改班级成绩功能未实现\033[0m")
    input("\n\t\t按任意键退出>>:")
    pass


def teacher_classes_list(t_obj):
    t_c_list = []
    for obj in Classes.open_file_list():
        if t_obj.Teacher_name == obj.teacher_to_course_id.get_id_file().Teacher_name:
            t_c_list.append(obj)
    return t_c_list


def show_classes_info(teacher_classes_list):
    """

    :return:
    """
    while True:
        try:
            for k,obj in enumerate(teacher_classes_list):
                print("\033[34;1m班级编号:[%s] 班级名称:[%s]"%(k,obj))
                choice_classes = int(input("\033[32;1m请选择查看学员信息的班级\033[0m").strip())
                c_classes_obj = teacher_classes_list[choice_classes]
                for obj in Student.open_file_list():
                    if str(obj.Classes_id.get_id_file().Classes_name) == str(c_classes_obj.Classes_name):
                        print("\033[34;1m 学生学号:[%s] 姓名:[%s] 年龄:[%s]"%(obj.Stu_num,obj.Stu_name,obj.Stu_age))
                    else:
                        print("\033[31;1m系统信息错误,为找到相关的班级信息\033[0m")
                return
        except Exception as e:
            print(e)


def show_teacher_info(obj):
    info = """\033[34;1m
    姓名:{t_name} 年龄:{t_age} 性别:{t_sex} 级别:{t_level} 所在学校:{t_school_name} 校区:{t_school_addr}
    \033[0m""".format(t_name=obj.Teacher_name,t_age=obj.Teacher_age,t_sex=obj.Teacher_sex,t_level=obj.Teacher_level,
                      t_school_name=obj.school_id.get_id_file().School_name,
                      t_school_addr=obj.school_id.get_id_file().School_addr)
    print("讲师个人信息:")
    print(info)
