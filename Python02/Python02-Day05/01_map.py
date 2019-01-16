# def pow2(x,y):
#     return x * y

# for x in map(pow2, range(1,10)):
#     print(x)

# for x in map(pow2, range(1,10),range(1,10)):
#     print(x)
# ========================================================
# 练习
# 求 1 ** 2 + 2 ** 2 + 3 ** 2 + ... + 9 ** 2 的和
# 求 1 ** 3 + 2 ** 3 + 3 ** 3 + ... + 9 ** 3 的和
# 求 1 ** 9 + 2 ** 8 + 3 ** 7 + ... + 9 ** 1 的和
def fx1(x):
    return(x ** 2)

def fx2(x):
    return(x ** 3)
    
print(sum(map(fx1,range(1,10))))

print(sum(map(lambda x: x ** 3,range(1,10))))