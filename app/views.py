"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from .models import UserProfile
from .forms import UserProfileForm


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/home')
def home1():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = UserProfileForm()

    if request.method == 'POST':

        fname = form.firstName.data
        lname =form.lastName.data
        email = form.email.data
        gender = form.gender.data
        location = form.location.data
        biography = form.biography.data
        photo = form.photo.data
        
        if photo:
            uploadfolder = app.config['UPLOAD_FOLDER']
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(uploadfolder, filename))
        
        if gender=='0':
            gender = 'Male'
        else:
            gender = 'Female'
        user = UserProfile(first_name=fname,last_name=lname,email=email,location=location,gender=gender,bio=biography,photo=photo.filename)
        db.session.add(user)
        db.session.commit()

        flash('You have successfully filled out the form', 'success')
        return redirect(url_for('profiles'))
    return render_template('profile.html', form=form)

@app.route('/profiles', methods=['GET','POST'])
def profiles():
    profile_list = UserProfile.query.filter_by().all()
    return render_template('profiles.html', profile_list=profile_list)
    

@app.route('/profile/<userid>', methods=['GET','POST'])
def details(userid):
    client = UserProfile.query.filter_by(id=userid).first()
    if client:
        return render_template('profileDetails.html',client=client)
    return render_template('profile.html')


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")