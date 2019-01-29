def mydeco(fn):
    def f():
        fn()
        print("World")
    return f # 这个地方注意不要带（）

@mydeco
def f2():
    '''
        大家好，这是装饰器函数
    '''
    print("hello")

print(f2.__doc__)
