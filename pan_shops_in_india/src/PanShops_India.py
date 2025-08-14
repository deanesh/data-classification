
import csv
import random
from faker import Faker
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings(action="ignore")

fake = Faker('en_IN')

# ----- Constants -----
NUM_SHOPS = 300  # Number of pan shops
SALES_ENTRIES = 5000  # Total number of sales entries

STATES = ['Maharashtra', 'Uttar Pradesh', 'Tamil Nadu', 'Karnataka', 'Delhi', 'West Bengal']
CITIES = {
    'Maharashtra': ['Mumbai', 'Pune'],
    'Uttar Pradesh': ['Lucknow', 'Kanpur'],
    'Tamil Nadu': ['Chennai', 'Coimbatore'],
    'Karnataka': ['Bengaluru', 'Mysore'],
    'Delhi': ['New Delhi'],
    'West Bengal': ['Kolkata', 'Howrah']
}

PRODUCTS = [
    ("Cigarettes", ["International", "Domestic"]),
    ("Drinks", ["International", "Domestic"]),
    ("Chocolates", ["International", "Domestic"]),
    ("Biscuits", ["International", "Domestic"]),
    ("Chips", ["International", "Domestic"]),
    ("Lighters", ["Local"]),
    ("Chewing Gum", ["International", "Domestic"]),
    ("Peanuts", ["Local"]),
    ("Soda", ["International", "Domestic"]),
    ("Match Boxes", ["Local"]),
    ("Sweets", ["Local"]),
    ("Jelly", ["Local"]),
    ("Mysorepak", ["Local"]),
    ("Soanpapdi", ["Local"])
]

def generate_timings():
    opening = random.randint(7, 11)
    closing = random.randint(20, 23)
    return f"{opening}:00 - {closing}:00"

"""
# ----- Generate pan_shops.csv -----
shop_names = []
pan_shops_path = \
    (f'D:\Career-Related\Trainings\ETLHive-Training-Content\Python\Python-ETL-Workspace'
     '\pan_shops_in_india\pan_shops.csv')
with open(pan_shops_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Size', 'Timings', 'Owner', 'Rent', 'Location', 'City', 'State'])

    for _ in range(NUM_SHOPS):
        state = random.choice(STATES)
        city = random.choice(CITIES[state])
        name = f"{fake.first_name()}'s Pan Shop"
        size = random.randint(50, 150)
        timings = generate_timings()
        owner = fake.name()
        rent = random.randint(2500, 12000)
        location = fake.street_address()
        writer.writerow([name, size, timings, owner, rent, location, city, state])
        shop_names.append(name)

# ----- Generate pan_shop_sales.csv -----
pan_shop_sales_path = 'D:\Career-Related\Trainings\ETLHive-Training-Content\Python\Python-ETL-Workspace\pan_shops_in_india\pan_shop_sales.csv'
with open(pan_shop_sales_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
        'Name', 'Date', 'Time', 'Item', 'Item_Description',
        'Packed', 'Quantity', 'Sold', 'UnitPrice', 'Profit'
    ])

    for _ in range(SALES_ENTRIES):
        shop_name = random.choice(shop_names)
        sale_date = fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d')
        sale_time = fake.time(pattern='%H:%M:%S')
        item, descriptions = random.choice(PRODUCTS)
        description = random.choice(descriptions)
        packed = 'Yes' if item not in ['Sweets', 'Jelly', 'Mysorepak', 'Soanpapdi', 'Peanuts', 'Match Boxes'] else 'No'
        quantity = random.randint(5, 100)
        sold = random.randint(1, quantity)
        unit_price = round(random.uniform(2.0, 60.0), 2)
        profit = round(sold * unit_price * random.uniform(0.1, 0.4), 2)

        writer.writerow([
            shop_name, sale_date, sale_time, item, description,
            packed, quantity, sold, unit_price, profit
        ])
"""