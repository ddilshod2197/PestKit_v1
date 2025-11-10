from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html', titile='Home page')



@app.route('/error')
def error404():
    return render_template('404.html', titile='Error 404')



@app.route('/about')
def about():
    return render_template('about.html', titile='About')



@app.route('/blog')
def blog():
    return render_template('blog.html', titile='Blog')



@app.route('/contact')
def contact():
    return render_template('contact.html', titile='Contact')




@app.route('/price')
def price():
    return render_template('price.html', titile='Price')



@app.route('/project')
def project():
    return render_template('project.html', titile='Project')


@app.route('/service')
def service():
    return render_template('service.html', titile='Service')



@app.route('/team')
def team():
    return render_template('team.html', titile='Team')



@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html', titile='Testimonial')







if __name__ == '__main__':
    app.run(debug=True)