"""
Parsing html file for get data in js script
"""

import logging
import re
from bs4 import BeautifulSoup
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



# Logging default config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def open_html(path_html_page) -> str:
    logging.info("Ouverture du fichier html")
    with open(path_html_page, "r") as file:
        html = file.read()
        logging.info("Affichage du code html")
        logging.info("DÃ©but du parsing du fichier html")
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')
        logging.info("Affichage des scripts")
        logging.info("DÃ©finition du pattern de recherche")
        pattern = re.compile(r"var\s+initListingCriteria\s+=\s+({.*?});", re.MULTILINE | re.DOTALL)
        logging.info("Recherche du pattern dans les scripts")
        for script in scripts:
            if script.string:
                if pattern.search(script.text):
                    logging.info("Pattern trouvÃ©")
                    return script.text
        
def parse_str(script:str)-> str:
    logging.info("Extracting json data from script")
    logging.info("DÃ©finition du pattern de recherche")
    try:
        start_index = script.index('{"total":127')
        logging.info("Pattern trouvÃ©")
        part = script[start_index:]
        return part
    except ValueError:
        part = None


if __name__ == "__main__":
    logging.info("DÃ©but du parsing du fichier html")
    

    
    
    for i in range(1,7):
        path_html_page=f"./data/html{i}.html"
        fin_scr = open_html( path_html_page)
        fin_data = parse_str(fin_scr)
     # print(fin_data)
    
     # json_data_dumps = json.dumps(fin_data)
     # json_data_load = json.load(json_data_dumps)
    
        # print(json_data_load)
        logging.info("Ecriture des donnÃ©es dans le fichier data.txt")
        with(open(f"data{i}.json", "w")) as file:
             file.write(fin_data)
    
