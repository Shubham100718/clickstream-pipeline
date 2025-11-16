import time
import random
from faker import Faker

fake = Faker()


def generate_click_event():
    """Generate a random clickstream event."""
    event = {
        "user_id": fake.uuid4(),
        "page_url": random.choice(["/home", "/products", "/cart", "/checkout"]),
        "timestamp": int(time.time()),
        "country": fake.country()
    }
    return event
