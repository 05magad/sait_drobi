from random import randint

from flask import Flask, render_template, request

server = Flask(__name__)


@server.get('/')
def index():
    return render_template('PUBG.html')


@server.get('/email')
def email():
    return render_template('email.html')


@server.get('/phone')
def phone():
    return render_template('phone.html')


@server.post('/email_changed')
def email_changed():
    form = request.form
    new_email = form['new_email']
    if new_email == 'vasya@mail.ru':
        return 'Гуляй, Вася, нельзя тебе менять email'
    else:
        return render_template('GOOD.html', email=new_email)


@server.post('/phone_changer')
def phone_changer():
    form = request.form
    new_phone = form['new_phone']
    print(f'Кто-то сменил либо привязал номер телефона на{new_phone}')
    return render_template('GOOD.html')


@server.get('/img')
def img():
    if randint(0, 1000000) == 1:
        return render_template('IM.html')
    else:
        return 'Тебе не повезло, подарка не получишь'


server.run()