if __name__ == "__name__":
    Users


class Users:

    def __init__(self, first_name, last_name, user_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_name = user_name
        self.__email = email
        self.__password = password

    def show_user_info(self):
        print("First name: ", self.__first_name, "\nLast name: ",
              self.__last_name, "\nUsername : ", self.__user_name, "\nPassword :")

    def save_user(self):

        doc = open('db.txt', 'a')
        doc.write(self.__first_name + " # " + self.__last_name + " # " +
                  self.__user_name + " # " + self.__email + " # " + self.__password+"\n")
        doc.close()

    def show_all_users(self):
        users = []
        with open('db.txt') as db_file:
            for line in db_file:
                if len(line.strip()) > 0:
                    user = line.strip()
                    user_info = user.split(" # ")
                    users.append(user_info)
        return users

    def register(self):
        """1. Реєстрація нового користувача з перевіркою (перевірити чи користувач вже є в файлі)
        """
        user = self.__dict__.values()
        all_users = self.show_all_users()
        for item in all_users:
            if item[2] == self.__user_name:
                print("Username '" + item[2] + "' is already exist")
                break
        with open('db.txt', 'a') as doc:
            doc.write(" # ".join(user)+"\n")

    def check_passw(self, user_name, password):
        """2. Логін користувача (логін по username з перевіркою паролю.)
        """
        all_users = self.show_all_users()
        for item in all_users:
            if item[2] == user_name:
                return item[4] == password
        return False

    def delete_user(self, user_name):
        """3. Видалення користувача (по username)
        """
        removed = False
        all_users = self.show_all_users()
        user_name = input("Enter  name to delete: ")
        with open('db.txt', 'w') as db_file:
            for item in all_users:
                if item[2] != user_name:
                    db_file.write(" # ".join(item)+"\n")
                else:
                    removed = True
        return user_name
