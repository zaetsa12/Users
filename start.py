from lib.person import Users

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
user_name = input("Enter your user name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
user = Users(first_name, last_name, user_name, email, password)
# user.show_user_info()
print(
    "===================================================================")
user.register()
print("User is logged in: ", user.check_passw(user_name, password))
print("User '", user.delete_user(user_name), "' has been removed")

# 1. Реєстрацію нового користувача з перевіркою (перевірити чи коистувач вже є в файлі)
# 2. Логін користувача (логін по username з перевіркою паролю.)
# 3. Видалення користувача (по username)
