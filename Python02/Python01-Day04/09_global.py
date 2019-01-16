def f1():
    # x = 100 不可以先声明普通变量后又声明为全局
    global x
    x = 100
f1()
print(x)

v = 100
def f2(v):  # 全局变量不可以是函数的形参
    #global v
    v = 300

f2(None)
print(v)
