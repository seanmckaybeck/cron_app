from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, ValidationError

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
    month = SelectField(u'Month', choices=[('*','All'), ('1','Jan'), ('2','Feb'), ('3','Mar'), ('4','Apr'), ('5','May'),
        ('6','Jun'), ('7','Jul'), ('8','Aug'), ('9','Sep'), ('10','Oct'), ('11','Nov'), ('12','Dec')], validators=[Required()])
    weekday = SelectField(u'Weekday', choices=[('*','All'), ('0','Sun'), ('1','Mon'), ('2','Tue'), ('3','Wed'), ('4','Thu'),
        ('5','Fri'), ('6','Sat')], validators=[Required()])
    # month = StringField('Month (1-12):', validators=[Required(), is_valid_input(min=1, max=12)])
    # weekday = StringField('Weekday (0-6):', validators=[Required(), is_valid_input(min=0, max=6)])
    submit = SubmitField('Submit')
