from app.models import User

def create_user(name, email, gender, age):
    user = User(
        name = name,
        email = email,
        gender = gender,
        age = age)
    

    return user

def get_user():
    