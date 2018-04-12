from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>') #wrap o decorador
def index(username):
   return "Hola {} y bienvenido ".format(username)

@app.route('/prime/<int:entero>') #wrap o decorador
def primo(entero):
    inicio = 1
    while(inicio <= entero):
        for i in range(2,inicio):
            if (inicio%i)==0:
                break
        else:
            return 'el numero {} es primo'.format(inicio)
        inicio += 1

