class Human:
    '''此类用于描述人类的共性行为'''
    def say(self,that):#说话
        print("say",that)
    def walk(self,distance):#走路
        print("走了",distance,'公里')

class Student(Human):
    def study(self,subject):
        print("正在学习",subject) 

class Teacher(Human):
    def teach(self,subject):
        print("正在上",subject,"课")


p1 = Student()

p1.study("物理")
p1.say("云里雾里")


