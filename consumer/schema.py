from pyspark.sql.types import StructType, StructField, StringType, LongType


clickstream_schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("page_url", StringType(), True),
    StructField("timestamp", LongType(), True),
    StructField("country", StringType(), True),
])
