from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from forms import CronForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'poop'
Bootstrap(app)

def create_string(form):
    res = ''
    res += form.minute.data + ' '
    res += form.hour.data + ' '
    res += form.day.data + ' '
    res += form.month.data + ' '
    res += form.weekday.data
    return res

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CronForm()
    result = ''
    if form.validate_on_submit():
        # create the correct cron submission
        result = create_string(form)
    return render_template('index.html', form=form, result=result)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
