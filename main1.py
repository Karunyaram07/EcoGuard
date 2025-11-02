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
# from datetime import datetime, timedelta

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


# main.py  (drop-in replacement for main1.py)
import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from flask_mail import Mail, Message
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy.dialects.mysql import JSON, ENUM
from sqlalchemy import func, text
import os

from sqlalchemy.dialects.mysql import JSON
load_dotenv()  # Load all variables from .env



# Optional AI/ML imports (wrapped in try/except)
try:
    from transformers import pipeline
    HF_AVAILABLE = True
except Exception as e:
    print("Hugging Face transformers not available:", e)
    HF_AVAILABLE = False

# Image processing and model imports
try:
    from PIL import Image
    import imagehash
    import torch
    from torchvision import models
    RESNET_AVAILABLE = True
except Exception as e:
    print("ResNet/PIL not available:", e)
    RESNET_AVAILABLE = False

# --- App setup ---
app = Flask(__name__)
app.secret_key = 'sjbit'

# --- Mail config (update with your SMTP details) ---
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", os.getenv("MAIL_USERNAME")),
    MAIL_SUPPRESS_SEND = False
)
mail = Mail(app)

# --- Login & DB ---
login_manager = LoginManager(app)
login_manager.login_view = 'login'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Karunyaram%4007@localhost:3306/msw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Upload config ---
UPLOAD_FOLDER = 'static/uploads'
NGO_PROOF_FOLDER = 'static/ngo_proofs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['NGO_PROOF_FOLDER'] = NGO_PROOF_FOLDER
for _folder in (UPLOAD_FOLDER, NGO_PROOF_FOLDER):
    if not os.path.exists(_folder):
        os.makedirs(_folder, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_proof(file):
    if not file or file.filename == '':
        return None
    fname = secure_filename(file.filename)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    fname = f"{timestamp}_{fname}"
    path = os.path.join(app.config['NGO_PROOF_FOLDER'], fname)
    file.save(path)
    return fname

# --- Models ---


from datetime import datetime
from sqlalchemy.dialects.mysql import JSON, ENUM

class UserStats(db.Model):
    __tablename__ = 'user_stats'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)
    level = db.Column(db.Integer, nullable=False, default=1)
    streak_count = db.Column(db.Integer, nullable=False, default=0)
    last_action_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class NGOStats(db.Model):
    __tablename__ = 'ngo_stats'
    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'), unique=True, nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)
    level = db.Column(db.Integer, nullable=False, default=1)
    streak_count = db.Column(db.Integer, nullable=False, default=0)
    last_action_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class GamificationEvent(db.Model):
    __tablename__ = 'gamification_events'
    id = db.Column(db.Integer, primary_key=True)
    actor_type = db.Column(ENUM('user', 'ngo'), nullable=False, index=True)
    actor_id = db.Column(db.Integer, nullable=False, index=True)  # polymorphic; no FK to keep simple
    action = db.Column(db.String(64), nullable=False, index=True)
    points = db.Column(db.Integer, nullable=False, default=0)
    meta = db.Column(JSON, nullable=True)  # MySQL 5.7+; else use db.Text
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True)

class Badge(db.Model):
    __tablename__ = 'badges'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)

class UserBadge(db.Model):
    __tablename__ = 'user_badges'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    badge_id = db.Column(db.Integer, db.ForeignKey('badges.id'), nullable=False, index=True)
    awarded_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('user_id', 'badge_id', name='uq_user_badge'),)

class NGOBadge(db.Model):
    __tablename__ = 'ngo_badges'
    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'), nullable=False, index=True)
    badge_id = db.Column(db.Integer, db.ForeignKey('badges.id'), nullable=False, index=True)
    awarded_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('ngo_id', 'badge_id', name='uq_ngo_badge'),)

# Optional: add JSON field to Complaints to track idempotent awards
# If your Complaints model is named Complaints and has table 'complaints'
# and you are on MySQL 5.7+, otherwise use db.Text instead of JSON.
def _ensure_points_awarded_column():
    if not hasattr(Complaints, 'points_awarded'):
        try:
            db.engine.execute("ALTER TABLE complaints ADD COLUMN points_awarded JSON NULL")
        except Exception:
            # fallback if JSON not supported: TEXT
            try:
                db.engine.execute("ALTER TABLE complaints ADD COLUMN points_awarded TEXT NULL")
            except Exception:
                pass

# ---------------- Gamification helpers ----------------

