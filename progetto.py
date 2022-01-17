from flask import Flask
from entities import User
import sqlite3

app = Flask(__name__)
con = sqlite3.connect('docweb.sqlite')


@app.route('/')
def index():
    gerardo = User('gerardomastrolia@gmail.com', 'Gerardo', 'Mastrolia')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
