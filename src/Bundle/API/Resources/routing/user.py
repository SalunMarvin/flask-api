from app import app
from src.Bundle.API.Services.Responder import UserResponder


@app.route('/users/', methods=['GET'])
def get_all_users():
    return UserResponder.get_all_users()


@app.route('/users/<string:user_reference_code>', methods=['GET'])
def get_user_by_reference_code(user_reference_code):
    return UserResponder.get_user_by_reference_code(user_reference_code)
