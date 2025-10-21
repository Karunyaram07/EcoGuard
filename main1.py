# import json
# from flask import Flask,render_template,request,session,redirect,url_for,flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash,check_password_hash
# from flask_login import login_user,logout_user,login_manager,LoginManager
# from flask_login import login_required,current_user

# from flask_mail import Mail

# #db connection
# local_server=True
# app=Flask(__name__)
# app.secret_key='sjbit'


# login_manager=LoginManager(app)
# login_manager.login_view='login'
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
    
    
    
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Karunyaram%4007@localhost:3306/msw'

# db=SQLAlchemy(app)



    
# #db tables
# class Test(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100))
#     email=db.Column(db.String(100))


# class User(UserMixin,db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     username=db.Column(db.String(50))
#     email=db.Column(db.String(50),unique=True)
#    # address=db.Column(db.String(50))
#     password=db.Column(db.String(1000))
    
# class Complaints(db.Model):
#     cid=db.Column(db.Integer,primary_key=True)
#     email=db.Column(db.String(50))
#     message=db.Column(db.String(50))
#     date=db.Column(db.String(50),nullable=False)
#     image=db.Column(db.String(50))
#     status = db.Column(db.String(20), default='Submitted')
    
    
# # to pass endpoints
# @app.route('/')
# def index():
#     return render_template('index.html')
# @app.route('/test')
# def test():
#     return render_template('test.html')

# @app.route('/home')
# @login_required
# def home():
#         return render_template('home.html')

# @app.route('/signup', methods=['POST','GET'])
# def signup():
#     if request.method == "POST":
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')

#         # Validate inputs
#         if not username or not email or not password:
#             flash("All fields are required!", "danger")
#             return render_template('signup.html')

#         # Check if user already exists
#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash("Email Already Exists", "warning")
#             return render_template('signup.html')

#         # Encrypt password
#         encpassword = generate_password_hash(password)

#         # Use ORM to add user safely
#         new_user = User(username=username, email=email, password=encpassword)
#         db.session.add(new_user)
#         db.session.commit()

#         flash("Signup Successful! Please Login", "success")
#         return render_template('login.html')

#     return render_template('signup.html')



# @app.route('/login',methods=['POST','GET'])
# def login():
#     if request.method == "POST":
#         email=request.form.get('email')
#         password=request.form.get('password')
#         user=User.query.filter_by(email=email).first()

#         if user and check_password_hash(user.password,password):
#             login_user(user)
#             flash("Login Success","primary")
#             return redirect(url_for('index'))
#         else:
#             flash("invalid credentials","danger")
#             return render_template('login.html')    


#     return render_template('login.html')

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash("Logout Succesful","warning")
#     return redirect(url_for('login'))   



# @app.route('/prcomplaint')
# @login_required
# def prcomplaint():
#     c_email = current_user.email
#     # Use SQLAlchemy ORM query
#     comp = Complaints.query.filter_by(email=c_email).all()
#     return render_template('prcomplaint.html', comp=comp)


# @app.route('/Complaint',methods=['POST','GET'])
# @login_required
# def Complaint():
#     if request.method =="POST":
#         email=request.form.get('email')
#         message=request.form.get('message')
#         date=request.form.get('date')
#         image=request.form.get('image')
#         new_complaint = new_complaint = Complaints(
#     email=email,
#     message=message,
#     date=date,
#     image=image,
#     status="Submitted"
# )

#         db.session.add(new_complaint)
#         db.session.commit()




#     flash("Complaint Submited Thank you!","primary")

#     return render_template('Complaint.html')




# @app.route('/areadetails')
# @login_required
# def area():
#     if not User.is_authenticated:
#         return render_template('login.html')
#     return render_template('areadetails.html')

# @app.route("/edit/<string:cid>",methods=['POST','GET'])
# @login_required
# def edit(cid):
#     posts=Complaints.query.filter_by(cid=cid).first()
#     if request.method=="POST":
#         email=request.form.get('email')
#         message=request.form.get('message')
#         date=request.form.get('date')
#         image=request.form.get('image')
#         query= db.engine.execute(f"UPDATE `complaints` SET `email` = '{email}', `meassage` = '{message}', `date` = '{date}', `image` = '{image}',   WHERE `complaints`.`cid` = {cid}")
#         flash("Slot is Updates","success")
#         return redirect('/complaint')
    
#     return render_template('edit.html',query=query)

# app.run(debug=True)



# import json
# from flask import Flask, render_template, request, session, redirect, url_for, flash, abort
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime

# # app setup
# app = Flask(__name__)
# app.secret_key = 'sjbit'

# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

# # DB config - update as needed
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Karunyaram%4007@localhost:3306/msw'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Models
# class Test(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50))
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(1000))
#     is_admin = db.Column(db.Boolean, default=False)  # new: admin flag

# class Complaints(db.Model):
#     cid = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100))
#     message = db.Column(db.String(1000))  # increased length
#     date = db.Column(db.String(50), nullable=False)
#     image = db.Column(db.String(200))
#     status = db.Column(db.String(20), default='Submitted')