def _calc_level(points: int) -> int:
    try:
        return max(1, points // 100 + 1)
    except Exception:
        return 1

def _ensure_user_stats(user_id: int) -> 'UserStats':
    us = UserStats.query.filter_by(user_id=user_id).first()
    if not us:
        us = UserStats(user_id=user_id, points=0, level=1, streak_count=0)
        db.session.add(us)
        db.session.flush()
    return us

def _ensure_ngo_stats(ngo_id: int) -> 'NGOStats':
    ns = NGOStats.query.filter_by(ngo_id=ngo_id).first()
    if not ns:
        ns = NGOStats(ngo_id=ngo_id, points=0, level=1, streak_count=0)
        db.session.add(ns)
        db.session.flush()
    return ns

def award_points_unique(actor_type: str, actor_id: int, action_key: str, points: int, meta: dict | None = None):
    existing = GamificationEvent.query.filter_by(actor_type=actor_type, actor_id=actor_id, action=action_key).first()
    if existing:
        return False
    ev = GamificationEvent(actor_type=actor_type, actor_id=actor_id, action=action_key, points=points, meta=meta or {})
    db.session.add(ev)
    if actor_type == 'user':
        stats = _ensure_user_stats(actor_id)
    else:
        stats = _ensure_ngo_stats(actor_id)
    stats.points = (stats.points or 0) + int(points)
    stats.level = _calc_level(stats.points)
    stats.last_action_at = datetime.utcnow()
    try:
        maybe_award_badges(actor_type, actor_id)
    except Exception as _e:
        pass
    db.session.commit()
    return True

def _normalize_text_fp(title: str | None, message: str | None, pincode: str | None) -> str:
    import hashlib, re
    t = (title or '') + ' ' + (message or '') + ' ' + (pincode or '')
    t = t.lower()
    t = re.sub(r"\s+", " ", t).strip()
    return hashlib.sha1(t.encode('utf-8')).hexdigest()

def _md5_file(path: str) -> str | None:
    import hashlib, os
    if not path or not os.path.exists(path):
        return None
    h = hashlib.md5()
    try:
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def _phash_file(path: str) -> str | None:
    if not RESNET_AVAILABLE or not path:
        # PIL/imagehash imported in same try; reuse flag
        pass
    try:
        img = Image.open(path).convert('RGB')
        ph = imagehash.phash(img)
        return ph.__str__()  # hex string
    except Exception:
        return None

from rapidfuzz.distance import Hamming as _Ham  # fast hamming for hex strings of equal length

def _hamming_hex(a: str, b: str) -> int:
    try:
        if not a or not b or len(a) != len(b):
            return 999
        return _Ham.distance(a, b)
    except Exception:
        return 999

def _check_duplicate_complaint(email: str, title: str | None, message: str | None, pincode: str | None,
                               image_filename: str | None,
                               pre_md5: str | None = None,
                               pre_phash: str | None = None,
                               pre_text_fp: str | None = None):
    from datetime import timedelta
    import os
    fp_new = pre_text_fp or _normalize_text_fp(title, message, pincode)
    img_md5_new = pre_md5
    img_phash_new = pre_phash
    recent = (Complaints.query
              .filter_by(email=email)
              .order_by(Complaints.cid.desc())
              .limit(200)
              .all())
    now = datetime.utcnow()
    for c in recent:
        # time window
        try:
            if c.date and (now - c.date).days > 60:
                continue
        except Exception:
            pass
        # exact text duplicate
        try:
            if getattr(c, 'text_fingerprint', None) and fp_new and c.text_fingerprint == fp_new:
                return c
        except Exception:
            pass
        # exact image hash
        try:
            if getattr(c, 'image_md5', None) and img_md5_new and c.image_md5 == img_md5_new:
                return c
        except Exception:
            pass
        # perceptual near-duplicate (phash)
        try:
            if getattr(c, 'image_phash', None) and img_phash_new:
                if _hamming_hex(c.image_phash, img_phash_new) <= 5 and (not pincode or c.pincode == pincode):
                    return c
        except Exception:
            pass
        # fallback recompute when columns missing
        if (img_md5_new is None or img_phash_new is None) and getattr(c, 'image', None):
            old_path = os.path.join(UPLOAD_FOLDER, c.image)
            if img_md5_new is None:
                img_md5_new = _md5_file(os.path.join(UPLOAD_FOLDER, image_filename)) if image_filename else None
            if img_phash_new is None:
                img_phash_new = _phash_file(os.path.join(UPLOAD_FOLDER, image_filename)) if image_filename else None
            if old_path and image_filename:
                # exact MD5
                if _md5_file(old_path) and img_md5_new and _md5_file(old_path) == img_md5_new:
                    return c
                # phash compare
                old_ph = _phash_file(old_path)
                if old_ph and img_phash_new and _hamming_hex(old_ph, img_phash_new) <= 5 and (not pincode or c.pincode == pincode):
                    return c
    return None

def maybe_award_badges(actor_type: str, actor_id: int):
    """Award badges based on accumulated events/stats.
    Users: first_complaint, verified_reporter (5 AI verified), first_resolution, streak_3/streak_7.
    NGOs: rapid_responder (3 fast resolves), resolver_bronze/silver/gold by total resolves.
    """
    if actor_type == 'user':
        # First complaint: any complaint_submit:% event
        submit_count = (
            GamificationEvent.query
            .filter_by(actor_type='user', actor_id=actor_id)
            .filter(GamificationEvent.action.like('complaint_submit:%'))
            .count()
        )
        if submit_count >= 1:
            badge = Badge.query.filter_by(code='first_complaint').first()
            if badge and not UserBadge.query.filter_by(user_id=actor_id, badge_id=badge.id).first():
                db.session.add(UserBadge(user_id=actor_id, badge_id=badge.id))
                u = User.query.get(actor_id)
                if u and u.email:
                    try:
                        send_user_email(u.email,
                                        'You earned a badge: First Complaint',
                                        'Great start! You earned the "First Complaint" badge.')
                    except Exception:
                        pass
        # Verified Reporter: 5 AI-verified complaints
        ai_verified_count = (
            GamificationEvent.query
            .filter_by(actor_type='user', actor_id=actor_id)
            .filter(GamificationEvent.action.like('ai_verified:%'))
            .count()
        )
        if ai_verified_count >= 5:
            badge = Badge.query.filter_by(code='verified_reporter').first()
            if badge and not UserBadge.query.filter_by(user_id=actor_id, badge_id=badge.id).first():
                db.session.add(UserBadge(user_id=actor_id, badge_id=badge.id))
                u = User.query.get(actor_id)
                if u and u.email:
                    try:
                        send_user_email(u.email,
                                        'You earned a badge: Verified Reporter',
                                        'Congrats! You earned the "Verified Reporter" badge for 5 AI-verified complaints.')
                    except Exception:
                        pass
        # First Resolution: any user_resolved:% event
        resolved_count = (
            GamificationEvent.query
            .filter_by(actor_type='user', actor_id=actor_id)
            .filter(GamificationEvent.action.like('user_resolved:%'))
            .count()
        )
        if resolved_count >= 1:
            badge = Badge.query.filter_by(code='first_resolution').first()
            if badge and not UserBadge.query.filter_by(user_id=actor_id, badge_id=badge.id).first():
                db.session.add(UserBadge(user_id=actor_id, badge_id=badge.id))
                u = User.query.get(actor_id)
                if u and u.email:
                    try:
                        send_user_email(u.email,
                                        'You earned a badge: First Resolution',
                                        'Awesome! A complaint you filed was resolved. Badge unlocked!')
                    except Exception:
                        pass
        # Streaks: simple daily streaks (3 and 7 days) based on recent submit events
        today = datetime.utcnow().date()
        # count distinct dates for last N days
        def distinct_days(n):
            start = datetime.combine(today - timedelta(days=n-1), datetime.min.time())
            rows = (
                db.session.query(func.date(GamificationEvent.created_at))
                .filter_by(actor_type='user', actor_id=actor_id)
                .filter(GamificationEvent.action.like('complaint_submit:%'))
                .filter(GamificationEvent.created_at >= start)
                .distinct().all()
            )
            return len(rows)
        if distinct_days(3) >= 3:
            badge = Badge.query.filter_by(code='streak_3').first()
            if badge and not UserBadge.query.filter_by(user_id=actor_id, badge_id=badge.id).first():
                db.session.add(UserBadge(user_id=actor_id, badge_id=badge.id))
        if distinct_days(7) >= 7:
            badge = Badge.query.filter_by(code='streak_7').first()
            if badge and not UserBadge.query.filter_by(user_id=actor_id, badge_id=badge.id).first():
                db.session.add(UserBadge(user_id=actor_id, badge_id=badge.id))
    else:
        # NGO badges
        # Rapid responder: 3 resolved_fast events
        fast_count = (
            GamificationEvent.query
            .filter_by(actor_type='ngo', actor_id=actor_id)
            .filter(GamificationEvent.action.like('resolved_fast:%'))
            .count()
        )
        if fast_count >= 3:
            badge = Badge.query.filter_by(code='rapid_responder').first()
            if badge and not NGOBadge.query.filter_by(ngo_id=actor_id, badge_id=badge.id).first():
                db.session.add(NGOBadge(ngo_id=actor_id, badge_id=badge.id))
        # Resolver tiers by total resolved events
        total_resolved = (
            GamificationEvent.query
            .filter_by(actor_type='ngo', actor_id=actor_id)
            .filter(GamificationEvent.action.like('resolved:%'))
            .count()
        )
        tiers = [
            ('resolver_bronze', 10),
            ('resolver_silver', 50),
            ('resolver_gold', 200),
        ]
        for code, threshold in tiers:
            if total_resolved >= threshold:
                badge = Badge.query.filter_by(code=code).first()
                if badge and not NGOBadge.query.filter_by(ngo_id=actor_id, badge_id=badge.id).first():
                    db.session.add(NGOBadge(ngo_id=actor_id, badge_id=badge.id))

# Initial badges seed

def seed_badges():
    try:
        existing = {b.code for b in Badge.query.all()}
        data = [
            ('first_complaint','First Complaint','Submitted your first complaint'),
            ('verified_reporter','Verified Reporter','5 AI-verified complaints'),
            ('first_resolution','First Resolution','A complaint you filed was resolved'),
            ('streak_3','Streak 3','Submitted complaints 3 days in a row'),
            ('streak_7','Streak 7','Submitted complaints 7 days in a row'),
            ('rapid_responder','Rapid Responder','NGO resolved 3 cases within 72 hours'),
            ('resolver_bronze','Resolver Bronze','NGO resolved 10 cases'),
            ('resolver_silver','Resolver Silver','NGO resolved 50 cases'),
            ('resolver_gold','Resolver Gold','NGO resolved 200 cases')
        ]
        for code, name, desc in data:
            if code not in existing:
                db.session.add(Badge(code=code, name=name, description=desc))
        db.session.commit()
    except Exception:
        db.session.rollback()

# Ensure tables exist, then schema tweaks and badge seed once on first incoming request
_BOOTSTRAP_DONE = False

@app.before_request
def _bootstrap_on_first_request():
    global _BOOTSTRAP_DONE
    if _BOOTSTRAP_DONE:
        return
    try:
        db.create_all()
    except Exception:
        pass
    _ensure_points_awarded_column()
    seed_badges()
    _BOOTSTRAP_DONE = True

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(1000))
    is_admin = db.Column(db.Boolean, default=False)
    is_ngo = db.Column(db.Boolean, default=False)

