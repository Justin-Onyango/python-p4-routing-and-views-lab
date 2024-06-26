#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_parameter(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count_parameter(parameter):
    count = '\n'.join(str(i) for i in range(parameter)) + '\n'
    print(count)
    return count


@app.route('/math/<int:parameter1>/<string:operation>/<int:parameter2>')
def math(parameter1, operation, parameter2):
    if operation == '+':
        result = parameter1 + parameter2
    elif operation == '-':
        result = parameter1 - parameter2
    elif operation == '*':
        result = parameter1 * parameter2
    elif operation == 'div' and parameter2 != 0:
        result = parameter1 / parameter2
    elif operation == '%':
        result = parameter1 % parameter2
      

    return str(result)

    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
