class A:
    def __init__(self):
        self.__p1 = 100 # __p1为私有变量

    def test(self):
        print(self.__p1)

    def __fn(self):
        print("A的私有方法")

a = A()
# print(a.__p1) # 在类外部无法查看__p1属性
a.test()
a.__fn() # 在类外部无法调用__fn函数