##

from flask import *

app = Flask(__name__, template_folder="frontend", static_folder="frontend")


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/auth", methods=["post", "get"])
def auth():
    if request.method == "POST":
        return render_template("auth.html")
    else:
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        
        return render_template("game.html") 


if __name__ == "__main__":
    app.run(debug=True)