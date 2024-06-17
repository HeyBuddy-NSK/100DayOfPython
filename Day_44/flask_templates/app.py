from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="home page", heading="Welcome to Flask", message="This is a Flask web app starting")

if __name__=="__main__":
    app.run(debug=True)