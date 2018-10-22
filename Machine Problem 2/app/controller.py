from app import app
import models
from flask import render_template, redirect, request
from forms import UserForm, DeleteForm, UpdateForm, SearchForm


@app.route('/')
def index():
    users = models.Users.all()
    return render_template('index.html', data=users)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(id_num=form.id_num.data, f_name=form.f_name.data, l_name=form.l_name.data, course=form.course.data, year=form.year.data, gender=form.gender.data)
        user.add()
        return redirect('/')
    else:
        return render_template('add.html', form=form)

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
