from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!."

@app.route('/about')
def about():
    return 'this is about page.'