class Complaints(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    title = db.Column(db.String(200), nullable=True)     # optional
    category = db.Column(db.String(100), nullable=True)  # AI suggested
    location = db.Column(db.String(200), nullable=True)  # optional: browser location text
    pincode = db.Column(db.String(10), nullable=True)
    message = db.Column(db.String(1000))
    date = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200))
    status = db.Column(db.String(20), default='Submitted')
    ai_verified = db.Column(db.Boolean, default=False)
    ai_confidence = db.Column(db.Float, nullable=True)
    ai_notified = db.Column(db.Boolean, default=False)
    admin_notified = db.Column(db.Boolean, default=False)
    # Dedupe helpers (nullable; added via manual ALTERs)
    image_md5 = db.Column(db.String(32), nullable=True)
    image_phash = db.Column(db.String(32), nullable=True)
    text_fingerprint = db.Column(db.String(40), nullable=True)
    points_awarded = db.Column(JSON, nullable=True)  # if MySQL JSON not supported, we will fallback to TEXT in DB
class NGO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    org_reg_no = db.Column(db.String(100), nullable=True)
    approved = db.Column(db.Boolean, default=False)
    categories = db.Column(db.String(500), nullable=True)    # comma-separated
    coverage_pincodes = db.Column(db.String(1000), nullable=True)  # comma-separated
    proof_file = db.Column(db.String(255), nullable=True)
    contact_person = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    notes = db.Column(db.String(500), nullable=True)

class ComplaintAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complaint_id = db.Column(db.Integer, db.ForeignKey('complaints.cid'), nullable=False)
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'), nullable=False)
    status = db.Column(db.String(30), default='Assigned')  # Assigned, Accepted, Rejected, In-Progress, Resolved
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    accepted_at = db.Column(db.DateTime, nullable=True)
    due_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    notes = db.Column(db.String(1000), nullable=True)
    assigned_by = db.Column(db.Integer, nullable=True)
    source = db.Column(db.String(30), default='auto')

# --- login loader ---
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Admin creation (unchanged) ---
def create_admin():
    with app.app_context():
        admin_email = 'admin@ecoguard.com'
        admin_user = User.query.filter_by(email=admin_email).first()
        if not admin_user:
            encpassword = generate_password_hash('admin123')
            new_admin = User(username='admin', email=admin_email, password=encpassword, is_admin=True)
            db.session.add(new_admin)
            db.session.commit()
            print("✅ Admin created: email=admin@ecoguard.com, password=admin123")
create_admin()

# --- AI initialization (lazy) ---
text_classifier = None
image_classifier = None
image_zs_classifier = None  # CLIP zero-shot image classifier
resnet_model = None
resnet_weights = None
resnet_categories = None
AI_LABELS = ["Waste Management", "Water Issue", "Electricity", "Road Damage", "Pollution", "Other"]
# Use image labels without 'Other' for better mapping; we'll only fall back to 'Other' on low confidence
IMAGE_LABELS_NO_OTHER = ["Waste Management", "Water Issue", "Electricity", "Road Damage", "Pollution"]
# Thresholds
TEXT_CAT_MIN_CONF = 0.55
IMAGE_CAT_MIN_CONF = 0.55
RESNET_MIN_CONF = 0.55
FUSION_BONUS_MATCH = 0.05  # small bonus if text top matches image top

def init_ai():
    global text_classifier, image_classifier, image_zs_classifier, resnet_model, resnet_weights, resnet_categories
    if HF_AVAILABLE:
        try:
            if text_classifier is None:
                text_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
            if image_classifier is None:
                image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
            if image_zs_classifier is None:
                image_zs_classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
        except Exception as e:
            print("AI pipeline init failed:", e)
    if RESNET_AVAILABLE:
        try:
            if resnet_model is None:
                weights = models.ResNet50_Weights.DEFAULT
                resnet_model = models.resnet50(weights=weights)
                resnet_model.eval()
                resnet_weights = weights
                resnet_categories = weights.meta.get('categories', None)
        except Exception as e:
            print("ResNet init failed:", e)

# --- helper: simple image relevance check ---
def image_relevance_check(image_path):
    """
    Returns (is_relevant:bool, confidence:float, label:str)
    We consider image relevant if classifier returns a label indicating waste/garbage/pollution.
    """
    init_ai()
    if image_classifier is None:
        return (False, None, None)

    try:
        results = image_classifier(image_path, top_k=3)
        # results: list of dicts with 'label' and 'score'
        # examine top labels for keywords
        labels = [r['label'].lower() for r in results]
        scores = [r['score'] for r in results]

        # simple heuristic: if any label contains these keywords -> relevant
        keywords = ['trash', 'garbage', 'waste', 'dump', 'rubbish', 'pollution', 'litter']
        for lbl, sc in zip(labels, scores):
            for kw in keywords:
                if kw in lbl:
                    return (True, float(sc), lbl)
        # else not relevant
        return (False, float(scores[0]) if scores else None, labels[0] if labels else None)
    except Exception as e:
        print("image_relevance_check failed:", e)
        return (False, None, None)

