# def f1():
#     nonlocal x  #报错，因为nonlocal是嵌套在函数内部使用的
#     x = 100
# f1()


# def f1():
#     v = 100
#     def f2():
#         v = 200
#         def f3():
#             nonlocal v  #nonelocal针对最近一次的嵌套函数生效
#             v += 1
#         f3()
#         print("f2最后的 v = ", v)
#     f2()
#     print('f1最后的 v = ', v)
# f1()

def f1(v):
    def f2():
        nonlocal v #    nonlocal声名的变量不可以出现在此函数的列表参数中
        v += 1
    f2()
f1(100)

v = 100
print(v)