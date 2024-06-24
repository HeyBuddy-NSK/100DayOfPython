from flask_mail import Message
from flask import render_template

# sending Asynchronous Email

"""
If you sent a few test emails, you likely noticed that the mail.send() function blocks
for a few seconds while the email is sent, making the browser look unresponsive dur‐
ing that time. To avoid unnecessary delays during request handling, the email send
function can be moved to a background thread. E
"""
from threading import Thread
def send_async_mail(app,msg,mail):
    with app.app_context():
        mail.send(msg)

def send_mail(to,subject,template,app,mail,user):
    msg = Message(app.config['NKBLOG_MAIL_SUB_PREFIX']+subject,sender=app.config['NKBLOG_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template+'.txt',user=user)
    msg.html = render_template(template+'.html',user=user)
    thr = Thread(target=send_async_mail,args=[app,msg,mail])
    thr.start()
    print(thr)
    return thr
    # mail.send(msg)