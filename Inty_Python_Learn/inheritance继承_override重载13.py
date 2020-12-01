# inheritance继承_override重载

class Fater:
    name = 'inty'

    def eat(self):
        print("father can eat")


class Son():
    def eat(self):
        pass


littleInty = Son()
littleInty.eat()
