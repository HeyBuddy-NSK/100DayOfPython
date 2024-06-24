from flask_mail import Message
from flask import render_template
from flask import current_app
from app import mail

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
    app = current_app._get_current_object()
    msg = Message(app.config['NKBLOG_MAIL_SUBJECT_PREFIX']+subject,sender=app.config['NKBLOG_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template+'.txt',**kwargs)
    msg.html = render_template(template+'.html',**kwargs)
    thr = Thread(target=send_async_mail,args=[app,msg])
    thr.start()
    print(thr)
    return thr
    # mail.send(msg)