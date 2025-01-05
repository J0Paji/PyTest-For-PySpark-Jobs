from pyspark.sql import SparkSession

def do_transformation(spark, df):
    query = '''
            SELECT group, sum(num) as sum_num
            FROM testTbl
            GROUP BY 1
            ORDER BY 1
            '''
    df.createOrReplaceTempView("testTbl")
    return spark.sql(query)

def main():
    spark = SparkSession.builder \
      .master("local[*]") \
      .appName("PyTest") \
      .getOrCreate()
    output_df = do_transformation(spark, spark.table("testTbl"))
    output_df.write.mode("overwrite").insertInto("testTbl_agg")
