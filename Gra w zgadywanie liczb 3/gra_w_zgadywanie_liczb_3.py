from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def kalkulator():
    if request.method == 'GET':
        return render_template('guess_start.html')
    else:
        button = request.form['button']
        if button == 'I am ready!':
            maximum = 1000
            minimum = 0
            guess = int((maximum - minimum) / 2 + minimum)
            info = f'Do you think about {guess}?'
            return render_template('guess.html', info=info)
        elif button == 'Too small':
            guess = request.form['minimum']
            info = f'Do you think about {guess}?'
            return render_template('guess.html', info=info)
        elif button == 'Too big':
            guess = request.form['maximum']
            info = f'Do you think about {guess}?'
            return render_template('guess.html', info=info)
        elif button == 'You win!':
            info = 'I knew it! Thank you, it was a pleasure to play with you.'
            return render_template('guess_win.html', info=info)
        elif button == 'Play again':
            return render_template('guess_start.html')
        else:
            pass

        # a = float(request.form['a'])
        # b = float(request.form['b'])
        # op = request.form['op']
        # if op == 'add':
        #     return f'{a} + {b} = {round(a+b, 3)}'
        # if op == 'sub':
        #     return f'{a} - {b} = {round(a-b, 3)}'
        # if op == 'mul':
        #     return f'{a} * {b} = {round(a*b, 3)}'
        # if op == 'div':
        #     return f'{a} / {b} = {round(a/b, 3)}'


# if __name__ == "__main__":
app.run(debug=True, port=5001)
