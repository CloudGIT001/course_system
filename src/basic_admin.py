#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys
import time
import uuid
import hashlib

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import settings
from core.basic_fun import Admin
from core.basic_fun import School
from core.basic_fun import Classes
from core.basic_fun import Course
from core.basic_fun import Teacher
from core.basic_fun import Student
from core.basic_fun import Teacher_To_Course


def file_oper(name):
    if not os.path.exists(name):
        info = {"北京":[],"上海":[]}
        # file_pick(name,info)
        return True
    else:
        return False


def initialize_admin():
    """
    初始化
    :return:
    """
    try:
        username = input("\033[32;1m请输入初始化用户名\033[0m>>:").strip()
        password = input("\033[32;1m请输入初始化用户密码\033[0m>>:").strip()
        obj = Admin(username,password)
        obj.save()
        print("\n\033[34;1m管理员[%s]创建完成,请知悉使用!"%username)

        with open(settings.ADMIN_USER_FILE,"w") as f:
            f.write("yes")
        return True
    except Exception as e:
        print(e)


def create_school():
    print("创建学校")
    try:
        s_name = input("\033[32;1m请输入创建的学校名称\033[0m>>:").strip()
        s_addr = input("\033[32;1m请输入创建学校的地址\033[0m>>:").strip()

        school_list = [(obj.School_name,obj.School_addr) for obj in School.open_file_list()]
        if (s_name, s_addr) in school_list:
            print("\033[31;1m[%s][%s]校区已经存在，不能重复创建\033[0m"%(s_name,s_addr))
            return
        else:
            obj = School(s_name,s_addr)
            obj.save()
            print("\033[34;1m[%s][%s]校区创建成功.\033[0m"%(s_name,s_addr))
            return
    except Exception as e:
        print(e)


def show_school():
    for obj in School.open_file_list():
        print("\033[34;1m学校名称:[%s] 学校地址:[%s] 学校创建日期[%s]\033[0m"%
              (obj.School_name,obj.School_addr,obj.create_time))


def create_course():
    print("创建课程")
    school_list = School.open_file_list()
    try:
        while True:
            for k , obj in enumerate(school_list):
                print("\033[35;1m学校编号[%s] 学校名称[%s] 校区[%s] \033[0m"%(k,obj,obj.School_addr))

            choice_school = int(input("\033[32;1m请输入选择的学校编号\033[0m>>:").strip())
            school_obj = school_list[choice_school]

            course_name = input("\033[32;1m请输入创建添加的课程名称\033[0m>>:").strip()
            course_period = input("\033[32;1m请输入课程的教学周期\033[0m>>:").strip()
            course_cost = input("\033[32;1m请输入课程的教学费用\033[0m>>:").strip()

            course_list = [(obj.Course_name, obj.school_id.Id) for obj in Course.open_file_list()]
            if (course_name, school_obj.Id) in course_list:
                print("\033[31;1m[%s]课程已经存在,不能重复创建\033[0m" % course_name)
                return
            else:
                obj = Course(course_name, course_period, course_cost, school_obj.Id)
                obj.save()
                print("\033[34;1m课程[%s] 课程周期[%s] 课程费用[%s] 课程创建时间[%s]"%
                      (obj.Course_name, obj.Course_period, obj.Course_cost, obj.create_time))
                return
    except Exception as e:
        print(e)


def show_course():
    for obj in Course.open_file_list():
        print("\033[34;1m校区:[%s][%s] 课程名称:[%s] 课程周期:[%s] 课程费用:[%s] 课程创建时间:[%s]"%
              (obj.school_id.get_id_file().School_name,obj.school_id.get_id_file().School_addr,
               obj.Course_name, obj.Course_period, obj.Course_cost,obj.create_time))


