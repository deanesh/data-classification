# Events/generate_events.py
import os
import csv
import random
from faker import Faker

fake = Faker()

def generate_events(devices, interfaces, num=50):
    data = [
        {
            "event_id": i,
            "timestamp": fake.date_time_between(start_date='-30d', end_date='now').isoformat(),
            "device_id": random.choice(devices)['device_id'],
            "interface_id": random.choice(interfaces)['interface_id'],
            "event_type": random.choice(["link_down", "link_up", "high_cpu", "reboot", "config_change"]),
            "description": fake.sentence()
        }
        for i in range(1, num + 1)
    ]

    os.makedirs("Event", exist_ok=True)
    with open("../data/Event/events.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
