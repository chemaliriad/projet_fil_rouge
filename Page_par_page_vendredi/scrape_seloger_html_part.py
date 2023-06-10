import os
import re
import time

import time
import random
import json




from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox import options as firefox_options
import pandas as pd



def parse_pages():
    """Parse all pages from the data folder

    Returns:
        pd.DataFrame: parsed data
    """
    results = pd.DataFrame()
    pages_paths = os.listdir("data")
    for pages_path in pages_paths:
        with open(os.path.join("data", pages_path), "rb") as f_in:
            # page = f_in.read().decode("utf-8")
            page = f_in.read()
            df=pd.read_html(page) 
            print(df)
            # print(page)
           # results = results.concat(parse_page(page))
            var_script = parse_page(page)
            
             ###
            #dictionary = json.loads(var_script)
            # print(var_script)
           
            ###
            #dictionary = json.loads(var_script)
            # print(var_script)

             #results = results.append(parse_page(will_parse_page))
            # results = pd.concat([results, will_parse_page], axis=0)
            # print(results)
            # results = results.concat(parse_page(page))
               
    return results
        



def parse_page(page):
    """Parses data from a HTML page and return it as a dataframe

    The parsed data for each property advertisement is :
    - loyer (€) (rent)
    - type
    - surface (m²) (area)
    - nb_pieces (room number)
    - emplacement (location)
    - description

    Args:
        page (bytes): utf-8 encoded HTML page

    Returns:
        pd.DataFrame: Parsed data
    """
    soup = BeautifulSoup(page, "html.parser")
    result = pd.DataFrame()
    
    variable_name = "initListingClassifieds" 
    var_script_str = get_script_variable_value(page, variable_name)
    
       ###
    nom_fichier = "fichier.txt"

            # Ouvrir le fichier en mode écriture
    fichier = open(nom_fichier, "w", encoding="utf-8")

                # Écrire la variable dans le fichier
    fichier.write( var_script_str )

                # Fermer le fichier
    fichier.close()
                 
          
    
    # print (var_script_str)
    
    
    
    # json_data = json.loads(var_script_str)
    
    return var_script_str
    


        # Access the values in the JSON objec
    
    #result["loyer (€)"] = [clean_price(tag) for tag in soup.find_all(attrs={"class": "annonce-card-price"}) ]
    # result["loyer (€)"] = [tag              for tag in soup.find_all(attrs={"class": "annonce-card-price"}) ]
   
  

def get_script_variable_value(html_content, variable_name):
    soup = BeautifulSoup(html_content, "html.parser")
    script_tags = soup.find_all("script")

    # Find the script tag containing the variable
    for script_tag in script_tags:
        script_content = script_tag.string
        # json_data = json.loads(script_content)
        # script_content = clean_string(script_content)
        # print(script_content)
        
        if script_content and variable_name in script_content:
            # Extract the variable value using regex
            
        
            match = re.search(rf"{variable_name}\s*=\s*(.*?);", script_content)
            
            
            if match:
                #TODO valeur vide 
                variable_value = match.group(1)
               
                var_temp= clean_string(variable_value)
                
                return var_temp

    # If variable not found, return None or raise an exception
    return variable_name


def clean_string(string):
    cleaned_string = string.replace(";", "")
    return cleaned_string


    
    

# print(parse_pages())

    
    



   


def clean_price(tag):
    text = tag.text.strip()
    # price = int(text.replace("€", "Ä").replace(" ", "").replace("[" , "")   )
    price = text.replace("Ä", "€").replace(" ", "").replace("\n", "").replace("H.H.","").replace("H.I.","")
    return price

# print(parse_pages())

def main():
   
    
    results = parse_pages()
    # print(parse_pages())
    # print (results.head(100))
    # print(results)
    

if __name__ == "__main__":

    main()

