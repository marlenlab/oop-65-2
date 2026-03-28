from os import name
    # Конструктор класса.
class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
    # Метод класса
    def action(self):
        return f"{self.name} hero bas action!!"
# Метод|Экземпляр на основе класса.
kirito = Hero("Kirito", 100, 100)
asuna = Hero("Asunato", 1000, 1000)

print(kirito.action())
print(asuna.action())

