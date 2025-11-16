from loguru import logger
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime, date_format, count
from config import INPUT_PATH, OUTPUT_PATH, JDBC_URL, DB_TABLE, DB_USER, DB_PASSWORD


def run_batch_job():
    spark = SparkSession.builder \
        .appName("ClickstreamBatchETL") \
        .getOrCreate()
    logger.debug("Spark Session created")

    # Read cleaned parquet
    df = spark.read.parquet(INPUT_PATH)
    logger.debug(f"Read cleaned data from: {INPUT_PATH}")

    # Daily aggregation: count page views by country
    agg_df = (
        df.withColumn(
            "date", date_format(from_unixtime(col("timestamp")), "yyyy-MM-dd")
        )
        .groupBy("date", "country")
        .agg(count("*").alias("page_views"))
    )
    logger.debug("Aggregated daily page views by country")

    # Write to parquet
    agg_df.write.mode("overwrite").parquet(OUTPUT_PATH)
    logger.debug(f"Wrote aggregated data to: {OUTPUT_PATH}")

    # Write to MySQL
    agg_df.write.format("jdbc") \
        .option("url", JDBC_URL) \
        .option("dbtable", DB_TABLE) \
        .option("user", DB_USER) \
        .option("password", DB_PASSWORD) \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .mode("overwrite") \
        .save()
    logger.debug(f"Wrote aggregated data to MySQL table: {DB_TABLE}")


if __name__ == "__main__":
    run_batch_job()
