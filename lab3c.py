#!/usr/bin/env python3
# Author ID: kchen129

def operate(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))        # 15
    print(operate(10, 5, 'subtract'))   # 5
    print(operate(10, 5, 'multiply'))   # 50
    print(operate(5, 50, 'divide'))     # Error: ...
