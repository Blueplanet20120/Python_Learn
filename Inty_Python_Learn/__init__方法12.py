# __init__方法
# #英文初始化的意思
class Students:
    def __init__(self, name, age):  # __init__有了这个之后好用很多.
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, 'can walk')
        print(self.name, 'is', self.age)


s1 = Students('pre', '18')
s1.walk()

s2 = Students('perfume', '33')
s2.walk()
