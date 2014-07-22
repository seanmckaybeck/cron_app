from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from forms import CronForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'poop'
Bootstrap(app)

def prepend_star(target):
    if '/' in target:
        return '*'+target
    else:
        return target

def create_string(form):
    res = ''
    res += prepend_star(form.minute.data) + ' '
    res += prepend_star(form.hour.data) + ' '
    res += prepend_star(form.day.data) + ' '
    res += form.month.data + ' '
    res += form.weekday.data + ' '
    res += 'your command goes here'
    return res

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CronForm()
    result = ''
    if form.validate_on_submit():
        result = create_string(form)
    return render_template('index.html', form=form, result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