# --- helper: image category suggestion (zero-shot with CLIP) ---

def classify_image_category(image_path):
    """
    Returns (label:str, score:float) using zero-shot image classification against IMAGE_LABELS_NO_OTHER.
    Falls back to (None, None) if unavailable.
    """
    init_ai()
    if 'image_zs_classifier' not in globals() or image_zs_classifier is None:
        return (None, None)
    try:
        res = image_zs_classifier(
            image_path,
            candidate_labels=IMAGE_LABELS_NO_OTHER,
            hypothesis_template="a photo related to {}"
        )
        if isinstance(res, list) and len(res) > 0:
            top = res[0]
            return (top.get('label'), float(top.get('score', 0.0)))
        return (None, None)
    except Exception as e:
        print("classify_image_category failed:", e)
        return (None, None)

# --- helper: ResNet50 classification + mapping to app categories ---

def _resnet_predict(image_path):
    init_ai()
    if resnet_model is None or resnet_weights is None:
        return (None, None)
    try:
        preprocess = resnet_weights.transforms()
        img = Image.open(image_path).convert('RGB')
        batch = preprocess(img).unsqueeze(0)
        with torch.no_grad():
            out = resnet_model(batch)
            prob = torch.nn.functional.softmax(out[0], dim=0)
            score, idx = torch.max(prob, dim=0)
            score = float(score.item())
            label = resnet_categories[int(idx.item())] if resnet_categories else str(int(idx.item()))
        return (label, score)
    except Exception as e:
        print("ResNet prediction failed:", e)
        return (None, None)

def _map_imagenet_to_app(label: str) -> str | None:
    if not label:
        return None
    L = label.lower()
    if any(k in L for k in ["trash","garbage","rubbish","dump","litter","landfill","bin"]):
        return "Waste Management"
    if any(k in L for k in ["water","flood","leak","pipe","sewer","drain"]):
        return "Water Issue"
    if any(k in L for k in ["wire","electric","transformer","cable","pole","power"]):
        return "Electricity"
    if any(k in L for k in ["road","street","pothole","asphalt","sidewalk","pavement"]):
        return "Road Damage"
    if any(k in L for k in ["smoke","smog","fume","fumes","exhaust","emission","pollution"]):
        return "Pollution"
    return None

# --- helper: text category suggestion ---
def suggest_category_from_text(text):
    init_ai()
    if text_classifier is None:
        return None
    try:
        res = text_classifier(text, AI_LABELS)
        # res['labels'][0] is top label
        top_label = res['labels'][0]
        score = float(res['scores'][0])
        return (top_label, score)
    except Exception as e:
        print("suggest_category_from_text failed:", e)
        return None

# --- helper: send email (simple) ---
def send_user_email(to_email, subject, body):
    try:
        msg = Message(subject=subject, recipients=[to_email], body=f"Ecovision : Please check your status for your Environmental Issue: {body}")
        mail.send(msg)
        return True
    except Exception as e:
        print("send_user_email failed:", e)
        return False

# ---------------- ROUTES ----------------
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

# --- signup/login/logout (unchanged) ---
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

# ---------------- Complaint submission ----------------
@app.route('/Complaint', methods=['GET', 'POST'])
@login_required
def Complaint():
    if request.method == "POST":
        email = request.form.get('email')
        message = request.form.get('message')
        date = request.form.get('date')
        pincode = request.form.get('pincode') or None
        # optional title/category fields provided by user
        title = request.form.get('title') or None
        user_category = request.form.get('category') or None
        file = request.files.get('image')

        # Validate
        if not email or not message or not date or not file:
            flash("All fields including image are required", "danger")
            return render_template('Complaint.html')
        if not pincode:
            flash("Pincode is required", "danger")
            return render_template('Complaint.html')

        if not allowed_file(file.filename):
            flash("Invalid file type. Allowed: jpg/jpeg/png/pdf", "danger")
            return render_template('Complaint.html')

        # Save file securely (avoid collisions by prefixing timestamp)
        filename = secure_filename(file.filename)
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
        filename = f"{timestamp}_{filename}"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)

        # AI: suggest category from text (non-blocking best-effort)
        text_cat = None
        text_conf = None
        try:
            cat_res = suggest_category_from_text(message)
            if cat_res:
                text_cat, text_conf = cat_res[0], cat_res[1]
        except Exception as e:
            print("Category suggestion skipped:", e)

        # AI: image relevance check (fast heuristic)
        ai_verified = False
        ai_conf = None
        ai_label = None
        try:
            rel, conf, lbl = image_relevance_check(save_path)
            ai_verified = bool(rel)
            ai_conf = conf
            ai_label = lbl
        except Exception as e:
            print("Image relevance check skipped:", e)

        # AI: image category via zero-shot (maps directly to our labels)
        image_cat = None
        image_conf = None
        try:
            image_cat, image_conf = classify_image_category(save_path)
        except Exception as e:
            print("Image zero-shot classification skipped:", e)

        # Fuse predictions: prefer highest-confidence among text/image when >= thresholds
        fused_cat = None
        fused_score = -1.0
        # apply small bonus if both agree on the same label
        if text_cat and image_cat and text_cat == image_cat and text_conf and image_conf:
            text_conf = min(1.0, text_conf + FUSION_BONUS_MATCH)
            image_conf = min(1.0, image_conf + FUSION_BONUS_MATCH)
        # consider only strong candidates
        candidates = []
        if text_cat and (text_conf or 0) >= TEXT_CAT_MIN_CONF:
            candidates.append((text_cat, float(text_conf)))
        if image_cat and (image_conf or 0) >= IMAGE_CAT_MIN_CONF:
            candidates.append((image_cat, float(image_conf)))
        if candidates:
            fused_cat, fused_score = max(candidates, key=lambda x: x[1])
        # prefer user-provided category if AI is unsure
        final_category = fused_cat or user_category
        # only use 'Other' if everything is low-confidence and user didn't provide category
        if final_category is None and text_cat is not None and (text_conf or 0) < TEXT_CAT_MIN_CONF and (image_conf or 0) < IMAGE_CAT_MIN_CONF:
            final_category = 'Other'

        # Compute hashes/fingerprints once
        text_fp = _normalize_text_fp(title, message, pincode)
        img_md5 = _md5_file(save_path)
        img_ph = _phash_file(save_path)

        # Duplicate check with md5/phash/text fp
        dup = _check_duplicate_complaint(email, title, message, pincode, filename,
                                        pre_md5=img_md5, pre_phash=img_ph, pre_text_fp=text_fp)
        if dup:
            try:
                flash(f"Possible duplicate of complaint #{dup.cid}. We did not create a new one.", "warning")
            except Exception:
                pass
            return redirect(url_for('prcomplaint'))

        # Additional ResNet50 classification and fusion
        rn_label, rn_score = _resnet_predict(save_path)
        rn_app = _map_imagenet_to_app(rn_label) if rn_label else None
        # add to candidates if strong
        candidates = []
        if final_category:
            # keep previous fused result with its score if known
            base_score = fused_score if isinstance(fused_score, (float,int)) else 0.0
            candidates.append((final_category, float(base_score)))
        if rn_app and (rn_score or 0) >= RESNET_MIN_CONF:
            candidates.append((rn_app, float(rn_score)))
        if image_cat and (image_conf or 0) >= IMAGE_CAT_MIN_CONF:
            candidates.append((image_cat, float(image_conf)))
        if text_cat and (text_conf or 0) >= TEXT_CAT_MIN_CONF:
            candidates.append((text_cat, float(text_conf)))
        if candidates:
            final_category, _ = max(candidates, key=lambda x: x[1])
        if not final_category:
            final_category = user_category or rn_app or image_cat or text_cat or 'Other'

        new_complaint = Complaints(
            email=email,
            title=title,
            category=final_category,
            message=message,
            date=date,
            pincode=pincode,
            image=filename,
            ai_verified=ai_verified,
            ai_confidence=ai_conf,
            image_md5=img_md5,
            image_phash=img_ph,
            text_fingerprint=text_fp
        )
        db.session.add(new_complaint)
        db.session.commit()

        # Log a zero-point submit event to enable badges like first_complaint and streaks
        try:
            u = User.query.filter_by(email=email).first()
            if u:
                award_points_unique('user', u.id, f'complaint_submit:{new_complaint.cid}', 0, { 'complaint_id': new_complaint.cid })
        except Exception:
            pass

        # Award user points only on AI verification (idempotent per complaint)
        if ai_verified:
            try:
                u = User.query.filter_by(email=email).first()
                if u:
                    award_points_unique('user', u.id, f'ai_verified:{new_complaint.cid}', 10, { 'complaint_id': new_complaint.cid })
            except Exception:
                pass

        # Auto-assign to NGO by pincode+category
        try:
            auto_assign_to_ngo(new_complaint)
        except Exception as e:
            print("auto_assign_to_ngo failed:", e)

        # If AI verified (green), notify user by email (only once)
        if ai_verified:
            try:
                send_user_email(email,
                                "Your complaint has been auto-verified",
                                f"Your complaint (ID: {new_complaint.cid}) was automatically verified by our AI system. Current status: {new_complaint.status}.")
                # record notification
                new_complaint.ai_notified = True
                db.session.commit()
            except Exception as e:
                print("Failed to send AI-notification:", e)

        flash("Complaint submitted successfully!", "primary")
        return redirect(url_for('prcomplaint'))

    return render_template('Complaint.html')

