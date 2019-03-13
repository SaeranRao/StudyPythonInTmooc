class A:
    def work(self):
        print("A's Fn is working...")

class B(A):
    def work(self):
        print("B's Fn is working...")
    def super_work(self):
        # 调用父类的work方法
        # super(B,b).work()
        super().work()

b = B()
# 调用b的父类方法
# b.__class__.__base__.work(b)
# super(B,b).work()
# b.super_work()
b.super_work()