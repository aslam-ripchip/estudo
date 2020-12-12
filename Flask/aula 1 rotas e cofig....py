from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return 'Index'

def teste():
    return '<p> testando 1 </p>'

app.add_url_rule('/teste', 'teste', teste)

if __name__== '__main__':
    app.run()
