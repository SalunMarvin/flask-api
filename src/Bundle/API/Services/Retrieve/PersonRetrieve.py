from src.Bundle.API.Entity.Person import Person


def retrieve_all():
    return Person.query.all()


def retrieve_by_reference_code(person_reference_code):
    return Person.query.filter(Person.reference_code == person_reference_code).first()
