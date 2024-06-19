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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__=="__main__":
    app.run(debug=True)