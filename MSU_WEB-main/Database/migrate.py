import json

DATA_DST = "Database/"
users = ['12' , '13' , '12763' , '12762']

with open(DATA_DST + "etalon.txt" , "r" , encoding="utf-8") as f:
        etalon = json.loads(f.read())


for i in users:
    with open(DATA_DST +  i + ".txt" , "r" , encoding="utf-8") as f:
        data = json.loads(f.read())
        for key in etalon.keys():
            
            if key == 'id':
                data['id'] = i
                continue

            if not key in data:
                data[key] = etalon[key]

    with open(DATA_DST +  i + ".txt" , "w" , encoding="utf-8") as f:
        f.write( json.dumps(data) )