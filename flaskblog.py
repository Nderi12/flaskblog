from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5a9086602a4bd0db6746d22e102b12d4'

posts = [

{
	'author': 'Jane Doe',
	'title': 'Script writer',
	'content': 'First Script content',
	'date_posted': 'April 4, 2019'
},

{
	'author': 'John Doe',
	'title': 'Content writer',
	'content': 'First post content',
	'date_posted': 'April 4, 2019'
}

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
 	app.run(debug=True)