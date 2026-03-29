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


deku = Hero("DeKu", 100, 150, 100)
bakugo = Hero("Bakugo", 100, 200, 75)

print(f"{deku.greeting()}.\n{deku.attack()}.\n{deku.rest()}.")
print(f"Сила: {deku.strength}, Здоровье: {deku.health}\n")

print(f"{bakugo.greeting()}.\n{bakugo.attack()}.\n{bakugo.rest()}.")
print(f"Сила: {bakugo.strength}, Здоровье: {bakugo.health}")
