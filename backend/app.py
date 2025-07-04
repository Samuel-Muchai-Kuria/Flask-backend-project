from flask import Flask,render_template, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin ,LoginManager,login_required, login_user, logout_user, current_user
from  wtforms import  StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, length ,ValidationError
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt
import requests

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# function to get meme from api
def get_meme():
    url = f"https://meme-api.com/gimme/wholesomememes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meme_large= data.get('preview', '')[0]
        subreddit = data.get('subreddit', '')
        title = data.get('title', '')
        return meme_large, subreddit, title
    else:
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired(), length(min=4, max=20)],render_kw={"placeholder": "Enter your username"})
    password = PasswordField('Password', [DataRequired(), length(min=6, max=80)],render_kw={"placeholder": "Enter your password"})
    
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError('Username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(), length(min=4, max=20)],render_kw={"placeholder": "Enter your username"})
    password = PasswordField('Password', [DataRequired(), length(min=6, max=80)],render_kw={"placeholder": "Enter your password"})
    
    submit = SubmitField('Login')
    


@app.route('/')
def home():

    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    meme_large, subreddit, title = get_meme()
    return render_template('dashboard.html', meme_large=meme_large, subreddit=subreddit, title=title, current_user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print('User registered successfully!')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
