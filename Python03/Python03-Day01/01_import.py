# 练习
# 1.输入正方形周长输出正方形面积
# 2.输入圆的半径返回面积
# 3.输入正方形的面积返回周长
# （使用math）
# 1 
import math
c = int(input("请输入正方形的周长"))
print("正方形的面积是",math.pow(c/4,2))
# 2
r = int(input("请输入圆的半径"))
print("圆的的面积是",math.pow(r,2) * math.pi)

# 3
s = int(input("输入正方形的面积"))
print("正方形的周长为",math.sqrt(s)*4)