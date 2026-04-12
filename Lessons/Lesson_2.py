# Наследование

# Родительский| Супер класс
class Hero:

    def __init__(self, name, level, health, ):
        self.name = name
        self.level = level
        self.health = health

    def action(self ):
        return f"{self.name} base action"


# Kirito= Hero("Kirito", 1, 100)


class MageHero(Hero):
    def __init__(self, name, level, health, mp):
        super().__init__(name, level, health,)
        self.mp = mp

    def action(self):
        print(f" Hi i'am {self.name} base action")

kirito = Hero("Kirito", 100, 1000)
asuna = MageHero("Asuno", 100, 1000, 100)

# print(kirito.action())
# print(asuna.action())

class Fly:
    @staticmethod
    def action():
        return f" Fly "

class Swim:
    @staticmethod
    def action ():
        return f"Swim "

class Animals(Fly,Swim):
    pass

# duck = Animals()
# print(duck.action())


class A:
    def action(self):
        print("A")

class B(A):
    def action(self):
        super().action()
        print("B")

class C(A):
    def action(self):
        super().action()
        print("C")

class D(B,C):
    def action(self):
        super().action()
        print("D")

TestObj = D()
TestObj.action()

print(D.__mro__)