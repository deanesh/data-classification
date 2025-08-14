# Required Libraries and Commands for Maps in Python
#    pip install geopandas folium geopy

import pandas as pd
# Code for Map - Step - Geocode the Cities
from geopy.geocoders import Nominatim
import time
# Step : Plot with Folium (Interactive Map)
import folium

# Data Ingestion
pan_shops_path = r"D:\Career-Related\Trainings\ETLHive-Training-Content\Python\Python-ETL-Workspace\pan_shops_in_india\pan_shops.csv"
pan_shop_sales_path = r"D:\Career-Related\Trainings\ETLHive-Training-Content\Python\Python-ETL-Workspace\pan_shops_in_india\pan_shop_sales.csv"
pan_shops_df = pd.read_csv(pan_shops_path, na_values=["", "NA"], keep_default_na=False)
pan_shop_sales_df = pd.read_csv(pan_shop_sales_path, na_values=["", "NA"], keep_default_na=False)
pan_shops_df.name = "pan_shops"; pan_shop_sales_df.name="pan_shop_sales"
shops_df = pan_shops_df; sales_df = pan_shop_sales_df
shop_sales_details = shops_df.merge(sales_df, on ="Name", how="left")

# Get Top and Bottom Cities based on Profit per State
state_city_profits = (
    shop_sales_details.groupby(by=["State", "City"], group_keys=False)
    .agg({"Profit":"sum"}).reset_index()
)

top_state_city_with_profit = (
    state_city_profits.sort_values(by=["State", "Profit"], ascending=[True, False])
    .groupby("State", group_keys=False).head(1).reset_index(drop=True)
)

bottom_state_city_with_profit = (
    state_city_profits.sort_values(by=["State", "Profit"], ascending=[True, True])
    .groupby("State", group_keys=False).head(1).reset_index(drop=True)
)

merged_df = (pd.concat([top_state_city_with_profit, bottom_state_city_with_profit])
             .sort_values(by=["State"], ascending=[True]).reset_index(drop=True))


# Let's say this is your merged DataFrame
merged_df = (pd.concat([top_state_city_with_profit, bottom_state_city_with_profit])
             .sort_values(by=["State"], ascending=[True]).reset_index(drop=True))

# Add a full address column for geocoding
merged_df["Location"] = merged_df["City"] + ", " + merged_df["State"]

# Geocode using Nominatim
geolocator = Nominatim(user_agent="intl_brand_locator")


def geocode_location(location):
    try:
        time.sleep(1)  # to prevent overloading the service
        loc = geolocator.geocode(location)
        if loc:
            return pd.Series([loc.latitude, loc.longitude])
        else:
            return pd.Series([None, None])
    except:
        return pd.Series([None, None])


merged_df[["Latitude", "Longitude"]] = merged_df["Location"].apply(geocode_location)


# Center of the map
map_center = [merged_df["Latitude"].mean(), merged_df["Longitude"].mean()]
m = folium.Map(location=map_center, zoom_start=5)


# Define color based on Highest/Lowest
def get_color(value):
    return 'green'


# Add points
for _, row in merged_df.iterrows():
    if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=6,
            popup=f"{row['City']}, {row['State']}<br>{row['Profit']}",
            color=get_color(row['Profit']),
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

m.save("top_bottom_profit_cities_per_state.html")