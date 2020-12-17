import random
import string
import os

size = 5
min_size = 3
aaaaaa = 100

def saveCode(code):
    global size
    i = 0
    while True:
        name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
        
        if not os.path.exists("codes/s{}/{}.txt".format(str(size) , name)):

            # Создадим директорию если нет
            if not os.path.exists( "codes/s{}".format(str(size)) ):
                os.makedirs("codes/s{}".format(str(size)))

            # Создаем файл
            f = open("codes/s{}/{}.txt".format(str(size) , name)  , "w" ,encoding="utf-8")
            f.write(code)
            f.close()
            size -= 1
            if size < min_size:
                size = min_size
            return name

        if i == aaaaaa:
            size += 1
            i = 0

        i += 1

def loadCode(id):
    id = str(id)

    size = len(id)
    try:
        with open("codes/s{}/{}.txt".format( str(size) , id ) , "r" , encoding="utf-8") as f:
            code = f.read()
            f.close()
            return code
    except:
        return False

if  __name__ == "__main__":
    for i in range():
        print(saveCode())