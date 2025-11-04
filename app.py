from flask import Flask
app = Flask(__name__)

# definir una ruta
@app.route('/')
def inicio():
    return '¡hola mundo desde flask!'
@app.route('/acerca')
def acerca():
    return 'Página acerca de nosotros'
@app.route('/contacto')
def contacto():
    return 'Página de contacto'
@app.route('/saludo')
def saludo():
    return 'Hola!'

# ejecutar la aplicacion
if __name__=='__main__':
    app.run(debug=True)



