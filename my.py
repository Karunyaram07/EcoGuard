# using flask shell or a small script
from main1 import db, User
from werkzeug.security import generate_password_hash
admin = User(username='admin', email='admin@example.com',
             password=generate_password_hash('StrongAdminPass'), is_admin=True)
db.session.add(admin)
db.session.commit()
