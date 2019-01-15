# 1.写一个lambda表达式，判断这个数的2次方+1是否能被5整除，如果可以则返回True，否则返回False

fn1 = lambda x:(True if (x**2+1)%5 == 0 else False)
print(fn1(2))

# 2.写一个lambda表达式，求两个变量的最大值：

fn2 = lambda x,y:x if x >= y else y
print(fn2(7,2))