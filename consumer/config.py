# Spark + Kafka Consumer config
KAFKA_BOOTSTRAP = "kafka:9092"  # inside docker network
KAFKA_TOPIC = "clickstream"
CHECKPOINT_DIR = "/app/data/checkpoints"
OUTPUT_PATH = "/app/data/clean/"
