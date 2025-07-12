from ..models import db, User

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_all_users():
    return User.query.all()

def update_user(user_id, data):
    user = get_user_by_id(user_id)
    if not user:
        return None
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user
