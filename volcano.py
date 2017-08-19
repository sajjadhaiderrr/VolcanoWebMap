# Program: A WebMap showing the name and location of all the volcanos in the world colour coded by country populations
# Name: Sajjad Haider

import folium
import pandas


data = pandas.read_json("volcano.json")

# Initialize list of latitudes, longitudes, and volcano names
lat = list()
lon = list()
name = list()

# Parse through data to get latitudes, longituds, and volcano names
for volcano in range(len(data["features"])):
    lat.append(data["features"][volcano]['properties']['Latitude'])
    lon.append(data["features"][volcano]['properties']['Longitude'])
    name.append(data["features"][volcano]['properties']['V_Name'])

# Create initial map
map = folium.Map(location = [37,-95], zoom_start=5)

# Create feature group called population
fgp = folium.FeatureGroup(name = "Population")

# Color code each country by population
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig'),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


# Create feature group called volcanoes for the map
fgv = folium.FeatureGroup(name = "Volcanoes")

# Add markers for each volcano
for lt, ln, nm in zip(lat, lon, name):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(nm)))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map1.html")
