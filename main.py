from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")
@app.route('/resumo')
def resumo():
    return render_template("resume.html")
@app.route('/projetos')
def projetos():
    return render_template("projects.html")
@app.route('/contatos')
def contatos():
    return render_template("contact.html")

if __name__=="__main__":

    app.run()
 