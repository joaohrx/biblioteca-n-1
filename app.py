from flask import Flask
from blueprints.livros import livros_bp
from blueprints.auth import auth_bp
import database


app = Flask(__name__)
app.secret_key = "biblioteca_secreta"

app.register_blueprint(livros_bp)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True)