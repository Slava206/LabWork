class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password):
        return self.__password == password
user = UserAccount("name", "ema il@gmail.com", "secure_password")
print("Пароль правильный:", user.check_password("secure_password"))
# Изменяем пароль
user.set_password("new_secure_password")
# Проверка нового пароля
print("Пароль правильный:", user.check_password("new_secure_password"))
# Проверка неправильного пароля
print("Пароль правильный:", user.check_password("wrong_password"))
