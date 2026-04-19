import time

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


admin = User("Ardager", "admin")
user = User("Bek", "user")


# Декоратор проверки администратора
def is_admin(func):
    def wrapper(current_user, *args, **kwargs):
        if current_user.role == "admin":
            return func(current_user, *args, **kwargs)
        print("У вас нет доступа")
        return None
    return wrapper


# Функция удаления видео
@is_admin
def delete_video(current_user):
    print(f"{current_user.name} Видео удалено")


# Декоратор таймера
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Время выполнения: {end - start:.1f} секунд")

        return result
    return wrapper


# Функция загрузки видео
@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")


# Проверка работы
delete_video(admin)
delete_video(user)
download_video()