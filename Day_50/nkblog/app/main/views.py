from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from .forms import NameForm
from ..models import User
from ..email import send_mail
from flask import current_app as app

@main.route('/',methods=['GET','POST'])
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

        return redirect(url_for('.index'))
    
    return render_template('index.html',form=form,name=session.get('name'),
                           known=session.get('known',False),current_time=datetime.utcnow())