'''
Author - Sean Beck

The main app for the flask application Cron Configure
'''
import os

from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from forms import CronForm

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'poop'
Bootstrap(APP)


def prepend_star(target):
    '''
    Prepends a * if the specified string starts with /
    '''
    if '/' in target:
        return '*'+target
    else:
        return target


def create_string(form):
    '''
    Creates the configuration string
    '''
    res = ''
    res += prepend_star(form.minute.data) + ' '
    res += prepend_star(form.hour.data) + ' '
    res += prepend_star(form.day.data) + ' '
    res += form.month.data + ' '
    res += form.weekday.data + ' '
    res += 'your command goes here'
    return res


@APP.route('/', methods=['GET', 'POST'])
def index():
    '''
    Handles GET and POST requests to the index
    '''
    form = CronForm()
    result = ''
    if form.validate_on_submit():
        result = create_string(form)
    return render_template('index.html', form=form, result=result)


if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 5000))
    APP.run(debug=True, host='0.0.0.0', port=PORT)
