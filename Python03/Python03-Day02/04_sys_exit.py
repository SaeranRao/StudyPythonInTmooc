def f():
    print("f开始调用")
    import sys
    sys.exit(0)
    print('f()结束掉用')

f()
print("结束调用")