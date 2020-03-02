# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 19:50
# @Author  : Jackey-lu
# @File    : mian.py

class School:
    def __init__(self,sch_name):
        self.sch_name = sch_name

    def less(self):
        if self.sch_name == 'shanghai':
            lesson = ['go']
        else:
            lesson = ['linux','python']
        return lesson

    def crea_class(self):
        lesson = School.less(self)


obj = School('shanghai').crea_class()

