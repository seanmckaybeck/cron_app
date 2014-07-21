from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'poop'
Bootstrap(app)

def create_string(form):
    res = ''
    res += form.minute + ' '
    res += form.hour + ' '
    res += form.day + ' '
    res += form.month + ' '
    res += form.weekday
    return res

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CronForm()
    result = ''
    if form.validate_on_submit():
        # create the correct cron submission
        result = create_string(form)
    return render_template('index.html', form=form, result=result)

# @app.route('/generate')
# def generate_config_page():
#     return render_template('config.html')

# @app.route('/api/generate_config')
# def generate_config():
#     # do some stuff to make it
#     return render_template('config.html')

def is_valid_input(min=-1, max=-1):
    msg = 'Must be a value between %d and %d or *' % (min, max)

    def _is_valid_input(form, field):
        if not field.data.isdigit() and field.data != '*':
            raise ValidationError(msg)
        if field.data.isdigit():
            n = int(field.data)
            if n < min or n > max:
                raise ValidationError(msg)

    return _is_valid_input

class CronForm(Form):
    minute = StringField('Minutes (0-59):', validators=[Required(), is_valid_input(min=0, max=59)])
    hour = StringField('Hours (0-23):', validators=[Required(), is_valid_input(min=0, max=23)])
    day = StringField('Day (1-30):', validators=[Required(), is_valid_input(min=1, max=30)])
    month = StringField('Month (1-12):', validators=[Required(), is_valid_input(min=1, max=12)])
    weekday = StringField('Weekday (0-6):', validators=[Required(), is_valid_input(min=0, max=6)])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    app.run(debug=True)