# ---------------- user complaint view ----------------
@app.route('/prcomplaint')
@login_required
def prcomplaint():
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    comp = Complaints.query.filter_by(email=current_user.email).order_by(Complaints.cid.desc()).all()
    # fetch all badges earned by this user
    user_badges = (
        db.session.query(Badge.code, Badge.name, Badge.description)
        .join(UserBadge, UserBadge.badge_id == Badge.id)
        .join(User, User.id == UserBadge.user_id)
        .filter(User.id == current_user.id)
        .order_by(UserBadge.awarded_at.desc())
        .all()
    )
    return render_template('prcomplaint.html', comp=comp, user_badges=user_badges)

# ---------------- template context: expose NGO name for navbar ----------------
@app.context_processor
def inject_current_ngo_name():
    ngo_name = None
    try:
        if current_user.is_authenticated and getattr(current_user, 'is_ngo', False):
            ngo = NGO.query.filter_by(user_id=current_user.id).first()
            if ngo:
                ngo_name = ngo.name
    except Exception:
        pass
    return dict(current_ngo_name=ngo_name)

@app.context_processor
def inject_gamification_stats():
    us = None
    ns = None
    try:
        if current_user.is_authenticated:
            if getattr(current_user, 'is_ngo', False):
                ngo = NGO.query.filter_by(user_id=current_user.id).first()
                if ngo:
                    ns = NGOStats.query.filter_by(ngo_id=ngo.id).first()
            else:
                us = UserStats.query.filter_by(user_id=current_user.id).first()
    except Exception:
        pass
    return dict(current_user_stats=us, current_ngo_stats=ns)

# ---------------- admin dashboard ----------------
@app.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    comp = Complaints.query.order_by(Complaints.cid.desc()).all()
    ngos = NGO.query.order_by(NGO.id.desc()).all()
    # Build latest assignment info per complaint (who updated and status)
    complaint_ids = [c.cid for c in comp]
    assign_map = {}
    if complaint_ids:
        assignments = (
            ComplaintAssignment.query
            .filter(ComplaintAssignment.complaint_id.in_(complaint_ids))
            .order_by(ComplaintAssignment.updated_at.desc())
            .all()
        )
        # keep latest per complaint_id
        for a in assignments:
            if a.complaint_id not in assign_map:
                ngo = NGO.query.get(a.ngo_id)
                assign_map[a.complaint_id] = {
                    'ngo_name': (ngo.name if ngo else 'NGO #'+str(a.ngo_id)),
                    'status': a.status,
                    'updated_at': a.updated_at,
                    'assignment_id': a.id,
                }
    # Leaderboards (top 10)
    top_ngos = db.session.query(NGO.name, NGOStats.points, NGOStats.level) \
        .join(NGO, NGO.id == NGOStats.ngo_id) \
        .order_by(NGOStats.points.desc()) \
        .limit(10).all()
    top_users = db.session.query(User.username, UserStats.points, UserStats.level) \
        .join(User, User.id == UserStats.user_id) \
        .order_by(UserStats.points.desc()) \
        .limit(10).all()
    # Allow optional dedupe results injection
    dedupe_candidates = request.args.get('dedupe')
    return render_template('admin_dashboard.html', comp=comp, ngos=ngos, assign_map=assign_map,
                           top_ngos=top_ngos, top_users=top_users, dedupe_candidates=None)

