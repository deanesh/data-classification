# map_generator.py

import time
import pandas as pd
import folium
from geopy.geocoders import Nominatim


class MapGenerator:
    def __init__(self, user_agent: str = "geo_mapper"):
        """
        Initialize the MapGenerator with a geopy Nominatim geocoder.
        """
        self.geolocator = Nominatim(user_agent=user_agent)

    def geocode_dataframe(self, df: pd.DataFrame, city_col: str = "City", state_col: str = "State") -> pd.DataFrame:
        """
        Geocode the City and State columns to add Latitude and Longitude.
        """
        def geocode_location(location):
            try:
                time.sleep(1)  # rate limit to prevent being blocked
                loc = self.geolocator.geocode(location)
                if loc:
                    return pd.Series([loc.latitude, loc.longitude])
                else:
                    return pd.Series([None, None])
            except:
                return pd.Series([None, None])

        df = df.copy()
        df["Location"] = df[city_col] + ", " + df[state_col]
        df[["Latitude", "Longitude"]] = df["Location"].apply(geocode_location)
        return df

    def plot_map(
        self,
        df: pd.DataFrame,
        lat_col: str = "Latitude",
        lon_col: str = "Longitude",
        popup_col: str = None,
        color_col: str = None,
        color_mapping: dict = None,
        map_file: str = "output_map.html",
        zoom_start: int = 5,
        default_color: str = "blue"
    ) -> folium.Map:
        """
        Create and save an interactive map from a DataFrame.

        Parameters:
        - popup_col: Column to show in the popup.
        - color_col: Column based on which marker colors are decided.
        - color_mapping: Dict mapping values in color_col to colors (e.g. {"Highest": "green", "Lowest": "red"}).
        - default_color: Default color if color_col is not used or not in mapping.
        """
        df = df.copy()
        m = folium.Map(location=[df[lat_col].mean(), df[lon_col].mean()], zoom_start=zoom_start)

        for _, row in df.iterrows():
            lat, lon = row[lat_col], row[lon_col]
            if pd.notna(lat) and pd.notna(lon):
                popup = str(row[popup_col]) if popup_col else None
                color = default_color
                if color_col and color_mapping:
                    color = color_mapping.get(row[color_col], default_color)

                folium.CircleMarker(
                    location=[lat, lon],
                    radius=6,
                    popup=popup,
                    color=color,
                    fill=True,
                    fill_opacity=0.7
                ).add_to(m)

        m.save(map_file)
        return m
