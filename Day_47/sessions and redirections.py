from flask import Flask, render_template, redirect, request, session, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DipWdasTwstDgh'
bootstrap = Bootstrap(app)
moment = Moment(app)

#  class
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/',methods = ["POST", "GET"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form, name=session.get('name')) 

if __name__=="__main__":
    app.run(debug=True)