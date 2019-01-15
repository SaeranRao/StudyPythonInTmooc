var = 100
def f1():
    var = 200
    print("f1里的var=", var)
    def f2():
        #nonlocal var
        var = 300
        print("f2里的var=", var)
    f2()
    print("f2调用结束后f1里的var值集为",var)
f1()
print('全局值var =', var)