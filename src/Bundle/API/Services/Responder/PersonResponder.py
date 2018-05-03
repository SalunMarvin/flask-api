from src.Bundle.API.Services.Retrieve import PersonRetrieve
from src.Bundle.API.Entity.Person import person_schema, persons_schema


def get_all_persons():
    persons = PersonRetrieve.retrieve_all()
    normalized_persons = persons_schema.jsonify(persons)

    return normalized_persons


def get_person_by_reference_code(person_reference_code):
    person = PersonRetrieve.retrieve_by_reference_code(person_reference_code)
    normalized_person = person_schema.jsonify(person)

    return normalized_person
