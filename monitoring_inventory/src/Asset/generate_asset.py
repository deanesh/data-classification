# Assets/generate_asset.py
import os
import csv
import random
from faker import Faker

fake = Faker()

def generate_assets(orgs, num=10):
    data = [
        {
            "asset_id": i,
            "name": fake.hostname(),
            "organization_id": random.choice(orgs)['organization_id'],
            "location": fake.city(),
            "purchase_date": fake.date_between(start_date='-3y', end_date='today').isoformat(),
            "owner": fake.name()
        }
        for i in range(1, num + 1)
    ]

    os.makedirs("Asset", exist_ok=True)
    with open("../data/Asset/assets.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return data
