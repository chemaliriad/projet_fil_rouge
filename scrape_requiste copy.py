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

    user_agents = [
        "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.81 Mobile Safari/537.36"
    ]

    pages = []

    for page_nb in range(1, count + 1):
        page_url = f"https://www.leboncoin.fr/recherche?category=13&text=local&locations=Lille_59000__50.6282_3.06881_5000&page={page_nb}"
        
        # page_url = f"https://bureaux-commerces.seloger.com/search/trading?ci=590350&project=1&page={page_nb}"
        # page_url = f"https://www.cessionpme.com/index.php?action=affichage&annonce=offre&moteur=OUI&type_moteur=imo&nature_imo=L&nature_imo=L&rubrique_imo&region_imo=0&departement_imo=0&commune_imo=59650&trap_imo&secteur_activite_imo=location&ou_imo=Lille%20%2859000%29&surfmin&et&immo_tri=1&loc_avec_dab=OUI&loc_sans_dab=OUI&entre_dab&et_dab&motcle_imo&numero_imo&page={page_nb}"
        
        headers = {
            "User-Agent": random.choice(user_agents)
        }

        response = requests.get(page_url, headers=headers)
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
    pages = get_pages(count=2)
    save_pages(pages)
    # results = parse_pages()


if __name__ == "__main__":
    main()
