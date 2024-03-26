# Load the pyproj library
import pyproj

# Define the projection parameters for Web Mercator
web_mercator = pyproj.Proj('EPSG:3857')

# Define the input coordinates in degrees
lat = 42.09325 # degrees
lon = -87.96189 # degrees

# Convert the input coordinates to Web Mercator (EPSG:3857)
x, y = pyproj.transform(pyproj.Proj('EPSG:4326'), web_mercator, lon, lat)

# Convert the Web Mercator coordinates to Artillery X, Y
artillery_x = x #/ 10 # divide by 10 to convert from meters to decimeters
artillery_y = -y #/ 10 # negate the Y coordinate and divide by 10

print(f"Coord X: {artillery_x}, Coord Y: {artillery_y}")