# update status route (admin)
@app.route('/update_status/<int:cid>', methods=['POST'])
@login_required
def update_status(cid):
    if not current_user.is_admin:
        abort(403)
    complaint = Complaints.query.get_or_404(cid)
    # Do not allow status changes for duplicates
    if getattr(complaint, 'duplicate_of', None) or complaint.status == 'Duplicate':
        flash(f"Complaint #{cid} is marked as duplicate and cannot be updated.", "warning")
        return redirect(url_for('admin_dashboard'))
    new_status = request.form.get('status')
    if new_status:
        prev_status = complaint.status
        complaint.status = new_status
        db.session.commit()
        # Award user points only upon AI verification status
        if new_status == 'Verified':
            try:
                u = User.query.filter_by(email=complaint.email).first()
                if u:
                    award_points_unique('user', u.id, f'ai_verified:{complaint.cid}', 10, { 'complaint_id': complaint.cid })
            except Exception:
                pass
        flash(f"Complaint #{cid} status updated to '{new_status}'", "success")

        # If admin sets a status that should notify user (for example "Verified" or "Resolved"), email user
        # We'll treat "Verified" and "Resolved" as statuses that trigger email
        if new_status == 'Resolved':
            try:
                u = User.query.filter_by(email=complaint.email).first()
                if u:
                    award_points_unique('user', u.id, f'user_resolved:{complaint.cid}', 0, { 'complaint_id': complaint.cid })
            except Exception:
                pass
        notify_statuses = {"Verified", "Resolved"}
        if new_status in notify_statuses and not complaint.admin_notified:
            try:
                send_user_email(complaint.email,
                                f"Complaint #{cid} status updated to {new_status}",
                                f"Your complaint (ID: {cid}) status changed from {prev_status} to {new_status}.")
                complaint.admin_notified = True
                db.session.commit()
            except Exception as e:
                print("Failed to send admin-notification:", e)

    return redirect(url_for('admin_dashboard'))

# --- Dedupe review & actions ---
@app.route('/admin/dedupe_review')
@login_required
def admin_dedupe_review():
    if not current_user.is_admin:
        abort(403)
    # Build candidate groups
    candidates = []
    try:
        # Text fingerprint groups
        tf_groups = db.session.query(Complaints.text_fingerprint, func.count(Complaints.cid)) \
            .filter(Complaints.text_fingerprint.isnot(None)) \
            .group_by(Complaints.text_fingerprint).having(func.count(Complaints.cid) > 1) \
            .order_by(func.count(Complaints.cid).desc()).limit(50).all()
        for fp, cnt in tf_groups:
            items = Complaints.query.filter_by(text_fingerprint=fp).order_by(Complaints.cid.desc()).all()
            candidates.append({ 'type': 'text', 'key': fp, 'items': items })
        # Image MD5 groups
        md5_groups = db.session.query(Complaints.image_md5, func.count(Complaints.cid)) \
            .filter(Complaints.image_md5.isnot(None)) \
            .group_by(Complaints.image_md5).having(func.count(Complaints.cid) > 1) \
            .order_by(func.count(Complaints.cid).desc()).limit(50).all()
        for md5, cnt in md5_groups:
            items = Complaints.query.filter_by(image_md5=md5).order_by(Complaints.cid.desc()).all()
            candidates.append({ 'type': 'image_md5', 'key': md5, 'items': items })
        # Perceptual hash near-duplicates (last 500)
        recent = Complaints.query.filter(Complaints.image_phash.isnot(None)).order_by(Complaints.cid.desc()).limit(500).all()
        rec_pairs = []
        bucket = {}
        for c in recent:
            key = (c.image_phash or '')[:4]
            bucket.setdefault(key, []).append(c)
        for key, arr in bucket.items():
            n = len(arr)
            for i in range(n):
                for j in range(i+1, n):
                    a, b = arr[i], arr[j]
                    try:
                        if _hamming_hex(a.image_phash, b.image_phash) <= 5 and (not a.pincode or a.pincode == b.pincode):
                            rec_pairs.append((a, b))
                    except Exception:
                        pass
        if rec_pairs:
            # flatten into candidate groups by pair
            for a, b in rec_pairs[:100]:
                candidates.append({ 'type': 'image_phash', 'key': f"{a.image_phash}~{b.image_phash}", 'items': [a, b] })
    except Exception as e:
        print('dedupe_review failed:', e)
    comp = Complaints.query.order_by(Complaints.cid.desc()).all()
    ngos = NGO.query.order_by(NGO.id.desc()).all()
    top_ngos = db.session.query(NGO.name, NGOStats.points, NGOStats.level).join(NGO, NGO.id==NGOStats.ngo_id).order_by(NGOStats.points.desc()).limit(10).all()
    top_users = db.session.query(User.username, UserStats.points, UserStats.level).join(User, User.id==UserStats.user_id).order_by(UserStats.points.desc()).limit(10).all()
    return render_template('admin_dashboard.html', comp=comp, ngos=ngos, assign_map={}, top_ngos=top_ngos, top_users=top_users, dedupe_candidates=candidates)

@app.route('/admin/mark_duplicate', methods=['POST'])
@login_required
def admin_mark_duplicate():
    if not current_user.is_admin:
        abort(403)
    primary_id = request.form.get('primary_id', type=int)
    dup_id = request.form.get('dup_id', type=int)
    if not primary_id or not dup_id:
        flash('Missing primary/duplicate ids', 'warning')
        return redirect(url_for('admin_dedupe_review'))
    dup = Complaints.query.get_or_404(dup_id)

    updated = False
    # Try ORM first (works if model had duplicate_of at startup)
    try:
        setattr(dup, 'duplicate_of', primary_id)
        dup.status = 'Duplicate'
        db.session.commit()
        updated = True
    except Exception:
        db.session.rollback()
    # Fallback: raw SQL in case ORM attribute missing
    if not updated:
        try:
            db.session.execute(
                text('UPDATE complaints SET duplicate_of = :primary_id, status = :status WHERE cid = :cid'),
                { 'primary_id': primary_id, 'status': 'Duplicate', 'cid': dup_id }
            )
            db.session.commit()
            updated = True
        except Exception:
            db.session.rollback()
    if updated:
        # Deduct 5 points from the complaint owner (once)
        try:
            u = User.query.filter_by(email=dup.email).first()
            if u:
                award_points_unique('user', u.id, f'duplicate_penalty:{dup.cid}', -5, { 'duplicate_of': primary_id, 'complaint_id': dup.cid })
        except Exception:
            pass
        flash(f'Marked #{dup_id} as duplicate of #{primary_id} and deducted 5 points from the reporter', 'success')
    else:
        flash('Failed to mark duplicate. Ensure column exists and restart the server.', 'danger')

    # Fallback: raw SQL in case ORM attribute missing
    if not updated:
        try:
            db.session.execute(
                text('UPDATE complaints SET duplicate_of = :primary_id, status = :status WHERE cid = :cid'),
                { 'primary_id': primary_id, 'status': 'Duplicate', 'cid': dup_id }
            )
            db.session.commit()
            updated = True
        except Exception:
            db.session.rollback()

    if updated:
        # Deduct 5 points from the complaint owner (once)
        try:
            u = User.query.filter_by(email=dup.email).first()
            if u:
                award_points_unique('user', u.id, f'duplicate_penalty:{dup.cid}', -5, { 'duplicate_of': primary_id, 'complaint_id': dup.cid })
        except Exception:
            pass
        flash(f'Marked #{dup_id} as duplicate of #{primary_id} and deducted 5 points from the reporter', 'success')
    else:
        flash('Failed to mark duplicate. Ensure column exists and restart the server.', 'danger')

    return redirect(url_for('admin_dedupe_review'))

