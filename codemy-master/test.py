import database

db = database.Database()
#code = database.Code()
#db.create_db()
#code.data = '3Fbc46'
#code.href = 'abcd4'
#code.id = 12
#db.Codes.append(code)
#db.update()
db.load_db()
print(db.Codes)
