import pandas as pd
import numpy as np
from faker import Faker

# Use Indian locale for names
fake = Faker('en_IN')
np.random.seed(42)

years = list(range(2013, 2026))
categories = ["General", "Reserved"]
sexes = ["M", "F"]
states = [
    "Uttar Pradesh", "Maharashtra", "Bihar", "West Bengal", "Madhya Pradesh",
    "Tamil Nadu", "Rajasthan", "Karnataka", "Gujarat", "Andhra Pradesh"
]

all_data = []

for year in years:
    num_students = 2000

    data_year = pd.DataFrame({
        "Year": year,
        "Exam_Date": pd.to_datetime(f"{year}-04-15") + pd.to_timedelta(np.random.randint(0, 7, size=num_students), unit='d'),
        "Name": [fake.name() for _ in range(num_students)],
        "Category": np.random.choice(categories, size=num_students, p=[0.7, 0.3]),
        "Sex": np.random.choice(sexes, size=num_students),
        "State": np.random.choice(states, size=num_students),
        "Maths_Marks": np.random.randint(40, 101, size=num_students),
        "Physics_Marks": np.random.randint(35, 101, size=num_students),
        "Chemistry_Marks": np.random.randint(30, 101, size=num_students),
    })

    data_year["Total_Marks"] = data_year["Maths_Marks"] + data_year["Physics_Marks"] + data_year["Chemistry_Marks"]

    data_year["Rank"] = data_year.groupby("Category")["Total_Marks"] \
                         .rank(ascending=False, method='dense').astype(int)

    counts = data_year.groupby("Category")["Rank"].transform('max')
    data_year["Percentile"] = 100 * (1 - (data_year["Rank"] - 1) / counts)

    all_data.append(data_year)

df = pd.concat(all_data).reset_index(drop=True)

top_30 = df[df["Rank"] <= 30].sort_values(["Year", "Category", "Rank"]).reset_index(drop=True)

# Save to CSV
# df.to_csv("D:\Career-Related\Trainings\ETLHive-Training-Content\Python\Python-ETL-Workspace\jee-mains\jee-mains-(2013-2025)-top-30.csv", index=False)