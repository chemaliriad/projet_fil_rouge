# from bs4 import BeautifulSoup



# file_html = "C:/Users/Administrateur/Projet_fil_rouge/Page_par_page_vendredi/htmlp2_1.html"

# # Ouvrir le fichier HTML en mode lecture
# with open(file_html, "r") as file:
#     # Lire le contenu du fichier
#     content = file.read()


# # Utiliser BeautifulSoup pour analyser le HTML
# soup = BeautifulSoup(content, 'html.parser')

# # Trouver l'élément avec l'ID "page-data-layer"
# element = soup.find(id='page-data-layer')

# # Extraire le contenu JSON de l'élément
# json_data = element.string

# # Afficher le contenu JSON
# print(json_data)


import json
import pandas as pd
from bs4 import BeautifulSoup
df = pd.DataFrame()
dff = pd.DataFrame()
for j in range (3,4): 
    for i in range (1,25) :
    

        file_html = f"C:/Users/Administrateur/Projet_fil_rouge/Page_par_page_vendredi/htmlp{j}_{i}.html"

        # Ouvrir le fichier HTML en mode lecture
        with open(file_html, "r") as file:
            # Lire le contenu du fichier
            content = file.read()

        # Utiliser BeautifulSoup pour analyser le HTML
        soup = BeautifulSoup(content, 'html.parser')

        # Trouver l'élément avec l'ID "page-data-layer"
        element = soup.find(id='page-data-layer')

        # Extraire le contenu JSON de l'élément
        json_data = element.get_text()

        # Charger le contenu JSON dans un dictionnaire Python
        data_dict = json.loads(json_data)
        
        print(data_dict )
        # Extraire les valeurs spécifiques
        id_annonce = data_dict['idAnnonce']
        id_type_transaction = data_dict['idTypeTransaction']
        type_boutique = data_dict ["stickyBar"]["imgAlt"]
        space = data_dict ["stickyBar"] ['title']
        latitude = data_dict['map']['coordinates']['latitude']
        longitude = data_dict['map']['coordinates']['longitude']
        price = data_dict["stickyBar"]['montant']['label']
        suffix = data_dict["stickyBar"]['montant']['suffix']

        # Créer un DataFrame à partir des valeurs extraites
        data = {
            'idAnnonce': [id_annonce],
            'idTypeTransaction': [id_type_transaction],
            "[type_boutique] "     :  [type_boutique] ,
            'space': [space],
            'latitude': [latitude],
            'longitude': [longitude],
            'monthlyPrice': [price],
            'mois ou année ': [suffix]
        }
        df = pd.DataFrame(data)
        dff = pd.concat([dff, df], axis=0)
        # Enregistrer le DataFrame dans un fichier Excel
        dff.to_excel("C:/Users/Administrateur/Projet_fil_rouge/Page_par_page_vendredi/output.xlsx", index=False)
