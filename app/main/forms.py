from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Write a short story about you',validators = [Required])
  submit = SubmitField('save')

class PitchForm(FlaskForm):
  title = StringField('Title',validators = [Required])
  category = StringField('Category', choices = [('Events','Events'),('Job','Job'),('Advertisement','Advertisement')], validators = [Required])
  post = TextAreaField('Your Pitch', validators = [Required])
  submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
  comment = TextAreaField('Leave a comment', validators = [Required])
  submit = SubmitField('Comment')