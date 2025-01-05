#Chispa is great library for comparing PySpark DFs
from chispa.dataframe_comparer import *

#Adding the project to PYTHONPATH env variable
import sys
sys.path.append(".")

from jobs.simple_job import do_transformation
from collections import namedtuple

#Using named tuples because of the flexibility of creating objects without explicitly coding classes
testTbl = namedtuple('testTbl', 'group num')
testTbl_agg = namedtuple('testTbl_agg', 'group sum_num')

def test_testTbl(spark):
    input_data = [
        testTbl(group='A',
                num=1),
        testTbl(group='B',
                num=2)
    ]
    
    source_df = spark.createDataFrame(input_data)
    transformed_df = do_transformation(spark, source_df)

    expected_val = [
        testTbl_agg(group='A',
                    sum_num=1),
        testTbl_agg(group='B',
                    sum_num=2)
    ]
    expected_df = spark.createDataFrame(expected_val)
    assert_df_equality(transformed_df, expected_df)