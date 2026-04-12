from colorama import Fore, Style
from faker import Faker

fake = Faker()

# Эта библиотека нужна для изменения цвета текста в консоли
# Она используется, чтобы делать вывод более наглядным

# Эта библиотека нужна для генерации случайных данных
# Она используется для создания тестовой информации (имена, адреса и т.д.)

print(Fore.GREEN + "Случайные данные:")
print("Имя:", fake.name())
print("Адрес:", fake.address())

print(Style.RESET_ALL)

