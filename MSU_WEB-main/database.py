import pickle
import secrets


class Database:
    def create_db(self, name="data.db"):
        self.Users = []
        self.Profiles = []
        with open(name, 'wb') as f:
            pickle.dump(self, f)

    def load_db(self, name="data.db"):
        self.Users = []
        self.Profiles = []
        with open(name, 'rb') as f:
            temp_obj = pickle.load(f)
            self.Users = temp_obj.Users[:]
            self.Profiles = temp_obj.Profiles[:]

    def registration(self, new_user):
        # проверка логина на уникальность
        for i in self.Users:
            if i.login == new_user.login:
                return False, 'Login is not availible'
        # определяем id для нового пользователя
        count = len(self.Users)
        new_user.id = count + 1
        self.Users.append(new_user)
        self.update()
        return True, 'OK'

    def auth(self, auth_user):
        # проверка логина на присутсвие
        for i in self.Users:
            if i.login == auth_user.login:
                if i.check_passwd(auth_user.password):

                    # уникальность ключей
                    while True:
                        key = str(secrets.token_hex())
                        if not self.key_isset(key):
                            break

                    i.session = key
                    self.update()

                    return True, key

                return False, 'Password is not correct'

        return False, 'Login is not correct'

    def update(self, name="data.db"):
        with open(name, 'wb') as f:
            pickle.dump(self, f)

    def key_isset(self, key):
        for i in self.Users:
            if i.session == key:
                return i
        return False

    def view(self):
        print(self.Users)

    # поиск пользователя по куки sid
    def findUserByKey(self, key):
        result = {}
        for i in self.Users:
            if i.session == key:
                result['id'] = i.id
                result['login'] = i.login
                return result

    def findUserByLogin(self, login):
        result = {}
        for i in self.Users:
            if i.login == login:
                result['id'] = i.id
                result['login'] = i.login
                return result
        return None

    def findProfileByUserId(self, id):
        for i in self.Profiles:
            if i.ref_id == id:
                return i
        return None


class User:
    id = 0
    session = ''
    login = "default"
    password = "default"

    def check_password(self, auth_password):
        if self.password == auth_password:
            return True
        return False

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):
        return f"{self.id} {self.login} {self.session}"


class Profile:
    ref_id = 0
    img = "default"
    description = "default"
    skills = []
    wish = []


if __name__ == "__main__":
    db = Database()
    db.load_db()
    print(db.Users)
    print(db.Profiles)
