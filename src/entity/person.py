from pyspark.sql import Row
from pyspark.sql.types import *


class Person:
    def __init__(self, id, firstName, lastName, gender, description):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.description = description


schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("firstName", StringType(), True),
    StructField("lastName", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("description", StringType(), True)])


def person_factory(row: Row):
    return Person(row['id'], row['firstName'], row['lastName'], row['gender'], row['description'])
