def mydeco(fn):
    def fx():
        print('++++++++++++++')
        fn()
        print('--------------')
    return fx


@mydeco
def myfunc():
    print("myfunc被调用")

# mydeco(myfunc)
# myfunc = mydeco(myfunc)
# myfunc()
myfunc()