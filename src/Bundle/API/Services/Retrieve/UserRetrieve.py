from src.Bundle.API.Entity.User import User


def retrieve_all():
    return User.query.all()


def retrieve_by_reference_code(user_reference_code):
    return User.query.filter(User.reference_code == user_reference_code).first()