# # User loader
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# # Routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/test')
# def test():
#     return render_template('test.html')

# @app.route('/home')
# @login_required
# def home():
#     return render_template('home.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == "POST":
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')

#         if not username or not email or not password:
#             flash("All fields are required!", "danger")
#             return render_template('signup.html')

#         # Check existing user
#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash("Email already exists", "warning")
#             return render_template('signup.html')

#         encpassword = generate_password_hash(password)
#         new_user = User(username=username, email=email, password=encpassword)
#         db.session.add(new_user)
#         db.session.commit()

#         flash("Signup successful! Please login.", "success")
#         return redirect(url_for('login'))

#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = User.query.filter_by(email=email).first()
#         if user and check_password_hash(user.password, password):
#             login_user(user)
#             flash("Login successful", "primary")
#             # redirect to home after login
#             return redirect(url_for('home'))
#         else:
#             flash("Invalid credentials", "danger")
#             return render_template('login.html')
#     return render_template('login.html')

# @app.route('/alogin', methods=['GET', 'POST'])
# def alogin():
#     """
#     Optional: separate admin login page if you want. This route uses the same form
#     as regular login, but enforces is_admin True. You can point admin login links to /alogin.
#     """
#     if request.method == "POST":
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = User.query.filter_by(email=email, is_admin=True).first()
#         if user and check_password_hash(user.password, password):
#             login_user(user)
#             flash("Admin login successful", "primary")
#             return redirect(url_for('prcomplaint_admin'))
#         else:
#             flash("Invalid admin credentials", "danger")
#             return render_template('login.html')
#     return render_template('login.html')

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash("Logout successful", "warning")
#     return redirect(url_for('login'))

# @app.route('/prcomplaint')
# @login_required
# def prcomplaint():
#     """
#     Preview complaints for the current user (regular view).
#     Admins may have a separate listing route to view all complaints.
#     """
#     if current_user.is_admin:
#         # admin sees all complaints
#         comp = Complaints.query.order_by(Complaints.cid.desc()).all()
#     else:
#         comp = Complaints.query.filter_by(email=current_user.email).order_by(Complaints.cid.desc()).all()
#     return render_template('prcomplaint.html', comp=comp)

# @app.route('/prcomplaint_admin')
# @login_required
# def prcomplaint_admin():
#     if not current_user.is_admin:
#         abort(403)
#     comp = Complaints.query.order_by(Complaints.cid.desc()).all()
#     return render_template('prcomplaint.html', comp=comp)

# @app.route('/Complaint', methods=['GET', 'POST'])
# @login_required
# def Complaint():
#     if request.method == "POST":
#         email = request.form.get('email')
#         message = request.form.get('message')
#         date = request.form.get('date')
#         image = request.form.get('image')  # currently basic text input; change to file handling later

#         # Basic validation
#         if not email or not message or not date:
#             flash("Please fill required fields", "danger")
#             return render_template('Complaint.html')

#         new_complaint = Complaints(
#             email=email,
#             message=message,
#             date=date,
#             image=image,
#             status="Submitted"
#         )

#         db.session.add(new_complaint)
#         db.session.commit()
#         flash("Complaint submitted — thank you!", "primary")
#         return redirect(url_for('prcomplaint'))

#     return render_template('Complaint.html')

# @app.route('/areadetails')
# @login_required
# def area():
#     if not current_user.is_authenticated:
#         return redirect(url_for('login'))
#     return render_template('areadetails.html')

# @app.route("/edit/<int:cid>", methods=['GET', 'POST'])
# @login_required
# def edit(cid):
#     complaint = Complaints.query.filter_by(cid=cid).first_or_404()

#     # Permission: admin can edit status; normal user can only edit their own complaint fields
#     if not current_user.is_admin and complaint.email != current_user.email:
#         # unauthorized: non-admin trying to edit someone else's complaint
#         abort(403)

#     if request.method == "POST":
#         # Fields editable by all owners+admin
#         email = request.form.get('email')
#         message = request.form.get('message')
#         date = request.form.get('date')
#         image = request.form.get('image')

#         if email:
#             complaint.email = email
#         if message:
#             complaint.message = message
#         if date:
#             complaint.date = date
#         if image is not None:
#             complaint.image = image

#         # Only admin can change status
#         if current_user.is_admin:
#             status = request.form.get('status')
#             if status:
#                 complaint.status = status

#         db.session.commit()
#         flash("Complaint updated successfully", "success")

#         # redirect appropriately
#         if current_user.is_admin:
#             return redirect(url_for('prcomplaint_admin'))
#         else:
#             return redirect(url_for('prcomplaint'))

#     # GET -> render edit template, pass complaint as posts for backward compatibility in template
#     return render_template('edit.html', posts=complaint)

# @app.route("/delete/<int:cid>", methods=['POST', 'GET'])
# @login_required
# def delete(cid):
#     # Only allow deleting by admin or the complaint owner
#     complaint = Complaints.query.filter_by(cid=cid).first_or_404()
#     if not current_user.is_admin and complaint.email != current_user.email:
#         abort(403)
#     db.session.delete(complaint)
#     db.session.commit()
#     flash("Complaint deleted", "warning")
#     return redirect(url_for('prcomplaint'))

