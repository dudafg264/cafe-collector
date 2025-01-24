from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location on Google Maps (URL)', validators=[DataRequired()])
    open = StringField('Opening time (add AM or PM)', validators=[DataRequired()])
    close = StringField('Closing time (add AM or PM)', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', choices=[
        ('✘', 'bad'),
        ('☕', 'ok'),
        ('☕☕', 'good'),
        ('☕☕☕', 'really good'),
        ('☕☕☕', 'delicious')
        ], validators=[DataRequired()])
    wifi = SelectField('Wifi strength rating', choices=[
        ('✘', 'bad'),
        ('💪', 'ok'),
        ('💪💪', 'good'),
        ('💪💪💪', 'really good'),
        ('💪💪💪💪', 'amazing')
        ], validators=[DataRequired()])
    power = SelectField('Power strength rating', choices=[
        ('✘', 'bad'),
        ('🔌', 'ok'),
        ('🔌🔌', 'good'),
        ('🔌🔌🔌', 'really good'),
        ('🔌🔌🔌🔌', 'amazing')
        ], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        form_data = [form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee.data, form.wifi.data, form.power.data]
        with open("cafe-data.csv", mode="a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(form_data)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
