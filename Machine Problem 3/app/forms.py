from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms.validators import InputRequired

class UserForm(Form):
    id_num = StringField('Id No',  validators = [InputRequired("Id Number is Required")])
    f_name = StringField('First Name',  validators = [InputRequired("Please Input First Name")])
    l_name = StringField('Last Name',  validators = [InputRequired("Please Input Last Name")])
    course = StringField('Choose Course', validators = [InputRequired("Please Select Student Course")])
    year = IntegerField('Year',  validators = [InputRequired("Please Input Year Level")])
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
    new_year = IntegerField('New Year Level', validators = [InputRequired("Please Input New Year Level")])
    new_gender = StringField('Update Gender', validators = [InputRequired("Please Update Gender")])
    submit = SubmitField("Submit")

class SearchForm(Form):
    search_id = StringField('Student ID Number',  validators = [InputRequired("Enter Student ID")])
    submit = SubmitField("Submit")

#////////////////////////////////////////

class AddCourse(Form):
    c_id = StringField('Course ID',  validators = [InputRequired("Course Id is Required")])
    c_name = StringField('Course Title',  validators = [InputRequired("Please Input Course Title")])
    c_college = StringField('College',  validators = [InputRequired("Please Input College")])
    submit = SubmitField("Submit")

class DeleteCourse(Form):
    del_cid = StringField('Course ID', validators =[InputRequired("Not a Valid Course ID")])
    submit = SubmitField("Submit")

class UpdateCourse(Form):
    new_cid = StringField('New Course Id', validators = [InputRequired("Course Id is Required")])
    new_cname = StringField('New Course Title', validators = [InputRequired("Please Input New Course Title")])
    new_ccollege = StringField('New College', validators = [InputRequired("Please Input New College")])
    submit = SubmitField("Submit")

class SearchCourse(Form):
    search_cid = StringField('Course ID',  validators = [InputRequired("Enter Course ID")])
    submit = SubmitField("Submit")