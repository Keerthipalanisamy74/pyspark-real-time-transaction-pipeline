from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("TransactionPipeline") \
    .getOrCreate()

schema = "transaction_id INT, user_id INT, amount DOUBLE, timestamp DOUBLE"

df = spark.readStream \
    .option("header", "true") \
    .schema(schema) \
    .csv("transactions")

high_value = df.filter(col("amount") > 1000)

revenue = df.groupBy(
    window(col("timestamp").cast("timestamp"), "1 minute")
).sum("amount")

query = revenue.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
