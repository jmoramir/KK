from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_World():
    return 'Hola Mundo'

@app.route('/predict')
def prediciones():
    return 'predicciones'

if __name__ == "__main__":
    app.run( port=5001)
