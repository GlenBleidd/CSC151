from app import app
import models
from flask import render_template, redirect, request
from forms import UserForm, DeleteForm, UpdateForm, SearchForm, AddCourse, DeleteCourse, UpdateCourse, SearchCourse


@app.route('/')
def index():
    users = models.Users.all()
    return render_template('index.html', data=users)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = UserForm(request.form)
    course = models.Course.all()
    if request.method == 'POST' and form.validate():
        user = models.Users(id_num=form.id_num.data, f_name=form.f_name.data, l_name=form.l_name.data, course=form.course.data, year=form.year.data, gender=form.gender.data)
        user.add()
        return redirect('/')
    else:
        return render_template('add.html', form=form, course=course)

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    form = DeleteForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(id_num = form.del_id.data)
        user.delete()
        return redirect('/')
    else:
        return render_template('delete.html', form = form)

@app.route('/update', methods = ['POST', 'GET'])
def update():
    form = UpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(id_num = form.new_id.data, f_name = form.new_fname.data, l_name = form.new_lname.data, course = form.new_course.data, year = form.new_year.data, gender = form.new_gender.data)
        user.update()
        return redirect('/')
    else:
        return render_template('update.html', form = form)

@app.route('/search', methods= ['POST', 'GET'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(id_num = form.search_id.data)
        data = user.search()
        return render_template('profile.html', data = data)
    else:
        return render_template('search.html', form = form)

#////////////////////////////////////////////////////////////////

@app.route('/course')
def courseindex():
    course = models.Course.all()
    return render_template('cindex.html', data=course)

@app.route('/course-add', methods=['POST', 'GET'])
def addcourse():
    form = AddCourse(request.form)
    if request.method == 'POST' and form.validate():
        course = models.Course(c_id=form.c_id.data, c_name=form.c_name.data, c_college=form.c_college.data)
        course.cadd()
        return redirect('/course')
    else:
        return render_template('cadd.html', form=form)

@app.route('/course-delete', methods=['POST', 'GET'])
def deletecourse():
    form = DeleteCourse(request.form)
    if request.method == 'POST' and form.validate():
        course = models.Course(c_id = form.del_cid.data)
        course.cdelete()
        return redirect('/course')
    else:
        return render_template('cdelete.html', form = form)

@app.route('/course-update', methods = ['POST', 'GET'])
def updatecourse():
    form = UpdateCourse(request.form)
    if request.method == 'POST' and form.validate():
        course = models.Course(c_id = form.new_cid.data, c_name = form.new_cname.data, c_college = form.new_ccollege.data)
        course.cupdate()
        return redirect('/course')
    else:
        return render_template('cupdate.html', form = form)

@app.route('/course-search', methods= ['POST', 'GET'])
def searchcourse():
    form = SearchCourse(request.form)
    if request.method == 'POST' and form.validate():
        course = models.Course(c_id = form.search_cid.data)
        course = course.csearch()
        return render_template('cprofile.html', data = course)
    else:
        return render_template('csearch.html', form = form)
