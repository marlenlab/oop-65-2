class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
    # Метод класса
    def action(self):
        return f"{self.name} готов к бою!"


class MageHero(Hero):
    def __init__(self, name, hp, lvl, mp):
        super().__init__(name, hp, lvl,)
        self.mp = mp

    def action(self):
        return  F"Маг {self.name} кастует заклинание! MP: {self.mp}"

# Merlin = MageHero("Merlin", 100, 100, 1000)
# print(Merlin.action())




class WarriorHero(MageHero):
    def __init__(self, name, hp, lvl, mp=0):
       super().__init__(name, hp, lvl, mp)

    def action(self):
       return F"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

# Conan = WarriorHero("Conan", 100, 100, 250)
# print(Conan.action())


class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name
        self._authorized = False

    def login(self, password):
        if password == self.__password:
            self._authorized = True
            return "✅ Авторизация успешна"
        return "❌ Неверный пароль"

    @property
    def full_info(self):
        if not self._authorized:
            return "❌ Доступ запрещён"
        bonus = self.bonus_for_level()
        info = (
            f"Банк: {self.bank_name}\n"
            f"Владелец: {self.hero.name}\n"
            f"HP: {getattr(self.hero, 'hp', 'Нет данных')}\n"
            f"Уровень: {getattr(self.hero, 'lvl', 'Нет данных')}\n"
            f"Баланс: {self._balance}\n"
            f"Бонус за уровень: {bonus}\n"
            f"Итого с бонусом: {self._balance + bonus}"
        )
        return info

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        if hasattr(self.hero, 'lvl'):
            return self.hero.lvl * 10
        return 0

    # Магические методы
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        raise TypeError("Нельзя складывать балансы героев разных классов")

    def __eq__(self, other):
        return (type(self.hero) is type(other.hero)) and (self.hero.lvl == other.hero.lvl)


from abc import ABC, abstractmethod

class SmsService(ABC):

        @abstractmethod
        def send_otp(self, phone):
            pass


class KGSms(SmsService):

    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):

    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}


mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)
acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")

print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)

# --- Классовые и статические методы ---
print("Банк:", acc1.get_bank_name())
print("Бонус зауровень:", acc1.bonus_for_level(), "SOM")

# --- Магические методы: __add__ ---

print("\n=== Проверка __add__ ===")
try:
    print("Сумма счетов двух магов:", acc1 + acc2)
    print("Сумма мага и воина:", acc1 + acc3)
except TypeError as e:
    print("Ошибка:", e)

# print("\n=== Проверка __add__ ===")
# print("Сумма счетов двух магов:", acc1 + acc2)
#
# print("Сумма мага и воина:", acc1 + acc3)

# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False

# --- SMS ---
sms = KGSms()
print("\n", sms.send_otp("+996777123456"))
