import json

import os
import re
import time

import time
import random
import json
from pandas import json_normalize



from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox import options as firefox_options
import pandas as pd

for i in range(1,7):

    # Specify the path to the JSON file
    file_path = "C:/Users/Administrateur/Projet_fil_rouge/data{i}.json"

    # Open the JSON file and load its contents into a Python dictionary
    with open(file_path, "r") as json_file:

    # ##
    # Ouvrir le fichier en mode lectur
        # Lire le contenu du fichier
        content = json_file.read()

    # Vérifier si le dernier caractère est ";"
    content = content.replace(';', '').rstrip()
    # Ouvrir le fichier en mode écriture
    with open(f'C:/Users/Administrateur/Projet_fil_rouge/data{i}.json', 'w') as json_file:
        # Écrire le contenu modifié dans le fichier
        print(content)
        
        json_file.write(content)
        
    json_file.close()
    ###    
    json_data = json.load(json_file)
    # Print the dictionary
    # print(json_data)

    df2 = json_normalize(json_data['classifieds']) 
    # df = pd.DataFrame([json_data])
    # df1 = df[["classifieds"]]
    print (df2)
    df2.to_excel(f'df{i}.xlsx', index=False)

