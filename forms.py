from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, ValidationError


def is_valid_input(minimum=-1, maximum=-1):
    '''
    Returns a function which checks input for whether it is within
    the specified bounds
    '''
    msg = 'Must be a value between %d and %d,' \
        'with optional / at front, or *' % (minimum, maximum)

    def _is_valid_input(form, field):
        '''
        Raises error on validation failure
        '''
        data = field.data[1:] if field.data[0] == '/' and \
            '*' not in field.data else field.data
        if not data.isdigit() and data != '*':
            raise ValidationError(msg)
        if data.isdigit():
            num = int(data)
            if num < minimum or num > maximum:
                raise ValidationError(msg)

    return _is_valid_input


class CronForm(Form):
    '''
    The submission form. It is generated in the template
    '''
    def __init__(self):
        self.minute = StringField('Minutes (0-59 or *):',
                                  validators=[Required(),
                                              is_valid_input(minimum=0,
                                              maximum=59)])
        self.hour = StringField('Hours (0-23 or *):', validators=[Required(),
                                is_valid_input(minimum=0, maximum=23)])
        self.day = StringField('Day (1-30 or *):', validators=[Required(),
                               is_valid_input(minimum=1, maximum=30)])
        self.month = SelectField(u'Month', choices=[('*', 'All'), ('1', 'Jan'),
                                 ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'),
                                 ('5', 'May'), ('6', 'Jun'), ('7', 'Jul'),
                                 ('8', 'Aug'), ('9', 'Sep'), ('10', 'Oct'),
                                 ('11', 'Nov'), ('12', 'Dec')],
                                 validators=[Required()])
        self.weekday = SelectField(u'Weekday', choices=[('*', 'All'),
                                   ('0', 'Sun'), ('1', 'Mon'), ('2', 'Tue'),
                                   ('3', 'Wed'), ('4', 'Thu'), ('5', 'Fri'),
                                   ('6', 'Sat')], validators=[Required()])
        self.submit = SubmitField('Submit')
