from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class UserForm(Form):
    id_num = StringField('Id No',  validators = [InputRequired("Id Number is Required")])
    f_name = StringField('First Name',  validators = [InputRequired("Please Input First Name")])
    l_name = StringField('Last Name',  validators = [InputRequired("Please Input Last Name")])
    course = StringField('Course',  validators = [InputRequired("Please Input Student Course")])
    year = StringField('Year',  validators = [InputRequired("Please Input Year Level")])
    gender = StringField('Gender',  validators = [InputRequired("Please Input Gender")])
    submit = SubmitField("Submit")

class DeleteForm(Form):
    del_id = StringField('Id Number', validators =[InputRequired("Make sure you enter an Id Number you want to delete!")])
    submit = SubmitField("Submit")

class UpdateForm(Form):
    new_id = StringField('Id No', validators = [InputRequired("Id Number is Required")])
    new_fname = StringField('New First Name', validators = [InputRequired("Please Input New First Name")])
    new_lname = StringField('New Last Name', validators = [InputRequired("Please Input New Last Name")])
    new_course = StringField('New Course', validators = [InputRequired("Please Input New Course")])
    new_year = StringField('New Year Level', validators = [InputRequired("Please Input New Year Level")])
    new_gender = StringField('Update Gender', validators = [InputRequired("Please Update Gender")])
    submit = SubmitField("Submit")

class SearchForm(Form):
    search_id = StringField('Student ID Number',  validators = [InputRequired("Enter Student ID")])
    submit = SubmitField("Submit")