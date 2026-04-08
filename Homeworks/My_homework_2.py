class Hero:
    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

    def greeting(self):
        return f"Привет, я {self.name}, мой уровень {self.lvl}"

    def attack(self):
        self.strength -= 1
        return f"{self.name} наносит удар!"

    def rest(self):
        self.health += 1
        return f"{self.name} отдыхает…"

class Warrior(Hero):
    def __init__(self, name, lvl, health, strength, stamina):
        super().__init__(name, lvl, health, strength,)
        self.stamina = stamina

    def attack(self):
        self.health += 1
        return f"Воин {self.name} атакует мечом!"

class Mage (Hero):
    def __init__(self, name, lvl, health, strength, mana):
        super().__init__(name, lvl, health, strength,)
        self.mana = mana

    def attack(self):
        self.health += 1
        return f"Маг {self.name} кастует заклинание!"

class Assassin (Hero):
    def __init__(self, name, lvl, health, strength, stealth):
        super().__init__(name, lvl, health, strength,)
        self.stealth = stealth

    def attack(self):
        self.health += 1
        return f"Ассасин {self.name} атакует из-под тишка!"

Conan = Warrior("Conan", 100, 100, 100, 100)
Merlin = Mage("Merlin", 100, 100, 100, 100)
Ezio = Assassin("Ezio", 100, 100, 100, 100)

import random

choices = [Conan.name, Merlin.name, Ezio.name]

while True:
    user = input("Выберите героя: Conan, Merlin, Ezio:")

    if user.lower() == "выход":
        print("Игра окончена!")
        break

    if user not in choices:
        print("Такого героя нету")
        continue

    computer = random.choice(choices)

    print("Вы выбрали", user)
    print("Компьютер выбрал", computer)



    if user == computer:
        print("Ничья!")
    elif (user == "Conan" and computer == "Ezio") or \
         (user == "Merlin" and computer == "Conan") or \
         (user == "Ezio" and computer == "Merlin"):
        print("Ты выиграл!")
    else:
        print("Ты проиграл!")


