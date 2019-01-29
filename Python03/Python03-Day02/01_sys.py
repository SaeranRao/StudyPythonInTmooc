import sys
# print(sys.path)
# for k in sys.modules:
#     print(k)


if sys.version[0] == '2':
    print("Python2")
elif sys.version[0] == '3':
    print("Python3")
else:
    print("未知版本")

for i in range(3):
    print(sys.version_info[i])
