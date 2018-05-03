from src.Bundle.API.Services.Retrieve import UserRetrieve
from src.Bundle.API.Entity.User import user_schema, users_schema


def get_all_users():
    users = UserRetrieve.retrieve_all()
    normalized_users = users_schema.jsonify(users)

    return normalized_users


def get_user_by_reference_code(user_reference_code):
    user = UserRetrieve.retrieve_by_reference_code(user_reference_code)
    normalized_user = user_schema.jsonify(user)

    return normalized_user
