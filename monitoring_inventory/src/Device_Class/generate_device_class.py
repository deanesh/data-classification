# Device_Class/generate_device_class.py
import os
import csv
from faker import Faker

fake = Faker()

def generate_device_class(num=5):
    data = [
        {
            "device_class_id": i,
            "name": fake.word().capitalize() + " Class",
            "description": fake.sentence()
        }
        for i in range(1, num + 1)
    ]

    os.makedirs("Device_Class", exist_ok=True)
    with open("../data/Device_Class/device_class.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return data
