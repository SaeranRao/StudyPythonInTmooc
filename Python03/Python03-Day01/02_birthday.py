# 练习
#   写一个程序，输入你的出生日期
#   1）算出你已经出生了多少天？
#   2）算出你出生那天是星期几？

import time
# 写一个程序，输入你的出生日期
year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))

birthday_second = time.mktime((year,month,day))
help(time)