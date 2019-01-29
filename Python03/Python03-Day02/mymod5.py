def f1():
    print("f1被调用")

if __name__ == '__main__':
    print("mymod5.py是作为主模块")
    f1()
else:
    print("mymod5.py正被其它模块调用")
    print("模块名为：",__name__)