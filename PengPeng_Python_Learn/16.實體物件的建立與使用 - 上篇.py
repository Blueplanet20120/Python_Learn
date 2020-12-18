# 实体物件的建立與使用 - 上篇 - 实体屬性 Instance Attributes
# class Point:
#     def __init__(self):
#         self.x=3
#         self.x=4
# Point()
#
# Point 实体物件的设计：平面坐标上的点
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 建立第一个实体物件
p1 = Point(3, 4)
print(p1.x, p1.y)  # 实体物件.物体名称
# 建立第二个实体物件
p2 = Point(5, 6)
print(p2.x, p2.y)


# FullName 实体物件的设计：分开记录姓、名资料的全名
class FullName:
    def __init__(self, first, last):
        self.fisrt = first
        self.last = last


name1 = FullName("C.W.", "Peng")
print(name1.fisrt, name1, last)
name2 = FullName("T.Y.", "Lin")
print(name2.fisrt, name2.last)
