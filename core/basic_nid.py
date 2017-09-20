#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys
import pickle

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf.commans import create_uuid


class Nid(object):
    def __init__(self,file_path):
        self.Id = create_uuid()
        self.File_path = file_path

    def __str__(self):
        return self.Id

    def get_id_file(self):
        for filename in os.listdir(self.File_path):
            if filename == self.Id:
                file_dir = os.path.join(self.File_path,self.Id)
                return pickle.load(open(file_dir,"rb"))
            return None


class Admin_Nid(Nid):
    def __init__(self,file_path):
        super(Admin_Nid,self).__init__(file_path)


class Classes_Nid(Nid):
    def __init__(self,file_path):
        super(Classes_Nid,self).__init__(file_path)


class Course_Nid(Nid):
    def __init__(self,file_path):
        super(Course_Nid,self).__init__(file_path)


class School_Nid(Nid):
    def __init__(self, file_path):
        super(School_Nid, self).__init__(file_path)


class Teacher_Nid(Nid):
    def __init__(self, file_path):
        super(Teacher_Nid, self).__init__(file_path)


class Teacher_To_Coures_Nid(Nid):
    def __init__(self, file_path):
        super(Teacher_To_Coures_Nid, self).__init__(file_path)


class Student_Nid(Nid):
    def __init__(self, file_path):
        super(Student_Nid, self).__init__(file_path)