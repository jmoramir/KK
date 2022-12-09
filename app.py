from flask import Flask,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_World():
    return render_template('index.html')

@app.route('/predict')
def prediciones():
    return 'predicciones'

if __name__ == "__main__":
    app.run()
