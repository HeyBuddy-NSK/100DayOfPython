from flask import Flask, render_template, redirect, url_for,session,flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Config for web forms
app.config['SECRET_KEY'] = 'ALIEURIFJKZDOIRHQWOIO'
bootstrap = Bootstrap(app)

# Config for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username

with app.app_context():
    db.create_all()    

# forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')


# configuring mail
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['NKBLOG_MAIL_SENDER'] = 'Nkblog Admin admin@nkblog.com'
app.config['NKBLOG_MAIL_SUB_PREFIX'] = '[Nkblog]'
app.config['NKBLOG_ADMIN'] = os.environ.get('NKBLOG_ADMIN')
mail = Mail(app)

# sending mail
# def send_mail(to,subject,template,**kwargs):
#     msg = Message(app.config['NKBLOG_MAIL_SUB_PREFIX']+subject,sender=app.config['NKBLOG_MAIL_SENDER'],
#                   recipients=[to])
#     # msg.body = render_template(template+'.txt',**kwargs)
#     msg.html = render_template(template+'.html',**kwargs)
#     mail.send(msg)


# sending Asynchronous Email

"""
If you sent a few test emails, you likely noticed that the mail.send() function blocks
for a few seconds while the email is sent, making the browser look unresponsive dur‐
ing that time. To avoid unnecessary delays during request handling, the email send
function can be moved to a background thread. E
"""
from threading import Thread
def send_async_mail(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to,subject,template,**kwargs):
    msg = Message(app.config['NKBLOG_MAIL_SUB_PREFIX']+subject,sender=app.config['NKBLOG_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template+'.txt',**kwargs)
    msg.html = render_template(template+'.html',**kwargs)
    thr = Thread(target=send_async_mail,args=[app,msg])
    thr.start()
    print(thr)
    return thr
    # mail.send(msg)

# Index
@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['NKBLOG_ADMIN']:
                send_mail(app.config['NKBLOG_ADMIN'],'New User', 'Mail/new_user',user=user)
                print("mail sent successfully.")
            else:
                print("--no admin mail--")

        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',name=session.get('name'),form=form,known=session.get('known',False))


if __name__=="__main__":
    app.run(debug=True)