# ... (rest of the code remains the same)
@app.route('/admin/backfill_hashes')
@login_required
def admin_backfill_hashes():
    if not current_user.is_admin:
        abort(403)
    limit = request.args.get('limit', default=500, type=int)
    q = Complaints.query.filter((Complaints.image_md5.is_(None)) | (Complaints.image_phash.is_(None)) | (Complaints.text_fingerprint.is_(None))).order_by(Complaints.cid.asc()).limit(limit)
    count = 0
    for c in q.all():
        try:
            # text fp
            if not c.text_fingerprint:
                c.text_fingerprint = _normalize_text_fp(getattr(c, 'title', None), getattr(c, 'message', None), getattr(c, 'pincode', None))
            # image hashes
            if c.image:
                path = os.path.join(UPLOAD_FOLDER, c.image)
                if not c.image_md5:
                    c.image_md5 = _md5_file(path)
                if not c.image_phash:
                    c.image_phash = _phash_file(path)
            count += 1
        except Exception:
            pass
    try:
        db.session.commit()
        flash(f'Backfilled hashes for {count} complaints', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Backfill failed', 'danger')
    return redirect(url_for('admin_dashboard'))

# --- edit route: admin only ---
@app.route('/edit/<int:cid>', methods=['GET', 'POST'])
@login_required
def edit(cid):
    complaint = Complaints.query.get_or_404(cid)
    if not current_user.is_admin:
        abort(403)

    if request.method == "POST":
        message = request.form.get('message')
        date = request.form.get('date')
        image = request.form.get('image')  # admin can edit image filename only if needed
        status = request.form.get('status')
        category = request.form.get('category')

        if message: complaint.message = message
        if date: complaint.date = date
        if image: complaint.image = image
        if status: complaint.status = status
        if category: complaint.category = category

        db.session.commit()
        flash("Complaint updated successfully", "success")
        return redirect(url_for('admin_dashboard'))

    return render_template('edit.html', posts=complaint)

# --- delete route (same permissions) ---
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

# ---------------- NGO: self-signup ----------------
@app.route('/ngo/signup', methods=['GET', 'POST'])
def ngo_signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('ngo_name')
        org_reg_no = request.form.get('org_reg_no')
        categories = request.form.get('categories')
        coverage_pincodes = request.form.get('coverage_pincodes')
        contact_person = request.form.get('contact_person')
        phone = request.form.get('phone')
        proof = request.files.get('proof')

        if not all([username, email, password, name, coverage_pincodes]) or proof is None:
            flash('All required fields and proof document are needed', 'danger')
            return render_template('ngo_signup.html')

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'warning')
            return render_template('ngo_signup.html')

        encpassword = generate_password_hash(password)
        user = User(username=username, email=email, password=encpassword, is_ngo=True)
        db.session.add(user)
        db.session.commit()

        proof_file = save_proof(proof)
        ngo = NGO(
            user_id=user.id,
            name=name,
            org_reg_no=org_reg_no,
            approved=False,
            categories=(categories or None),
            coverage_pincodes=coverage_pincodes,
            proof_file=proof_file,
            contact_person=contact_person,
            phone=phone,
            email=email
        )
        db.session.add(ngo)
        db.session.commit()
        flash('NGO registration submitted. Await admin approval.', 'success')
        return redirect(url_for('login'))

    return render_template('ngo_signup.html')


@app.route('/pincode_map/<pincode>')
def pincode_map(pincode):
    # basic normalization and validation
    pincode = (pincode or '').strip()
    # allow only digits; optional: enforce 6 digits
    if not pincode.isdigit() or len(pincode) != 6:
        flash('Invalid pincode for map view', 'warning')
        return redirect(url_for('index'))
    return render_template('pincode_map.html', pincode=pincode)

# ---------------- Admin: manage NGOs ----------------
@app.route('/admin/ngos')
@login_required
def admin_ngos():
    if not current_user.is_admin:
        abort(403)
    ngos = NGO.query.order_by(NGO.id.desc()).all()
    return render_template('admin_ngos.html', ngos=ngos)

@app.route('/admin/ngos/<int:ngo_id>/approve', methods=['POST'])
@login_required
def approve_ngo(ngo_id):
    if not current_user.is_admin:
        abort(403)
    ngo = NGO.query.get_or_404(ngo_id)
    ngo.approved = True
    db.session.commit()
    # notify NGO by email
    if ngo.email:
        try:
            send_user_email(ngo.email, 'Your NGO has been approved', 'Your NGO registration has been approved. You can now access the NGO Dashboard to manage assignments.')
        except Exception as e:
            print('NGO approval email failed:', e)
    flash('NGO approved', 'success')
    return redirect(request.referrer or url_for('admin_ngos'))

# ---------------- NGO Dashboard ----------------
@app.route('/ngo/dashboard')
@login_required
def ngo_dashboard_view():
    if not current_user.is_ngo:
        abort(403)
    ngo = NGO.query.filter_by(user_id=current_user.id).first()
    if not ngo or not ngo.approved:
        flash('Your NGO is pending approval', 'warning')
        return render_template('ngo_pending.html', ngo=ngo)
    assignments = ComplaintAssignment.query.filter_by(ngo_id=ngo.id).order_by(ComplaintAssignment.assigned_at.desc()).all()
    # Fetch complaint details for display
    complaint_ids = [a.complaint_id for a in assignments]
    complaints = Complaints.query.filter(Complaints.cid.in_(complaint_ids)).all() if complaint_ids else []
    complaint_map = {c.cid: c for c in complaints}
    return render_template('ngo_dashboard.html', assignments=assignments, complaint_map=complaint_map)

# ---------------- NGO Assignment Actions ----------------
@app.route('/ngo/assignments/<int:assign_id>/accept', methods=['POST'])
@login_required
def ngo_accept_assignment(assign_id):
    if not current_user.is_ngo:
        abort(403)
    ngo = NGO.query.filter_by(user_id=current_user.id).first_or_404()
    a = ComplaintAssignment.query.get_or_404(assign_id)
    if a.ngo_id != ngo.id:
        abort(403)
    a.status = 'Accepted'
    a.accepted_at = datetime.utcnow()
    if not a.due_at:
        a.due_at = datetime.utcnow() + timedelta(days=3)
    db.session.commit()
    # Gamification: NGO +5 on accepting (idempotent per assignment)
    try:
        award_points_unique('ngo', ngo.id, f"assignment_accept:{a.id}", 5, { 'assignment_id': a.id, 'complaint_id': a.complaint_id })
    except Exception:
        pass
    flash('Assignment accepted', 'success')
    return redirect(url_for('ngo_dashboard_view'))

@app.route('/ngo/assignments/<int:assign_id>/reject', methods=['POST'])
@login_required
def ngo_reject_assignment(assign_id):
    if not current_user.is_ngo:
        abort(403)
    ngo = NGO.query.filter_by(user_id=current_user.id).first_or_404()
    a = ComplaintAssignment.query.get_or_404(assign_id)
    if a.ngo_id != ngo.id:
        abort(403)
    a.status = 'Rejected'
    db.session.commit()
    flash('Assignment rejected', 'warning')
    return redirect(url_for('ngo_dashboard_view'))

