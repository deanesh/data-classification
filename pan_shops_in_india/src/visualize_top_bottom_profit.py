# visualize_top_bottom_profit.py

import pandas as pd
from map_generator import MapGenerator
import webbrowser

# ------------------------------
# Load and Merge Shop + Sales Data
# ------------------------------
path = r"D:\Career-Related\Trainings\ETLHive-Training-Content\Python\Python-ETL-Workspace\pan_shops_in_india\data"
shops_path = path+r"/pan_shops.csv"
sales_path = path+r"/pan_shop_sales.csv"

shops_df = pd.read_csv(shops_path, na_values=["", "NA"], keep_default_na=False)
sales_df = pd.read_csv(sales_path, na_values=["", "NA"], keep_default_na=False)

shop_sales_details = shops_df.merge(sales_df, on="Name", how="left")

# ------------------------------
# Compute Top and Bottom Cities by Profit per State
# ------------------------------
state_city_profit = (
    shop_sales_details.groupby(["State", "City"], as_index=False)
    .agg({"Profit": "sum"})
)

top_profit = (
    state_city_profit.sort_values(["State", "Profit"], ascending=[True, False])
    .groupby("State", group_keys=False).head(1)
)
top_profit["Profit_Category"] = "Highest"

bottom_profit = (
    state_city_profit.sort_values(["State", "Profit"], ascending=[True, True])
    .groupby("State", group_keys=False).head(1)
)
bottom_profit["Profit_Category"] = "Lowest"

merged_df = pd.concat([top_profit, bottom_profit]).reset_index(drop=True)

# ------------------------------
# Geocode & Map Plotting
# ------------------------------
mapper = MapGenerator()
geocoded_df = mapper.geocode_dataframe(merged_df)

# Optional: create a nice popup string
geocoded_df["Popup_Info"] = geocoded_df["City"] + ", " + geocoded_df["State"] + "<br>Profit: ₹" + geocoded_df["Profit"].round(2).astype(str)
map_path = "top_bottom_profit_cities.html"
# Plot
mapper.plot_map(
    geocoded_df,
    popup_col="Popup_Info",
    color_col="Profit_Category",
    color_mapping={"Highest": "green", "Lowest": "red"},
    map_file=map_path
)

print(merged_df)

# open map after creation
webbrowser.open(map_path)
