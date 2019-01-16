def get_op(s):
    if s == '+':
        return fn1
    elif s == '-':
        return fn2
    elif s == '*':
        return fn3
    else:
        return fn4

def fn1(a,b):
    return a + b
def fn2(a,b):
    return a - b
def fn3(a,b):
    return a * b
def fn4(a,b):
    return a / b

def caculator():
    while True:
        Fomule = input("请输入计算公式：")
        L = Fomule.split()
        a,s,b = L
        a,b = int(a),int(b)

        fn = get_op(s)
        print(fn(a,b))

caculator()