from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, ValidationError

def is_valid_input(min=-1, max=-1):
    msg = 'Must be a value between %d and %d, with optional / at front, or *' % (min, max)

    def _is_valid_input(form, field):
        data = field.data[1:] if field.data[0] == '/' and '*' not in field.data else field.data
        if not data.isdigit() and data != '*':
            raise ValidationError(msg)
        if data.isdigit():
            n = int(data)
            if n < min or n > max:
                raise ValidationError(msg)

    return _is_valid_input

class CronForm(Form):
    minute = StringField('Minutes (0-59 or *):', validators=[Required(), is_valid_input(min=0, max=59)])
    hour = StringField('Hours (0-23 or *):', validators=[Required(), is_valid_input(min=0, max=23)])
    day = StringField('Day (1-30 or *):', validators=[Required(), is_valid_input(min=1, max=30)])
    month = SelectField(u'Month', choices=[('*','All'), ('1','Jan'), ('2','Feb'), ('3','Mar'), ('4','Apr'), ('5','May'),
        ('6','Jun'), ('7','Jul'), ('8','Aug'), ('9','Sep'), ('10','Oct'), ('11','Nov'), ('12','Dec')], validators=[Required()])
    weekday = SelectField(u'Weekday', choices=[('*','All'), ('0','Sun'), ('1','Mon'), ('2','Tue'), ('3','Wed'), ('4','Thu'),
        ('5','Fri'), ('6','Sat')], validators=[Required()])
    submit = SubmitField('Submit')
