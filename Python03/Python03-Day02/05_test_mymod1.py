#实例如何导入自定义模块
#使用自定义模块里的数据和函数

import mymod1 as mm

print(mm.name)

mm.PrintMyName()

print(dir(mm))