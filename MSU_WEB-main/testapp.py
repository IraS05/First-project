import flask
import json
import core
import secrets

app = flask.Flask("app")

count = 0


@app.route("/auth", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("login.html")

    if flask.request.method == "POST":
        data = flask.request.form

        try:
            with open('Database/' + data['login'] + '.txt', 'r', encoding='utf-8') as f:
                user = json.loads(f.read())
                if user['pass'] == data['pass']:
                    response = flask.make_response(flask.render_template('login.html'))
                    key = str(secrets.token_hex())
                    print(key)
                    response.set_cookie('sid', key)
                    return response
                else:
                    return "Неправильный логин или пароль"
        except:
            print("Произошла ошибка")
            return "Неправильный логин или пароль"


@app.route("/reg", methods=["GET", "POST"])
def reg():
    if flask.request.method == "GET":
        return flask.render_template("reg.html")

    if flask.request.method == "POST":
        data = flask.request.form
        print(data)

        with open("Database/" + data['login'] + ".txt", "w", encoding="utf-8") as f:
            f.write(json.dumps(data))

        return "Привет" + data["login"]


# Для тестирования функций
@app.route("/test/<id>", methods=["GET", "POST"])
def test(id):
    print(id)
    profile = core.profile.Profile(id)
    return flask.render_template('profile.html', data=profile.get())


@app.route("/", methods=["GET"])
def index():
    if flask.request.method == "GET":
        print("пришел")
        data = flask.request.args
        if not data:
            # ген случайных wtl
            wtl = ['python', 'gamer', 'english']
            # ген случайных wtt
            wtt = ['guitar', 'singing', 'drawing']

            return flask.render_template('index.html', data={'wtl': wtl, 'wtt': wtt})

        # ищем людей с таким навыком
        result = [
            {'name': 'Иван', 'href': '#'},
            {'name': 'Иван', 'href': '#'},
            {'name': 'Иван', 'href': '#'}]

        return flask.render_template('peoples.html', data=result)


app.run()
