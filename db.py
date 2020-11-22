from werkzeug.security import generate_password_hash
from models.db import *


def user_save(username, email,password):
     pswrd_hash = generate_password_hash(password)
     user_collection.insert_one({'_id': username, 'email': email, 'password':pswrd_hash})

