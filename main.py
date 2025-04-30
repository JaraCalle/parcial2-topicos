from flask import Flask, abort

app = Flask(__name__)

def factorial(n):
    if n < 0:
        return
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/<int:number>')
def calcular_factorial(number):
    result = factorial(number)
    return f'El factorial de {number} es 🎉 {result} 🎉'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)