def create_teacher():
    print("创建讲师")
    school_list = School.open_file_list()
    try:
        while True:
            for k,obj in enumerate(school_list):
                print("\033[35;1m学校编号[%s] 学校名称[%s] 校区[%s] \033[0m"%(k,obj,obj.School_addr))
                # print(k,obj,obj.School_name,obj.School_addr)

            choice_school = int(input("\033[32;1m请输入选择的学校编号\033[0m>>:").strip())
            school_obj = school_list[choice_school]

            t_name = input("\033[32;1m请输入创建讲师的姓名\033[0m>>:").strip()
            t_pwd = input("\033[32;1m请输入创建讲师的密码\033[0m>>:").strip()
            t_level = input("\033[32;1m请输入讲师的级别\033[0m>>:").strip()
            t_age = input("\033[32;1m请输入讲师的年龄\033[0m>>:").strip()
            t_sex = input("\033[32;1m请输入讲师的性别\033[0m>>:").strip()

            t_name_list = [(obj.Teacher_name,obj.school_id.Id) for obj in Teacher.open_file_list()]
            if (t_name,school_obj.Id.Id) in t_name_list:
                print("\033[31;1m讲师[%s] 已经存在，不能重复创建!\033[0m"%t_name)
                return
            else:
                obj = Teacher(t_name,t_pwd,t_age,t_sex,t_level,school_obj.Id)
                obj.save()
                print("\033[34;1m校区:[%s][%s] 讲师:[%s] 创建成功.\033[0m"%
                      (obj.school_id.get_id_file().School_name,obj.school_id.get_id_file().School_addr,obj.Teacher_name))
                return
    except Exception as e:
        print(e)


def show_teacher():
    for obj in Teacher.open_file_list():
        print("\033[34;1m校区:[%s][%s] 讲师姓名:[%s] 讲师年龄:[%s] 讲师级别:[%s] 讲师创建时间:[%s]\033[0m"%
              (obj.school_id.get_id_file().School_name,obj.school_id.get_id_file().School_addr,
               obj.Teacher_name,obj.Teacher_age,obj.Teacher_level,obj.create_time))


def create_classes():
    print("创建班级")
    school_list = School.open_file_list()
    try:
        while True:
            for k, obj in enumerate(school_list):

                print("\033[35;1m学校编号[%s] 学校名称[%s] 学校地址[%s] \033[0m"%(k,obj,obj.School_addr))

            choice_school = int(input("\033[32;1m请输入选择的学校编号\033[0m>>:").strip())
            school_obj = school_list[choice_school]
            print(school_obj)
            print(school_obj.Id.Id)

            c_name = input("\033[32;1m请输入创建的班级名称\033[0m>>:").strip()
            c_name_list = [(obj.Classes_name,obj.school_id.Id) for obj in Classes.open_file_list()]
            if (c_name,school_obj.Id.Id) in c_name_list:
                print("\033[31;1m[%s]班级 已经存在，不能重复创建\033[0m"%c_name)
            else:
                teacher_to_course_list = Teacher_To_Course.open_file_list()
                for k,obj in enumerate(teacher_to_course_list):
                    if str(school_obj.Id) == str(obj.school_id.Id):
                        print("\033[34;1m课程编号[%s] --->: 课程讲师与课程[%s]\033[0m"%(k,obj))
                    choice_course = int(input("\033[32;1m请选择讲师与课程\033[0m>>:").strip())
                    teacher_to_course_obj = teacher_to_course_list[choice_course]
                    obj = Classes(school_obj.Id,c_name,teacher_to_course_obj.Id)
                    obj.save()
                    print("\033[34;1m[%s][%s]校区 [%s]班级 创建成功!"%
                          (obj.school_id.get_id_file().School_name,obj.school_id.get_id_file().School_addr,obj.Classes_name))
                    return
                else:
                    print("\033[0m内容错误\033[0m")

    except Exception as e:
        print(e)


def show_classes():
    for obj in Classes.open_file_list():
        print("\033[34;1m[%s] [%s]校区 班级:[%s] 课程:[%s] 讲师:[%s]\033[0m"%
              (obj.school_id.get_id_file().School_name,obj.school_id.get_id_file().School_addr,
               obj.Classes_name,
               obj.teacher_to_course_id.get_id_file().Course_name,
               obj.teacher_to_course_id.get_id_file().Teacher_name,))


