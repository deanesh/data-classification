# visualize_top_bottom_sales.py

import pandas as pd
from map_generator import MapGenerator
import webbrowser

# ------------------------------
# Load and Merge Shop + Sales Data
# ------------------------------
path = r"D:\Career-Related\Trainings\ETLHive-Training-Content\Python\Python-ETL-Workspace\pan_shops_in_india"
shops_path = path+r"/pan_shops.csv"
sales_path = path+r"/pan_shop_sales.csv"

shops_df = pd.read_csv(shops_path, na_values=["", "NA"], keep_default_na=False)
sales_df = pd.read_csv(sales_path, na_values=["", "NA"], keep_default_na=False)

shop_sales_details = shops_df.merge(sales_df, on="Name", how="left")

# ------------------------------
# Compute Top and Bottom Cities by Sales per State
# ------------------------------
city_sales = (
    shop_sales_details.groupby(by=["State", "City"], group_keys=False)
                      .agg( Sales=("Sold", "sum") )
                      .reset_index()
)

top_sales_city_per_day = (
    city_sales.sort_values(by=["State", "Sales"], ascending=[True, False])
    .groupby("State", group_keys=False)
    .head(1)
    .reset_index(drop=True)
)
top_sales_city_per_day["Sales_Category"] = "Highest"

bottom_sales_city_per_day = (
    city_sales.sort_values(by=["State", "Sales"], ascending=[True, True])
                    .groupby("State", group_keys=False)
                    .head(1)
                    .reset_index(drop=True)
)
bottom_sales_city_per_day["Sales_Category"] = "Lowest"

# Combined (Top/Bottom 3 sold items per day)
merged_df = pd.concat([top_sales_city_per_day, bottom_sales_city_per_day])\
                                            .sort_values(by=["State", "Sales"], ascending=[True, False])

# merged_df = pd.concat([top_profit, bottom_profit]).reset_index(drop=True)

# ------------------------------
# Geocode & Map Plotting
# ------------------------------
mapper = MapGenerator()
geocoded_df = mapper.geocode_dataframe(merged_df)

# Optional: create a nice popup string
geocoded_df["Popup_Info"] = geocoded_df["City"] + ", " + geocoded_df["State"] + "<br>Sales: ₹" + geocoded_df["Sales"].round(2).astype(str)
map_path = "top_bottom_sales_cities.html"
# Plot
mapper.plot_map(
    geocoded_df,
    popup_col="Popup_Info",
    color_col="Sales_Category",
    color_mapping={"Highest": "green", "Lowest": "red"},
    map_file=map_path
)

print(merged_df)

# open map after creation
webbrowser.open(map_path)
