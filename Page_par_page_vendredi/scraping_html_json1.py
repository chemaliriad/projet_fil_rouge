import logging
import re
from bs4 import BeautifulSoup


# Logging default config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def open_html(path_html_page):
    logging.info("Ouverture du fichier html")
    with open(path_html_page, "r") as file:
        html = file.read()
        logging.info("Affichage du code html")
        logging.info("Début du parsing du fichier html")
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')
        logging.info("Affichage des scripts")
        logging.info("Définition du pattern de recherche")
        pattern = re.compile(r"var\s+initListingCriteria\s+=\s+({.*?});", re.MULTILINE | re.DOTALL)
        logging.info("Recherche du pattern dans les scripts")
        for script in scripts:
            if script.string:
                if pattern.search(script.text):
                    logging.info("Pattern trouvé")
                    return script.text


def parse_str(script):
    logging.info("Extracting json data from script")
    logging.info("Définition du pattern de recherche")
    try:
        start_index = script.index('{"total"')
        logging.info("Pattern trouvé")
        part = script[start_index:]
        return part
    except ValueError:
        part = None


if __name__ == "__main__":
    logging.info("Début du parsing du fichier html")
    
    for i in range(1, 7):
        path_html_page = f"C:/Users/Administrateur/Projet_fil_rouge/scrpaing_ok/data/html{i}.html"
        fin_scr = open_html(path_html_page)
        fin_data = parse_str(fin_scr)
    
        logging.info("Ecriture des données dans le fichier data.json")
        with open(f"C:/Users/Administrateur/Projet_fil_rouge/scrpaing_ok/data{i}.json", "w") as file:
            file.write(fin_data)
