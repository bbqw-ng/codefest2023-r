from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class teamBranch(FlaskForm):
    subjects = SelectField(u'subject', choices=['Team-Based'])
    team = SelectField(u'Type', choices=['Sprint Retrospective', 'Stand-up Meeting', 'Sprint Planning', '1-on-1 Meeting'])
    times = SelectField(u'Time', choices=['<10min','<30min','<1hr','<2hr'])
    occurrence = SelectField(u'Occurrence', choices=['Daily','Weekly','Monthly','Annually'])
    submit = SubmitField('Submit')

class genBranch(FlaskForm):
    subjects = SelectField(u'subject', choices=['General Announcements'])
    gen = SelectField(u'Type', choices=['Business Updates','Product Performance'])
    times = SelectField(u'Time', choices=['<10min','<30min','<1hr','<2hr'])
    occurrence = SelectField(u'Occurrence', choices=['Daily','Weekly','Monthly','Annually'])
    submit = SubmitField('Submit')