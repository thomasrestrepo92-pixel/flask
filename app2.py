from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        return 'Datos recibidos por POST'
    else:
        return 'Mostrando formulario (GET)'

# ejecutar la aplicacion
if __name__=='__main__':
    app.run(debug=True)