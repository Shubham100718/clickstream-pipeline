import json
import time
from loguru import logger
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
from utils import generate_click_event
from config import BOOTSTRAP_SERVERS, TOPIC_NAME


def create_producer():
    for attempt in range(10):
        try:
            return KafkaProducer(
                bootstrap_servers=BOOTSTRAP_SERVERS,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
        except NoBrokersAvailable:
            logger.debug(f"[Retry {attempt+1}/10] Kafka not ready, waiting 5s...")
            time.sleep(5)
    raise Exception("Kafka still not reachable after retries")


def run_producer():
    producer = create_producer()
    logger.debug(f"Producing messages to topic: {TOPIC_NAME}")
    while True:
        event = generate_click_event()
        producer.send(TOPIC_NAME, event)
        logger.debug(f"Produced: {event}")
        time.sleep(5)  # 1 event per 5 seconds


if __name__ == "__main__":
    run_producer()
