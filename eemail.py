import smtplib, ssl
import config

def send_email(title, name, msg, host):
    dict_smtp = {
        'google': {'smtp':"smtp.google.com", 'port': 587},
        'yandex': {'smtp':"smtp.yandex.ru", 'port': 465}
    }
    message = "Subject: {}\n\n{}".format(title, msg)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(dict_smtp[host]['smtp'], dict_smtp[host]['port'], context=context) as server:
        server.ehlo()
        server.login(user=config.EMAIL_ADDRESS, password=config.EMAIL_PASSWORD)
        server.sendmail(from_addr=config.EMAIL_ADDRESS, to_addrs=config.LIST_EMAIL_COLLEAGUES[name], msg=message)

# name = 'honza'
# content = 'Cau Honzo! Jak se dari?'
# send_email(title='Zdravim', name=name, msg=content, host='yandex')