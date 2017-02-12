import json


class Person:
    def __init__(self, id, firstName, lastName, gender, description):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.description = description


def dct_person_mapper(dct):
    return Person(dct['id'], dct['firstName'], dct['lastName'], dct['gender'], dct['description'])


line = '{"id":262477,"firstName":"AFirstName","lastName":"ALastName","gender":"Male","description":"Pleased him another was settled for. Moreover end horrible endeavor entrance any families. Income appear extent on of thrown in admire. Stanhill on we if vicinity material in. Saw him smallest you provided ecstatic supplied. Garret wanted expect remain as mr. Covered parlors concern we express in visited to do. Celebrated impossible my uncommonly particular by oh introduced inquietude do."}'
person = json.loads(line, object_hook=dct_person_mapper)
print(vars(person))
