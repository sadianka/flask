from flask import Flask, render_template
app = Flask(__name__)

@app.route('/about/<name>')
def about(name):
    return render_template('about.html', name=name)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/osa')
def osa():
    return '<ol><li>Osa</li><li>pszczola</li></ol>'

@app.route('/foto')
def foto():
    return '<img src=https://images.unsplash.com/photo-1448827067615-fa74e848e86c?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D>' 

@app.route('/hello/<name>')
def hello_name(name):
    return f'Witaj, {name}!'

@app.route('/podzielnosc/<liczba>')
def podzielnosc2(liczba):
    if int(liczba)%2==0 & int(liczba)%3==0 & int(liczba)%5==0 :
        return f'{int (liczba)} jest podzielna przez 2, 3, 5'
    elif int(liczba)%2==0 & int(liczba)%3==0 & int(liczba)%5!=0:
        return f'{int (liczba)} jest podzielna przez 2 i 3, ale nie jest podzielna przez 5'
    elif int(liczba)%2==0 & int(liczba)%3!=0 & int(liczba)%5==0:
        return f'{int (liczba)} jest podzielna przez 2 i 5, ale nie jest podzielna przez 3'
    elif int(liczba)%2!=0 & int(liczba)%3==0 & int(liczba)%5==0:
        return f'{int (liczba)} jest podzielna przez 3 i 5, ale nie jest podzielna przez 2'
    elif int(liczba)%2==0 & int(liczba)%3!=0 & int(liczba)%5!=0:
        return f'{int (liczba)} jest podzielna przez 2, ale nie jest podzielna przez 3 i 5'
    elif int(liczba)%2!=0 & int(liczba)%3==0 & int(liczba)%5!=0:
        return f'{int (liczba)} jest podzielna przez 3, ale nie jest podzielna przez 2 i 5'
    elif int(liczba)%2!=0 & int(liczba)%3!=0 & int(liczba)%5==0:
        return f'{int (liczba)} jest podzielna przez 5, ale nie jest podzielna przez 2 i 3'

    
    