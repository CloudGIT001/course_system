#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys
import time
import pickle

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import settings
from core.basic_nid import Admin_Nid
from core.basic_nid import Classes_Nid
from core.basic_nid import Course_Nid
from core.basic_nid import School_Nid
from core.basic_nid import Teacher_Nid
from core.basic_nid import Student_Nid
from core.basic_nid import Teacher_To_Coures_Nid


class BasicModel(object):
    def save(self):
        file_dir = os.path.join(self.file_path,str(self.Id))
        pickle.dump(self,open(file_dir,"wb"))

    @classmethod
    def open_file_list(cls):
        list = []
        for file in os.listdir(cls.file_path):
            file_dir = os.path.join(cls.file_path,file)
            list.append(pickle.load(open(file_dir,"rb")))
        return list


class Admin(BasicModel):
    file_path = settings.ADMIN_DIR

    def __init__(self,username,password):
        self.Id = Admin_Nid(self.file_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def admin_login(admin_username,admin_password):
        try:
            for obj in Admin.open_file_list():
                if obj.username == admin_username and obj.password == admin_password:
                    tag = True
                    error = ""
                    data = "\033[33;1m管理员账号登陆成功\033[0m"
                    return {"tag": tag, "error": error, "data": data}
                else:
                    raise Exception("\033[31;1m 管理登陆账号或用户密码输入错误\033[0m")
        except Exception as e:
            tag = False
            error = str(e)
            data = ""
            return {"tag":tag,"error":error,"data":data}


class School(BasicModel):
    file_path = settings.SCHOOL_DIR

    def __init__(self,school_name,school_addr):
        self.School_name = school_name
        self.School_addr = school_addr
        self.Id = School_Nid(self.file_path)
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.School_name


class Classes(BasicModel):
    file_path = settings.CLASSES_DIR
    number = 0

    def __init__(self,school_id,classes_name,teacher_to_course_id):
        self.Classes_name = classes_name
        self.Id = Classes_Nid(self.file_path)
        self.school_id = school_id
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.teacher_to_course_id = teacher_to_course_id

    def __str__(self):
        return self.Classes_name


class Course(BasicModel):
    file_path = settings.COURSE_DIR

    def __init__(self,course_name,course_period,course_cost,school_id):
        self.Id = Course_Nid(self.file_path)
        self.Course_name = course_name
        self.Course_period = course_period
        self.Course_cost = course_cost
        self.school_id = school_id
        self.score = Score(self.Id)
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.Course_name


class Teacher(BasicModel):
    file_path = settings.TEACHER_DIR
    number = 0

    def __init__(self,teacher_name,teacher_pwd,teacher_age,teacher_sex,teacher_level,school_id):
        self.Id = Teacher_Nid(self.file_path)
        self.Teacher_name = teacher_name
        self.Teacher_pwd = teacher_pwd
        self.Teacher_age = teacher_age
        self.Teacher_sex = teacher_sex
        self.Teacher_level = teacher_level
        self.school_id = school_id
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.Teacher_name

    @staticmethod
    def teacher_login(teacher_name,teacher_pwd):
        try:
            for obj in Teacher.open_file_list():
                if obj.Teacher_name == teacher_name and obj.Teacher_pwd == teacher_pwd:
                    tag = True
                    error = ""
                    file_dir = os.path.join(obj.file_path,str(obj.Id))
                    data = file_dir
                    return {"tag": tag, "error": error, "data": data}
                else:
                    raise Exception ("\033[31;1m用户名或密码错误\033[0m")
        except Exception as e:
            tag = False
            error = str(e)
            data = ""
            return {"tag":tag,"error":error,"data":data}


class Teacher_To_Course(BasicModel):
    file_path = settings.TEACHER_COURSE_DIR

    def __init__(self,course_name,teacher_name,school_id):
        self.Id = Teacher_To_Coures_Nid(self.file_path)
        self.Teacher_Course_Name = teacher_name + "<-->" + course_name
        self.Course_name = course_name
        self.Teacher_name = teacher_name
        self.school_id = school_id

    def __str__(self):
        return self.Teacher_Course_Name


class Student(BasicModel):
    file_path = settings.STUDENT_DIR

    def __init__(self,stu_num,stu_name,stu_pwd,stu_age,school_id,classes_id,stu_phone):
        self.Id = Student_Nid(self.file_path)
        self.Stu_num = stu_num
        self.Stu_name = stu_name
        self.Stu_pwd = stu_pwd
        self.Stu_age = stu_age
        self.school_id = school_id
        self.Classes_id = classes_id
        self.Stu_phone = stu_phone
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.Stu_name

    @staticmethod
    def stu_login(username,password):
        try:
            for obj in Student.open_file_list():
                if obj.Stu_name == username and obj.Stu_pwd == password:
                    tag = True
                    error = ""
                    file_dir = os.path.join(obj.file_path,str(obj.Id))
                    data = file_dir
                    return {"tag": tag, "error": error, "data": data}

                else:
                    raise Exception("\033[31;1m用户名或密码错误\033[0m")
        except Exception as e:
            tag = False
            error =str(e)
            data = ""
            return {"tag":tag,"error":error,"data":data}


class Score(BasicModel):
    def __init__(self,nid):
        self.Id = nid
        self.Score_dict = {}

    def set(self,Teacher_To_Course_id,number):
        self.Score_dict[Teacher_To_Course_id] = number

    def get(self,Teacher_To_Course_id):
        return self.Score_dict[Teacher_To_Course_id]

