# 4. ООП - Магические, статичные методы. Гит - слияние веток. Контрольная работа #1
from abc import ABC, abstractmethod

# ---------------- Герои ----------------
class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        return f"{self.name} готов к бою!"


class MageHero(Hero):
    def __init__(self, name, hp, lvl, mp):
        super().__init__(name, hp, lvl)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def __init__(self, name, hp, lvl, mp):
        super().__init__(name, hp, lvl, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


# ---------------- Банк ----------------
class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance       # protected (по соглашению)
        self.__password = password    # private
        self.bank_name = bank_name
        self._authorized = False

    def login(self, password):
        if password == self.__password:
            self._authorized = True
            return "✅ Авторизация успешна"
        return "❌ Неверный пароль"

    # Свойство для безопасного доступа к информации
    @property
    def full_info(self):
        if not self._authorized:
            return "❌ Доступ запрещён"
        bonus = self.bonus_for_level()
        return (
            f"Банк: {self.bank_name}\n"
            f"Владелец: {self.hero.name}\n"
            f"HP: {getattr(self.hero, 'hp', 'Нет данных')}\n"
            f"Уровень: {getattr(self.hero, 'lvl', 'Нет данных')}\n"
            f"Баланс: {self._balance}\n"
            f"Бонус за уровень: {bonus}\n"
            f"Итого с бонусом: {self._balance + bonus}"
        )

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return getattr(self.hero, "lvl", 0) * 10

    # ---------------- Магические методы ----------------
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        raise TypeError("Нельзя складывать балансы героев разных классов")

    def __eq__(self, other):
        return (type(self.hero) is type(other.hero)) and (self.hero.lvl == other.hero.lvl)


# ---------------- SMS ----------------
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


# ---------------- Пример использования ----------------
mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)

acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")

# Действия героев
print(mage1.action())
print(warrior.action())

# Вывод счетов
print(acc1)
print(acc2)

# Банк и бонус
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

# Магические методы
print("\n=== Проверка __add__ ===")
try:
    print("Сумма счетов двух магов:", acc1 + acc2)
    print("Сумма мага и воина:", acc1 + acc3)
except TypeError as e:
    print("Ошибка:", e)

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

# SMS
kg_sms = KGSms()
ru_sms = RUSms()
print("\nKG SMS:", kg_sms.send_otp("+996777123456"))
print("RU SMS:", ru_sms.send_otp("+79991234567"))

# Полная информация о счете
acc1.login("1234")
print("\nПолная информация:\n", acc1.full_info)