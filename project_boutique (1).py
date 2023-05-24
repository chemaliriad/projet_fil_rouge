#project
#import glob                         # this module helps in selecting files 
import pandas as pd                 # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime
import requests
## Set Paths
#tmpfile    = "temp.tmp"               # file used to store all extracted data
#logfile    = "logfile.txt"            # all event logs will be stored in this file
#targetfile = "transformed_data.csv"   # file where transformed data is stored

### CSV Extract Function
# def extract_from_csv(file_to_process):
#     dataframe = pd.read_csv(file_to_process)
#     return dataframe

# import requests

# def get_overpass_data(query):
#     overpass_url = "https://overpass-api.de/api/interpreter"
#     response = requests.get(overpass_url, params={'data': query})
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# # Specify your Overpass query
# overpass_query = """
# [out:json];
# node(50.6360126,3.0761092,50.6360126,3.0761092); 
# out;
# """

# # Call the function to retrieve data from Overpass API
# data = get_overpass_data(overpass_query)

# if data:
#     # Process the data as per your requirement
#     print("Data retrieved successfully!")
# else:
#     print("Failed to retrieve data from the Overpass API.")

import pandas as pd
import xml.etree.ElementTree as ET

# Specify the path to your XML file
xml_file_path ="map_lille_flandre.xlm"

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Create empty lists to store the extracted data
node_ids = []
latitudes = []
longitudes = []
versions = []
timestamps = []
changesets = []
uids = []
users = []
tags_list = []

# Iterate over the nodes and extract information
for node in root.iter("node"):
    node_id = node.attrib["id"]
    lat = node.attrib["lat"]
    lon = node.attrib["lon"]
    version = node.attrib["version"]
    timestamp = node.attrib["timestamp"]
    changeset = node.attrib["changeset"]
    uid = node.attrib["uid"]
    user = node.attrib["user"]
    
    # Append the extracted data to the respective lists
    node_ids.append(node_id)
    latitudes.append(lat)
    longitudes.append(lon)
    versions.append(version)
    timestamps.append(timestamp)
    changesets.append(changeset)
    uids.append(uid)
    users.append(user)

    tags = []
    # Iterate over the tags within each node
    for tag in node.iter("tag"):
        k = tag.attrib["k"]
        v = tag.attrib["v"]
        
        # Append the tag to the tags list
        tags.append((k, v))
    
    # Append the tags list to the tags_list
    tags_list.append(tags)

# Create a DataFrame from the extracted data
data = {
    "Node ID": node_ids,
    "Latitude": latitudes,
    "Longitude": longitudes,
    "Version": versions,
    "Timestamp": timestamps,
    "Changeset": changesets,
    "UID": uids,
    "User": users,
    "Tags": tags_list
}

df = pd.DataFrame(data)

# Specify the output Excel file path
excel_file_path = "output.xlsx"

# Save the DataFrame to Excel
df.to_excel(excel_file_path, index=False)

print(f"Data saved to {excel_file_path} successfully.")



# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Create empty lists to store the extracted data
node_ids = []
latitudes = []
longitudes = []
timestamps = []
highways = []
amenities = []
building_types = []
landuses = []
railways = []
leisures = []
contact_postcodes = []
contact_streets = []
healthcares = []
names = []
opening_hours = []
contact_cities = []
addr_postcodes = []
addr_streets = []
brands = []
contact_phones = []
subways = []
public_transports = []
trains = []
buses = []
surveillance_types = []
shops = []
housenumbers = []

# Iterate over the nodes and extract information
for node in root.iter("node"):
    node_id = node.attrib["id"]
    lat = node.attrib["lat"]
    lon = node.attrib["lon"]
    timestamp = node.attrib["timestamp"]
    
    # Append the extracted data to the respective lists
    node_ids.append(node_id)
    latitudes.append(lat)
    longitudes.append(lon)
    timestamps.append(timestamp)
    
    # Initialize tag values as None
    highway = None
    amenity = None
    building_type = None
    landuse = None
    railway = None
    leisure = None
    contact_postcode = None
    contact_street = None
    healthcare = None
    name = None
    opening_hour = None
    contact_city = None
    addr_postcode = None
    addr_street = None
    brand = None
    contact_phone = None
    subway = None
    public_transport = None
    train = None
    bus = None
    surveillance_type = None
    shop = None
    housenumber = None

    # Iterate over the tags within each node
    for tag in node.iter("tag"):
        k = tag.attrib["k"]
        v = tag.attrib["v"]
        
        # Check the commonly used tags and assign their values to respective variables
        if k == "highway":
            highway = v
        elif k == "amenity":
            amenity = v
        elif k == "building":
            building_type = v
        elif k == "landuse":
            landuse = v
        elif k == "railway":
            railway = v
        elif k == "leisure":
            leisure = v
        elif k == "contact:postcode":
            contact_postcode = v
        elif k == "contact:street":
            contact_street = v
        elif k == "healthcare":
            healthcare = v
        elif k == "name":
            name = v
        elif k == "opening_hours":
            opening_hour = v
        elif k == "contact:city":
            contact_city = v
        elif k == "addr:postcode":
            addr_postcode = v
        elif k == "addr:street":
            addr_street = v
        elif k == "brand":
            brand = v
        elif k == "contact:phone":
            contact_phone = v
        elif k == "subway":
            subway = v
        elif k == "public_transport":
            public_transport = v
        elif k == "train":
            train = v
        elif k == "bus":
            bus = v
        elif k == "surveillance:type":
            surveillance_type = v
        elif k == "shop":
            shop = v
        elif k == ":housenumber":
            housenumber = v

    # Append the extracted tag values to the respective lists
    highways.append(highway)
    amenities.append(amenity)
    building_types.append(building_type)
    landuses.append(landuse)
    railways.append(railway)
    leisures.append(leisure)
    contact_postcodes.append(contact_postcode)
    contact_streets.append(contact_street)
    healthcares.append(healthcare)
    names.append(name)
    opening_hours.append(opening_hour)
    contact_cities.append(contact_city)
    addr_postcodes.append(addr_postcode)
    addr_streets.append(addr_street)
    brands.append(brand)
    contact_phones.append(contact_phone)
    subways.append(subway)
    public_transports.append(public_transport)
    trains.append(train)
    buses.append(bus)
    surveillance_types.append(surveillance_type)
    shops.append(shop)
    housenumbers.append(housenumber)

# Create a DataFrame from the extracted data
data = {
    "Node ID": node_ids,
    "Latitude": latitudes,
    "Longitude": longitudes,
    "Timestamp": timestamps,
    "Highway": highways,
    "Amenity": amenities,
    "Building Type": building_types,
    "Landuse": landuses,
    "Railway": railways,
    "Leisure": leisures,
    "Contact Postcode": contact_postcodes,
    "Contact Street": contact_streets,
    "Healthcare": healthcares,
    "Name": names,
    "Opening Hours": opening_hours,
    "Contact City": contact_cities,
    "Address Postcode": addr_postcodes,
    "Address Street": addr_streets,
    "Brand": brands,
    "Contact Phone": contact_phones,
    "Subway": subways,
    "Public Transport": public_transports,
    "Train": trains,
    "Bus": buses,
    "Surveillance Type": surveillance_types,
    "Shop": shops,
    "Housenumber": housenumbers
}

df = pd.DataFrame(data)

# Specify the output Excel file path
excel_file_path = "output.xlsx"

# Save the DataFrame to Excel
df.to_excel(excel_file_path, index=False)

print(f"Data saved to {excel_file_path} successfully.")


