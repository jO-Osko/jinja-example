from flask import Flask, render_template, request, make_response

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index_page():
    user = get_user()
    return render_template("index.html", user=user)


@app.route("/login", methods=["GET"])
def login_page_get():
    user = get_user()
    return render_template("login.html", user=user)


@app.route("/login", methods=["POST"])
def login_page_post():
    username = request.form.get("username")
    password = request.form.get("password")
    response = make_response(
        render_template("success.html", user=username)
    )
    response.set_cookie("username", username)
    return response


@app.route("/logout")
def logout():
    response = make_response(
        render_template("logout_success.html")
    )
    response.set_cookie("username", "", expires=0)
    return response


def get_user():
    return request.cookies.get("username")


class Uporabnik:
    def __init__(self, ime, priimek):
        self.ime = ime
        self.priimek = priimek

    def polno_ime(self):
        return f"{self.priimek}, {self.ime}"

    # To je posebna metoda, ki pove, kako se objekt izpisuje
    # Uporablja se takrat, ko poskušamo na objektu uporabiti str (ga pretvoriti v niz)
    def __str__(self):
        return f"Sem uporabnik po imenu: {self.polno_ime()}"


@app.route("/advanced")
def advanced_view():
    # Jinja je sposobna uporabljati cel kup pythonskih klicev
    full_user = Uporabnik("Neko Ime", "Priimek")
    return render_template("advanced.html", user=full_user)

if __name__ == '__main__':
    app.run()