# if __name__ == "__main__":
#     app.run(debug=True)



import json
from flask import Flask, render_template, request, session, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
from werkzeug.utils import secure_filename


# app setup
app = Flask(__name__)
app.secret_key = 'sjbit'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# DB config - update as needed
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Karunyaram%4007@localhost:3306/msw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --------------------- MODELS ---------------------
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(1000))
    is_admin = db.Column(db.Boolean, default=False)  # admin flag

class Complaints(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    message = db.Column(db.String(1000))
    date = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200))
    status = db.Column(db.String(20), default='Submitted')

# --------------------- USER LOADER ---------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --------------------- ADMIN CREATION ---------------------
def create_admin():
    """Automatically creates predefined admin if not already in database."""
    with app.app_context():
        admin_email = 'admin@ecoguard.com'
        admin_user = User.query.filter_by(email=admin_email).first()
        if not admin_user:
            encpassword = generate_password_hash('admin123')
            new_admin = User(username='admin', email=admin_email, password=encpassword, is_admin=True)
            db.session.add(new_admin)
            db.session.commit()
            print("✅ Admin created: email=admin@ecoguard.com, password=admin123")

# call this manually at startup (safe for Flask 3.x)
create_admin()


# --------------------- ROUTES ---------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/areadetails')
@login_required
def area():
    return render_template('areadetails.html')


@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username or not email or not password:
            flash("All fields are required!", "danger")
            return render_template('signup.html')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", "warning")
            return render_template('signup.html')

        encpassword = generate_password_hash(password)
        new_user = User(username=username, email=email, password=encpassword)
        db.session.add(new_user)
        db.session.commit()
        flash("Signup successful! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful", "primary")
            if user.is_admin:
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout successful", "warning")
    return redirect(url_for('login'))

# --------------------- USER COMPLAINT ROUTES ---------------------



UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/Complaint', methods=['GET', 'POST'])
@login_required
def Complaint():
    if request.method == "POST":
        email = request.form.get('email')
        message = request.form.get('message')
        date = request.form.get('date')
        file = request.files.get('image')

        # validate all fields
        if not email or not message or not date or not file:
            flash("All fields including image are required", "danger")
            return render_template('Complaint.html')

        # validate file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        else:
            flash("Invalid file type. Allowed types: jpg, jpeg, png, pdf", "danger")
            return render_template('Complaint.html')

        # save complaint
        new_complaint = Complaints(email=email, message=message, date=date, image=filename)
        db.session.add(new_complaint)
        db.session.commit()
        flash("Complaint submitted successfully!", "primary")
        return redirect(url_for('prcomplaint'))

    return render_template('Complaint.html')


@app.route('/prcomplaint')
@login_required
def prcomplaint():
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    comp = Complaints.query.filter_by(email=current_user.email).order_by(Complaints.cid.desc()).all()
    return render_template('prcomplaint.html', comp=comp)

# --------------------- ADMIN DASHBOARD ---------------------
@app.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    comp = Complaints.query.order_by(Complaints.cid.desc()).all()
    return render_template('admin_dashboard.html', comp=comp)

@app.route('/update_status/<int:cid>', methods=['POST'])
@login_required
def update_status(cid):
    if not current_user.is_admin:
        abort(403)
    complaint = Complaints.query.get_or_404(cid)
    new_status = request.form.get('status')
    if new_status:
        complaint.status = new_status
        db.session.commit()
        flash(f"Complaint #{cid} status updated to '{new_status}'", "success")
    return redirect(url_for('admin_dashboard'))

# --------------------- DELETE / EDIT ---------------------
@app.route('/edit/<int:cid>', methods=['GET', 'POST'])
@login_required
def edit(cid):
    complaint = Complaints.query.get_or_404(cid)

    # Only allow admin to edit
    if not current_user.is_admin:
        abort(403)  # normal users cannot edit

    if request.method == "POST":
        # Admin can edit message, date, image, and status
        message = request.form.get('message')
        date = request.form.get('date')
        image = request.form.get('image')
        status = request.form.get('status')

        if message: complaint.message = message
        if date: complaint.date = date
        if image: complaint.image = image
        if status: complaint.status = status

        db.session.commit()
        flash("Complaint updated successfully", "success")
        return redirect(url_for('admin_dashboard'))

    return render_template('edit.html', posts=complaint)


@app.route('/delete/<int:cid>', methods=['GET', 'POST'])
@login_required
def delete(cid):
    complaint = Complaints.query.get_or_404(cid)
    if not current_user.is_admin and complaint.email != current_user.email:
        abort(403)
    db.session.delete(complaint)
    db.session.commit()
    flash("Complaint deleted", "warning")
    return redirect(url_for('admin_dashboard' if current_user.is_admin else 'prcomplaint'))

create_admin()


if __name__ == "__main__":
    app.run(debug=True)
