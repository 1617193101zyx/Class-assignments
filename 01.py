#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Student:
   '所有学生的基类'
  stu_count = 0
  stu_count_wangluo161 = 0
  stu_count_wangluo161 = 0
  
   def __init__(self,stu_no, name,stu_class,male,stu_count):
      self.name = name
      self.stu_no = stu_no
      self.stu_class = stu_class
      self.male = male
      Student.stu_count += 1
      if self.stu_class=='wangluo161':
	      Student.stu_count_wangluo161 +=1
	      elif self.stu_class=='wangluo161':
		      Student.stu_count_wangluo161 +=1
	
   def displayStudent(self):
     print "Name :",self.name,",stu_no",self.stu_no,"stu_class",self.stu_class
   def displayCount(self):
      print"Count:",Student,stu_count
 
