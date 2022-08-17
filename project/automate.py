from datetime import datetime
from tasks import mail_send, check_date
from celery import chain, group


# Send mail within a time range
old_date = datetime.strptime('15-08-2022', "%d-%m-%Y")
new_date = datetime.strptime('17-08-2022', "%d-%m-%Y")
msg = 'Hello and Welcome'
m_address = 'hello@example.com'

workflow = chain(check_date.s(old_date, new_date), mail_send.s(msg, m_address))


