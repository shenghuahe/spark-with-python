from __future__ import print_function
from pyspark.sql import SparkSession

import sys
import entity.person as person

if __name__ == "__main__":

    print(sys.argv)

    if len(sys.argv) != 2:
        print("Usage: Json Mapper <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("Json Mapper") \
        .getOrCreate()

    output = spark.read.json(sys.argv[1], schema=person.schema).rdd \
        .map(person.person_factory) \
        .filter(lambda p: p.id > 262473) \
        .foreach(lambda p: print(p.id, p.firstName, p.lastName))

    spark.stop()
