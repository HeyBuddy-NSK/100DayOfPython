from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

user = {'username':'nk_boy'}

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('boot.html',name=user['username'])

if __name__=="__main__":
    app.run(debug=True)