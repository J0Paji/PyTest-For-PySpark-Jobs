import pytest
from pyspark.sql import SparkSession

#fixtures ensures this spark variable is passed on to all tests
@pytest.fixture(scope='session')
def spark():
    spark = SparkSession.builder\
            .master('local[*]')\
            .appName('PyTest')\
            .getOrCreate()
    return spark
    