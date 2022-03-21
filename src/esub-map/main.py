import pandas as pd
import folium as fl

class point:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.args = {"name": self.name, "coordinate": {"latitude": self.latitude, "longitude": self.longitude}}

