from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return render_template('result.html', result=result)
    return render_template('index.html')


@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 - num2
        return render_template('result.html', result=result)
    return render_template('index.html')


@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 * num2
        return render_template('result.html', result=result)
    return render_template('index.html')


@app.route('/divide', methods=['GET', 'POST'])
def divide():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if num2 == 0:
            return render_template('error.html', error='Error: Division by zero')
        result = num1 / num2
        return render_template('result.html', result=result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
