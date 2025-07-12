from ..models import db, Skill

def get_skills_by_user(user_id):
    return Skill.query.filter_by(user_id=user_id).all()

def add_skill(user_id, name, skill_type):
    skill = Skill(user_id=user_id, name=name, type=skill_type)
    db.session.add(skill)
    db.session.commit()
    return skill
