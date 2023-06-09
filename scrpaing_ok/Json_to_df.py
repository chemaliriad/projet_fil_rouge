import json
import pandas as pd
from pandas import json_normalize

df3=pd.DataFrame() 

for i in range(1, 7):
    # Specify the path to the JSON file
    file_path = f"C:/Users/Administrateur/Projet_fil_rouge/data{i}.json"

    # Open the JSON file and load its contents into a Python dictionary
    with open(file_path, "r") as json_file:
        # Lire le contenu du fichier
        content = json_file.read()

    # Vérifier si le dernier caractère est ";"
    content = content.replace(';', '').rstrip()

    # Ouvrir le fichier en mode écriture
    with open(f'C:/Users/Administrateur/Projet_fil_rouge/data{i}.json', 'w') as json_file:
        # Écrire le contenu modifié dans le fichier
        print(content)
        json_file.write(content)

    # Fermer le fichier après avoir écrit les modifications
    json_file.close()

    # Charger le contenu JSON dans un dictionnaire
    json_data = json.loads(content)

    # Convertir le dictionnaire en DataFrame
    df2 = json_normalize(json_data['classifieds'])
    print(df2)
    df2.to_excel(f'df{i}.xlsx', index=False)
    df3 = pd.concat([df3, df2], axis=0)
    
df3.to_excel('df_final.xlsx', index=False)

