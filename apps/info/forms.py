from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class FishForm(FlaskForm):
  fishname = StringField('생선명')
  season = IntegerField('계절',validators=[DataRequired(), NumberRange(min=1, max=5, message="0부터 4 사이의 숫자를 입력하세요.")])
  etc = StringField('비고')

  submit = SubmitField('신규등록')
  