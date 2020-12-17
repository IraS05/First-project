import pickle


class Code():
    data = ''
    id = 0
    href = ''


class Database:
    def create_db(self, name="data.db"):
        self.Codes = []
        with open(name, 'wb') as f:
            pickle.dump(self, f)

    def load_db(self, name="data.db"):
        self.Codes = []
        with open(name, 'rb') as f:
            temp_obj = pickle.load(f)
            self.Codes = temp_obj.Codes[:]

    def update(self, name="data.db"):
        with open(name, 'wb') as f:
            pickle.dump(self, f)

    def save_code(self, code):
        length = len(self.Codes)
        code.id = length + 1
        code.href = code.id
        self.Codes.append(code)
        self.update()
