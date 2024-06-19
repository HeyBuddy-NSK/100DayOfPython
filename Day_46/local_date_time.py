from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime, timezone

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# print(datetime.now(timezone.utc))

user = {'username':'nk_boy'}

@app.route('/')
@app.route('/index')
def index():
    return render_template('local.html',name=user['username'], current_time=datetime.now(timezone.utc))

if __name__=="__main__":
    app.run(debug=True)