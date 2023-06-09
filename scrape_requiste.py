import os
import re
import time
import random
import requests

from bs4 import BeautifulSoup
import pandas as pd








def get_pages(count=1):
    """Fetch a specific count of result pages of property advertisements

    Args:
        count (int, optional): Number of result pages to fetch. Defaults to 1.

    Returns:
        list: pages HTML as utf-8 encoded bytes
    """

    pages = []

    for page_nb in range(1, count + 1):
        
        page_url = f"https://bureaux-commerces.seloger.com/search/trading?ci=590350&project=1&page={page_nb}"
        # page_url = f"https://www.cessionpme.com/index.php?action=affichage&annonce=offre&moteur=OUI&type_moteur=imo&nature_imo=L&nature_imo=L&rubrique_imo&region_imo=0&departement_imo=0&commune_imo=59650&trap_imo&secteur_activite_imo=location&ou_imo=Lille%20%2859000%29&surfmin&et&immo_tri=1&loc_avec_dab=OUI&loc_sans_dab=OUI&entre_dab&et_dab&motcle_imo&numero_imo&page={page_nb}"
        
        response = requests.get(page_url)
        page = response.content

        pages.append(page)

        # Sleep between requests (optional)
        time.sleep(20)

    return pages


def save_pages(pages):
    """Saves HTML pages into the "data" folder

    Args:
        pages (list): list of pages as bytes
    """
    os.makedirs("data", exist_ok=True)
    for page_nb, page in enumerate(pages):
        with open(f"data/page_{page_nb}.html", "wb") as f_out:
            f_out.write(page)


def parse_pages():
    """Parse all pages from the data folder

    Returns:
        pd.DataFrame: parsed data
    """
    results = pd.DataFrame()
    pages_paths = os.listdir("data")
    for pages_path in pages_paths:
        with open(os.path.join("data", pages_path), "rb") as f_in:
            page = f_in.read().decode("utf-8")
            parse_paged = parse_page(page)
            results = results.append(parse_paged)
    return results


# Rest of the code remains the same...


def main():
    pages = get_pages(count=6)
    save_pages(pages)
    # results = parse_pages()


if __name__ == "__main__":
    main()
