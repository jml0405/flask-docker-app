from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print('hola mundo')
    return '¡Hola Mundo!'

if __name__ == '__main__':
    app.run()
