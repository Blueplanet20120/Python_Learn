#實體物件的建立與使用 - 下篇
#实体属性 封装在实体物件中的变数
#实体方法 封装在实体物件总的函式

#Point 实体物件的设计：实体物件的平面坐标上的点

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #定义实体方法
    def show(self):
        print(self.x,self.y)
    def distance(self,targetX,targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
p=Point(1,5) #建立实体物件
p.show()     #呼叫实体方法 / 函式
result=p.distance(34,66) #计算坐标1，5 和坐标34，66之间的距离
print(result)
# File 实体物件的设计：包装档案读取的形式
class File:
    def __init__(self,name):
        self.name=name
        self.file=None #尚未开启档案：初始化是None
    def open(self):
        self.file=open(self.name,"r",encoding="utf-8")
    def read(self):
        return self.file.read()
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)
#读取第二个档案
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)