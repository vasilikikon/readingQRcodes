from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  data = request.form
  return render_template("login.html")


@auth.route('/logout')
def logout():
 return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
 if request.method == 'POST':
  email = request.POST.get('email')
  firstName = request.POST.get('firstName')
  password1 = request.POST.get('password1')
  password2 = request.POST.get('password2')

  if len(email)<4:
   flash('Email must be greater than 3 characters', category='error')
  elif len(firstName)<2:
   flash('First must be greater than 1 characters', category='error')
  elif password1 != password2:
   flash('Passwords don\'t match', category='error')
  elif len(password1)<7:
   flash('Password must be greater than 6 characters', category='error')
  else:
   flash('Account ctreated!', category='success')
 return render_template("sign_up.html")





