#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_parameter(parameter):
    print(f"{parameter}")
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [i for i in range(int(parameter))]
    return "\n".join(map(str, numbers)) + '\n' 

@app.route('/math/<int:parameter1>/<string:operation>/<int:parameter2>')
def math(parameter1, operation, parameter2):
    if operation == "+":
        return str(parameter1 + parameter2)
    elif operation == "-":
        return str(parameter1 - parameter2)
    elif operation == "*":
        return str(parameter1 * parameter2)
    elif operation == "div":
        return str(parameter1 / parameter2)
    elif operation == "%":
        return str(parameter1 % parameter2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)