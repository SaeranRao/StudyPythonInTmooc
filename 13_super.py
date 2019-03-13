class Humman:
    def __init__(self, n, a):
        '''此方法为人的对象添加姓名、年龄
        '''
        self.name = n
        self.age= a
    def info(self):
        print("姓名：",self.name)
        print("年龄：",self.age)

class Student(Humman):
    def __init__(self, n, a, s):
        '''此方法为人的对象添加姓名、年龄、成绩
        '''
        # self.name = n
        # self.age = a
        super().__init__(n , a)
        self.score = s

    def info(self):
        super().info()
        print("成绩：", self.score)

s1 = Student('小张', 18, 100)
s1.info()

