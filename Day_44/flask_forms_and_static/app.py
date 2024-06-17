from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="home page", heading="Welcome to Flask", message="This is a Flask web app starting")

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}"

if __name__=="__main__":
    app.run(debug=True)