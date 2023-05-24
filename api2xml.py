

# import requests



# # Specify the area of interest and desired file path
# minlat="50.6185600" 
# minlon="3.1409300" 
# maxlat="50.6200200" 
# maxlon="3.1451400"
# bbox = "<minlon>,<minlat>,<maxlon>,<maxlat>"

 
 
# output_file = "output.xml"

# # Define the OpenStreetMap API URL
# api_url = f"https://api.openstreetmap.org/api/0.6/map?bbox={bbox}"

# # Send a GET request to the OpenStreetMap API
# response = requests.get(api_url)

# if response.status_code == 200:
#     # Save the XML data to a file
#     with open(output_file, "w") as file:
#         file.write(response.text)
    
#     print(f"XML data saved to {output_file} successfully.")
# else:
#     print("Failed to retrieve XML data from the OpenStreetMap API.")
import requests

# Specify the area of interest and desired file path
minlat=50.6185600 
minlon=3.1409300
maxlat=50.6200200
maxlon=3.1451400
#bbox = "<minlon>,<minlat>,<maxlon>,<maxlat>"
     #  "50.6360300,3.0685300,50.6374900,3.0727400"
bbox = "3.1409300,50.6185600,3.1451400,50.6200200"
output_file = "villeneuve.xml"

# Define the OpenStreetMap API URL
api_url = f"https://api.openstreetmap.org/api/0.6/map?bbox={bbox}"

# Send a GET request to the OpenStreetMap API
response = requests.get(api_url)

if response.status_code == 200:
    # Save the XML data to a file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(response.text)
    
    print(f"XML data saved to {output_file} successfully.")
else:
    print("Failed to retrieve XML data from the OpenStreetMap API.")
