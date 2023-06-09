import json
from pandas import json_normalize

# Specify the path to the JSON file
file_path = "C:/Users/Administrateur/Projet_fil_rouge/data1.json"

# Open the JSON file and load its contents into a Python dictionary
with open(file_path, "r") as json_file:
    # Read the content of the file
    content = json_file.read()

    # Vérifier si le dernier caractère est ";"
    content = content.replace(';', '').rstrip()

# Open the file in write mode
with open('C:/Users/Administrateur/Projet_fil_rouge/data1.json', 'w') as json_file:
    # Write the modified content back to the file
    json_file.write(content)

# Load the JSON data after modifying the file
json_data = json.loads(content)

# Convert the JSON data to a DataFrame
df2 = json_normalize(json_data['classifieds'])

# Save the DataFrame to an Excel file
df2.to_excel('df2.xlsx', index=False)
