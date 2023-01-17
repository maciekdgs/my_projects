from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def kalkulator():
    if request.method == 'GET':
        return render_template('guess_start.html')
    else:
        # minimum = int(request.form['minimum'])
        # maximum = int(request.form['maximum'])
        # guess = int(request.form['guess'])
        button = request.form['button']
        if button == 'I am ready!':
            minimum = 0
            maximum = 1000
            guess = int((maximum - minimum) / 2 + minimum)
            info = f'Do you think about {guess}?'
            return render_template('guess.html', info=info, minimum=minimum, maximum=maximum, guess=guess)
        elif button == 'Too small':
            minimum = int(request.form.get('guess'))
            maximum = int(request.form.get('maximum'))
            guess = int((maximum - minimum) / 2 + minimum)
            info = f'Do you think about {guess}?'
            return render_template('guess.html', info=info, minimum=minimum, maximum=maximum, guess=guess)
        elif button == 'Too big':
            minimum = int(request.form.get('minimum'))
            maximum = int(request.form.get('guess'))
            guess = int((maximum - minimum) / 2 + minimum)
            info = f'Do you think about {guess}?'
            return render_template('guess.html', info=info, minimum=minimum, maximum=maximum, guess=guess)
        elif button == 'You win!':
            info = 'I knew it! Thank you, it was a pleasure to play with you.'
            return render_template('guess_win.html', info=info)
        elif button == 'Play again':
            return render_template('guess_start.html')


# if __name__ == "__main__":
app.run(debug=True, port=5001)
