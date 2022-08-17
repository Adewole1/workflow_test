from conf import app
from datetime import datetime
from django.core.mail import send_mail

@app.task(name='send_mail')
def mail_send(time_range, msg, email, subject='Welcome to automation'):
    if time_range!=False:
        send_mail(
            subject,
            msg,
            'from',
            [email]
        )

@app.task
def check_date(old_date, new_date):
    now = datetime.now()
    if old_date <= now <= new_date:
        return True
    else:
        return False

@app.task
def add_list(email, grp_list):
    if email in grp_list:
        grp_list.append(email)
    else:
        return

@app.task
def rm_list(email, grp_list):
    if email in grp_list:
        grp_list.remove(email)
    else:
        return

@app.task
def add_tags(email, tag):
    pass

@app.task
def rm_tags(email, tag):
    pass

@app.task
def time_delay(time=2):
    return time*60