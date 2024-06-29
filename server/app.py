#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<p>{parameter}</p>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ''.join(f'{num}<br>' for num in range(parameter))
    return f'<p>{numbers}</p>'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400

    return f'<p>{num1} {operation} {num2} = {result}</p>'

if __name__ == '__main__':
    app.run(debug=True)


