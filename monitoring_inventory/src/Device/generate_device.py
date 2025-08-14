# Device/generate_device.py
import os
import csv
import random
from faker import Faker

fake = Faker()

def generate_devices(assets, dev_classes, num=20):
    data = [
        {
            "device_id": i,
            "asset_id": random.choice(assets)['asset_id'],
            "device_class_id": random.choice(dev_classes)['device_class_id'],
            "ip_address": fake.ipv4(),
            "serial_number": fake.uuid4(),
            "manufacturer": fake.company()
        }
        for i in range(1, num + 1)
    ]

    os.makedirs("Device", exist_ok=True)
    with open("../data/Device/devices.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return data
