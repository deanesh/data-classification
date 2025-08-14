# Interface/generate_interface.py
import os
import csv
import random
from faker import Faker

fake = Faker()

def generate_interfaces(devices, interfaces_per_device=2):
    data = []
    interface_id = 1
    for device in devices:
        for _ in range(interfaces_per_device):
            data.append({
                "interface_id": interface_id,
                "device_id": device["device_id"],
                "name": f"eth{random.randint(0, 3)}",
                "mac_address": fake.mac_address(),
                "status": random.choice(["up", "down", "unknown"]),
            })
            interface_id += 1

    os.makedirs("Interface", exist_ok=True)
    with open("../data/Interface/interfaces.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return data
