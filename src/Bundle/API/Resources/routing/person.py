from app import app
from src.Bundle.API.Services.Responder import PersonResponder


@app.route('/persons/', methods=['GET'])
def get_all_persons():
    return PersonResponder.get_all_persons()


@app.route('/persons/<string:person_reference_code>', methods=['GET'])
def get_person_by_reference_code(person_reference_code):
    return PersonResponder.get_person_by_reference_code(person_reference_code)
