from abc import ABC, abstractmethod

class Hero(ABC):

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health  # приватный атрибут
        self.strength = strength

    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.level}"

    def rest(self):
        self.__health += 1
        return f"{self.name} отдыхает…"

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        return f"Воин {self.name} атакует мечом"


class Mage(Hero):
    def attack(self):
        return f"Маг {self.name} использует магию"


class Assassin(Hero):
    def attack(self):
        return f"Ассасин {self.name} атакует из-под тишка"


Conan = Warrior("Conan", 100, 100, 100)
Merlin = Mage("Merlin", 100, 100, 100)
Ezio = Assassin("Ezio", 100, 100, 100)


for hero in [Conan, Merlin, Ezio]:
    print(hero.greet())
    print(hero.attack())
    print(hero.rest())