@app.route('/ngo/assignments/<int:assign_id>/status', methods=['POST'])
@login_required
def ngo_update_status(assign_id):
    if not current_user.is_ngo:
        abort(403)
    ngo = NGO.query.filter_by(user_id=current_user.id).first_or_404()
    a = ComplaintAssignment.query.get_or_404(assign_id)
    if a.ngo_id != ngo.id:
        abort(403)
    new_status = request.form.get('status')
    notes = request.form.get('notes')
    if new_status:
        a.status = new_status
    if notes:
        a.notes = notes
    db.session.commit()
    # Gamification awards
    try:
        if new_status == 'In-Progress':
            award_points_unique('ngo', ngo.id, f"inprogress:{a.id}", 5, { 'assignment_id': a.id, 'complaint_id': a.complaint_id })
        if new_status == 'Resolved':
            # base points
            award_points_unique('ngo', ngo.id, f"resolved:{a.id}", 25, { 'assignment_id': a.id, 'complaint_id': a.complaint_id })
            # fast bonus if resolved within 72h from assigned/accepted
            base_time = a.accepted_at or a.assigned_at
            fast = False
            if base_time:
                elapsed = datetime.utcnow() - base_time
                if elapsed.total_seconds() <= 72 * 3600:
                    award_points_unique('ngo', ngo.id, f"resolved_fast:{a.id}", 10, { 'assignment_id': a.id, 'complaint_id': a.complaint_id, 'hours': elapsed.total_seconds()/3600 })
                    fast = True
            # Log a zero-point user resolution event for badge tracking
            comp = Complaints.query.get(a.complaint_id)
            if comp:
                u = User.query.filter_by(email=comp.email).first()
                if u:
                    award_points_unique('user', u.id, f'user_resolved:{comp.cid}', 0, { 'complaint_id': comp.cid, 'fast': fast })
    except Exception:
        pass
    # Notify complaint user concisely on status changes handled by NGO
    if new_status in ('Resolved', 'In-Progress'):
        comp = Complaints.query.get(a.complaint_id)
        if comp and comp.email:
            try:
                status_text = 'resolved' if new_status == 'Resolved' else 'in progress'
                ok = send_user_email(
                    comp.email,
                    f"Update: Complaint #{comp.cid} {new_status}",
                    f"NGO {ngo.name} has marked your complaint #{comp.cid} as {status_text}."
                )
                flash(('User notified: ' + new_status) if ok else 'Failed to notify user', 'success' if ok else 'danger')
            except Exception as e:
                print('User status email failed:', e)
                flash('Failed to notify user (exception)', 'danger')
    flash('Assignment updated', 'success')
    return redirect(url_for('ngo_dashboard_view'))

# NGO can email the complaint user directly
@app.route('/ngo/assignments/<int:assign_id>/email', methods=['POST'])
@login_required
def ngo_email_user(assign_id):
    if not current_user.is_ngo:
        abort(403)
    ngo = NGO.query.filter_by(user_id=current_user.id).first_or_404()
    a = ComplaintAssignment.query.get_or_404(assign_id)
    if a.ngo_id != ngo.id:
        abort(403)
    comp = Complaints.query.get_or_404(a.complaint_id)
    subject = request.form.get('subject') or f"Regarding your complaint #{comp.cid}"
    body = request.form.get('body') or ""
    ok = False
    if comp.email:
        try:
            ok = send_user_email(comp.email, subject, body)
        except Exception as e:
            print('NGO -> user email failed:', e)
    flash('Email sent to user' if ok else 'Failed to send email', 'success' if ok else 'danger')
    return redirect(url_for('ngo_dashboard_view'))

# ---------------- Admin: manual assignment ----------------
@app.route('/admin/assign', methods=['POST'])
@login_required
def admin_assign():
    if not current_user.is_admin:
        abort(403)
    complaint_id = request.form.get('complaint_id', type=int)
    ngo_id = request.form.get('ngo_id', type=int)
    if not complaint_id or not ngo_id:
        flash('Complaint and NGO are required', 'danger')
        return redirect(url_for('admin_dashboard'))
    assign = ComplaintAssignment(
        complaint_id=complaint_id,
        ngo_id=ngo_id,
        status='Assigned',
        due_at=datetime.utcnow() + timedelta(days=3),
        assigned_by=current_user.id,
        source='manual'
    )
    db.session.add(assign)
    db.session.commit()
    # email NGO about the manual assignment
    ngo = NGO.query.get(ngo_id)
    comp = Complaints.query.get(complaint_id)
    if ngo and ngo.email:
        try:
            send_user_email(ngo.email,
                            f'New complaint assigned manually #{comp.cid if comp else complaint_id}',
                            f'A complaint (ID: {comp.cid if comp else complaint_id}) has been assigned to your NGO.')
        except Exception as e:
            print('Manual assignment NGO email failed:', e)
    flash('Complaint assigned to NGO', 'success')
    return redirect(url_for('admin_dashboard'))

# ---------------- Matching & Auto-assignment ----------------

def _parse_list(csv_text):
    if not csv_text:
        return []
    return [x.strip() for x in csv_text.split(',') if x.strip()]

def find_candidate_ngos(category: str, pincode: str):
    if not category or not pincode:
        return []
    candidates = []
    for ngo in NGO.query.filter_by(approved=True).all():
        cats = set(map(str.lower, _parse_list(ngo.categories))) if ngo.categories else set()
        pins = set(_parse_list(ngo.coverage_pincodes)) if ngo.coverage_pincodes else set()
        if (not cats or category.lower() in cats) and (not pins or pincode in pins):
            candidates.append(ngo)
    return candidates

def auto_assign_to_ngo(complaint: Complaints):
    try:
        category = complaint.category
        pincode = complaint.pincode
        candidates = find_candidate_ngos(category, pincode)
        if not candidates:
            return False
        def open_count(ngo_id):
            return ComplaintAssignment.query.filter(ComplaintAssignment.ngo_id==ngo_id, ComplaintAssignment.status.in_(['Assigned','Accepted','In-Progress'])).count()
        candidates.sort(key=lambda n: open_count(n.id))
        chosen = candidates[0]
        assign = ComplaintAssignment(
            complaint_id=complaint.cid,
            ngo_id=chosen.id,
            status='Assigned',
            due_at=datetime.utcnow() + timedelta(days=3),
            source='auto'
        )
        db.session.add(assign)
        db.session.commit()
        if chosen.email:
            try:
                send_user_email(chosen.email, f"New complaint assigned #{complaint.cid}", f"A complaint in your coverage (pincode {pincode}) and category {category} has been assigned to your NGO.")
            except Exception as e:
                print('NGO email notify failed:', e)
        return True
    except Exception as e:
        print('auto_assign_to_ngo error:', e)
        return False

# --- run ---
if __name__ == "__main__":
    app.run(debug=True)
