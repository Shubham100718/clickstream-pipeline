from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from loguru import logger
from schema import clickstream_schema
from config import KAFKA_BOOTSTRAP, KAFKA_TOPIC, CHECKPOINT_DIR, OUTPUT_PATH


def run_streaming_job():
    spark = SparkSession.builder \
        .appName("KafkaClickstreamConsumer") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("INFO")
    logger.debug("Spark Session created")

    # Read Kafka stream
    df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP) \
        .option("subscribe", KAFKA_TOPIC) \
        .load()
    logger.debug(f"Subscribed to Kafka topic: {KAFKA_TOPIC}")

    # Parse JSON value
    parsed_df = df.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), clickstream_schema).alias("data")) \
        .select("data.*")
    logger.debug("Parsed JSON messages from Kafka")

    # Write to parquet
    query = parsed_df.writeStream \
        .format("parquet") \
        .option("checkpointLocation", CHECKPOINT_DIR) \
        .option("path", OUTPUT_PATH) \
        .outputMode("append") \
        .start()
    logger.debug(f"Writing cleaned data to: {OUTPUT_PATH}")

    query.awaitTermination()
    logger.debug("Streaming job terminated")


if __name__ == "__main__":
    run_streaming_job()
