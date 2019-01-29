import sys
for path in sys.path: # 可以将导入的自定义模块放到这些路径下
    print(path)

import mymod3 # 模块的加载时会执行模块内的代码

import mymod3

import importlib
importlib.reload(mymod3)