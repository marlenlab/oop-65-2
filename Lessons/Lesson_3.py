#  3. принципы ООП: Инкапсуляция, Абстракция. Гит - ветки
class BankAccount:

     def __init__(self, login, password, balance):
         self.login = login
         self.password = password
         self.balance = balance

    def get_balance(self):
        return self.balance

ardager = BankAccount("admin", "123456789", 100)
