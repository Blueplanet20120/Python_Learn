# Module 模組的載入與使用
# import sys
# print(sys.path)
# print(sys.platform)
# from PengPeng_Python_Learn.Modules import geometry #这也是一种加载路径的方法
# import geometry
# result= geometry.distance(1, 1, 3, 4)
# print(result)
# result= geometry.slope(2, 3, 4, 6)
# print(result)

# 调整搜寻模组的路径
import sys

print(sys.path)  # 印出模组的搜寻路径
sys.path.append("Modules")  # 添加python当前路径下的Modules路径
print(sys.path)  # 印出模组的搜寻路径列表

import geometry
result = geometry.distance(1, 1, 3, 4)
print(result)
result = geometry.slope(2, 3, 4, 6)
print(result)
