from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class RPSForm(FlaskForm):
    moves = SelectField("Post Author", choices=[('rock','Rock 🪨'), ('paper','Paper 📄'), ('scissors','Scissors ✂️')])
    submit = SubmitField("Play Move!")