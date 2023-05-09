from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Ciao, mondo!'

if __name__ == '__main__':
    app.run()

@app.route('/nome/<string:name>')
def hello_name(name):
    return f'Ciao, {name}!'

@app.route('/somma/<int:num1>/<int:num2>')
def sum_numbers(num1, num2):
    return f'La somma di {num1} e {num2} è {num1 + num2}.'

