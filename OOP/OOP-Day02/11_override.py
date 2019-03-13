class A:
    def work(self):
        print("A's Fn is working...")

class B(A):
    def work(self):
        print("B's Fn is working...")

b = B()
b.work()