# Наследование


# Родительский| Супер класс
class Hero:

    def __init__(self, name, level, health, ):
        self.name = name
        self.level = level
        self.health = health

    def action(self ):
        return f"{self.name} base action"


kirito= Hero("Kirito", 1, 100)

# Дочерний класс
class MageHero:
    pass

    def __init__(self):


    def action(self):
        print(f"Hi i am{self.name} base action")




asuno = Hero("Asuno", 100, 1000)


asuno.action()



