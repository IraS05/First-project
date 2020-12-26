import pickle


class Database:
    def create_db(self, name="data.db"):
        self.Users = ["sd", "ff"]
        self.Profiles = ["1", "2"]
        with open(name, 'wb') as f:
            pickle.dump(self, f)

    def load_db(self, name="data.db"):
        self.Users = []
        self.Profiles = []
        with open(name, 'rb') as f:
            temp_obj = pickle.load(f)
            self.Users = temp_obj.Users[:]
            self.Profiles = temp_obj.Profiles[:]


class User:
    id = 0
    login = "default"
    password = "default"

    def __init__(login, password):
        self.login = login
        self.password = password


class Profile:
    ref_id = 0
    img = "default"
    description = "default"
    skills = []
    wish = []


if __name__ == "__main__":
    db = Database()
    db.create_db()
    db.load_db()
    print(db.Users)
    print(db.Profiles)
