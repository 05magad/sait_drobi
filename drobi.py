from flask import Flask, render_template, request

from main import plus, minus, umnozh, deli

server = Flask(__name__)


@server.get('/')
def dro():
    return render_template('dro.html')


@server.post('/main')
def index():
    # (1, 5, 8)
    a = int(request.form['dro1'])
    b = int(request.form['dro2'])
    v = int(request.form['dro3'])
    d = int(request.form['dro4'])
    c = int(request.form['dro5'])
    z = int(request.form['dro6'])

    if (a != 0 and b < 0) or (d != 0 and c < 0):
        return 'Так нельзя, минус должен стоять у целой части, а не у числителя.'

    drob1 = (a,b,v)
    drob2 = (d,c,z)
    znak = request.form['znak']

    if znak == '+':
        result = plus(drob1, drob2)
    elif znak == '-':
        result = minus(drob1, drob2)
    elif znak == '/':
        result = deli(drob1, drob2)
    elif znak == '*':
        result = umnozh(drob1, drob2)
    return render_template('hero.html', result=result)




server.run(debug=True)
