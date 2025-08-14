# Organization/generate_organization.py
import os
import csv
from faker import Faker

fake = Faker()

def generate_organization(num=3):
    data = [
        {
            "organization_id": i,
            "name": fake.company(),
            "industry": fake.job(),
            "address": fake.address().replace('\n', ', '),
            "contact_email": fake.company_email(),
            "contact_phone": fake.phone_number()
        }
        for i in range(1, num + 1)
    ]
    print(os.curdir)
    os.makedirs(".", exist_ok=True)
    with open("../data/Organization/organization.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return data
