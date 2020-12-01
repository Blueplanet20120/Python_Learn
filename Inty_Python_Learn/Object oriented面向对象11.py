# object oriented 面向对象
# class Student():
#     def eat(self):
#         print("student can eat")
#     def study(self):
#         print("inty can study")

# Student().eat()
# fiut="apple"
# print(fiut.upper())  #upper()这是转换大写的方法

# class Student():  # 单词第一个字母大写
#     def eat(self, name, age):
#         print(name, "student can eat", 'and he is ', age, ' years')
#
#
# Student().eat('perfume: ', '33')  # 数字也要加入'',因为前面是str,不能后面是int


class Student:  # 另一种类写法
    name = 'inty'
    age = 18

    def eat(self):
        print(self.name, "student can eat", 'and he is ', self.age, ' years')

    # 调用静态的方法 不需要定义walk()里面带self,当时不能应用class里面的变量
    @staticmethod
    def walk():
        print("student can walk")


Student().eat()  # 数字也要加入'',因为前面是str,不能后面是int
Student().walk()