def correlation_course():
    print("课程关联")
    try:
        while True:
            school_list = School.open_file_list()
            for k,obj in enumerate(school_list):
                print("\033[34;1m学校编号[%s] 学校名称[%s] 校区地址[%s]\033[0m"%(k,obj,obj.School_addr))
            choice_school = int(input("\033[32;1m请输入学校编号\033[0m>>:").strip())
            school_obj = school_list[choice_school]

            course_list = Course.open_file_list()
            for k,obj in enumerate(course_list):
                if str(obj.school_id.Id) == str(school_obj.Id):
                    print("\033[34;1m课程编号[%s] 课程名称[%s]\033[0m"%(k,obj))
            choice_course = int(input("\033[32;1m请输入课程编号\033[0m>>:").strip())
            course_obj = course_list[choice_course]

            teacher_list = Teacher.open_file_list()
            for k,obj in enumerate(teacher_list):
                if str(obj.school_id.Id) == str(school_obj.Id):
                    print("\033[34;1m讲师编号[%s] 讲师姓名[%s]"%(k,obj))
            choice_teacher = int(input("\033[32;1m请输入讲师编号\033[0m>>:").strip())
            teacher_obj = teacher_list[choice_teacher]

            c_name_obj = [(obj.Classes_name,obj.Teacher_name,obj.school_id.Id)
                          for obj in Teacher_To_Course.open_file_list()]

            if (course_obj.Course_name,teacher_obj.Teacher_name,school_obj.Id.Id) in c_name_obj:
                print("\033[31;1m[%s] [%s]校区 ,课程[%s]与[%s] 已经关联,不能重复关联\033[0m"%
                      (obj.school_id.get_id_file().School_name,
                       obj.school_id.get_id_file().School_addr,
                       course_obj.Course_name,teacher_obj.Teacher_name))
                return
            else:
                obj = Teacher_To_Course(course_obj.Course_name,teacher_obj.Teacher_name,school_obj.Id)
                obj.save()
                print("\033[31;1m[%s] [%s]校区 ,课程[%s]与[%s] 关联成功\033[0m"%
                      (obj.school_id.get_id_file().School_name,
                       obj.school_id.get_id_file().School_addr,
                       course_obj.Course_name,teacher_obj.Teacher_name))
                return
    except Exception as e:
        print(e)


def show_teacher_to_course():
    for obj in Teacher_To_Course.open_file_list():
        print("\033[34;1m[%s] [%s]校区 课程:[%s] 讲师:[%s]\033[0m"%
              (obj.school_id.get_id_file().School_name,obj.school_id.get_id_file().School_addr,
               obj.Course_name,obj.Teacher_name))


def create_student():
    print("创建学生信息")
    try:
        while True:
            school_list = School.open_file_list()
            for k,obj in enumerate(school_list):
                print("\033[34;1m学校编号[%s] 学校名称[%s] 学校地址[%s]\033[0m"%(k,obj,obj.School_addr))
            choice_school = int(input("\033[32;1m请选择学校编号\033[0m>>:").strip())
            s_name_list = [(obj.stu_num,obj.stu_name) for obj in Student.open_file_list()]
            school_obj = school_list[choice_school]

            s_stu_num = input("\033[32;1m请输入学员学号\033[0m>>:")
            if s_stu_num in s_name_list:
                print("\033[31;1m学号:[]已经创建,不能重复创建\033[0m")
                return
            s_stu_name = input("\033[32;1m请输入学员姓名\033[0m>>:").strip()
            s_stu_pwd = input("\033[32;1m请输入学员系统密码\033[0m>>:").strip()
            s_stu_phone = input("\033[32;1m请输入学员电话号码\033[0m>>:").strip()
            s_stu_age = input("\033[32;1m请输入学员年龄\033[0m>>:").strip()

            s_classes_list = Classes.open_file_list()
            for k,obj in enumerate(s_classes_list):
                print("\033[34;1m班级编号[%s] 班级名称[%s]" % (k, obj))
                if str(obj.school_id.Id) == str(school_obj.Id):
                    print("\033[34;1m班级编号[%s] 班级名称[%s]"%(k,obj))
            choice_classes = int(input("\033[32;1m请选择班级\033[0m>>:").strip())
            classes_name_obj = s_classes_list[choice_classes]
            obj = Student(s_stu_num,s_stu_name,s_stu_pwd,s_stu_age,school_obj.Id,classes_name_obj.Id,s_stu_phone)
            obj.save()
            print("\033[34;1m[%s][%s]校区 学号为:[%s]的学生[%s] 添加成功!"%
                  (obj.school_id.get_id_file().School_name,
                   obj.school_id.get_id_file().School_addr,
                   s_stu_num,s_stu_name))
            return

    except Exception as e:
        print(e)


def show_student():
    for obj in Student.open_file_list():
        print("\033[34;1m[%s] [%s]校区 学员编号:[%s] 学员姓名:[%s] 年龄:[%s] 电话:[%s] 所在班级:[%s]\033[0m"%
              (obj.school_id.get_id_file().School_name,obj.school_id.get_id_file().School_addr,
               obj.Stu_num,obj.Stu_name,obj.Stu_age,obj.Stu_phone,obj.Classes_id.get_id_file().Classes_name))

















