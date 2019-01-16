

v = 100
def fun1():
    v = 200
    print('fun1内的v=', v)
    def fun2():
        v = 300
        print("fun2内的v=", v)
    fun2()
fun1()
print("v =", v)