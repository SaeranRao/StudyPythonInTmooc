def div_apple(n):
    print('%d个苹果您想分给几个人' % n)
    s = input('请输入人数：')
    cnt = int(s)
    result = n / cnt
    print("每个人分了", result, '个苹果')

# 以下是调用者
# 通过try-except语句来捕获并处理ValueError类型的错误
try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except (ValueError,ZeroDivisionError):
    print('苹果分配失败，不分了')

print("程序正常退出")