"""
Ce script vient scrapper l'ensemble du site :
https://bureaux-commerces.seloger.com/search/trading?ci=590350&project=1&page=1
Afin de récuperer les pages html
"""

"""
Cookie : 
datadome=7uneUyXZMoDxsJB-gvBmRvdUeoJonjl8yycjMDHD9_Y9SPUi9GDSJI8marMrPHAOKC1L8fth_pnvvkCaKEjqHLNl8XAfG9pDvq0vNpEvXumT7E~XiMfXjA00BFInTRH4; 
didomi_token=eyJ1c2VyX2lkIjoiMTg4OTA5OWMtMWI3ZC02YWRlLTk3YTUtM2M4ODVmYTVkN2FlIiwiY3JlYXRlZCI6IjIwMjMtMDYtMDZUMTI6MDY6MTguMTMxWiIsInVwZGF0ZWQiOiIyMDIzLTA2LTA2VDEyOjA2OjE4LjEzMVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsaW5rZWRpbi1tYXJrZXRpbmctc29sdXRpb25zIiwiYzpvbW5pdHVyZS1hZG9iZS1hbmFseXRpY3MiLCJjOmhhcnZlc3QtUFZUVHRVUDgiLCJjOmhvdGphci1MWWdod25VSiJdfSwicHVycG9zZXMi…Wt1QUVBRmtCSllBLkFrdUFFQUZrQkpZQSJ9;
euconsent-v2=CPs8KYAPs8KYAAHABBENDHCsAP_AAH_AAAAAJeNf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tqoKuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_87wS7AJMNW4gC7EscCbaMIoUQIwrCQqgUAFFAMLRAYQOrgp2VwE-sIkAKAUARgRAhwBRkwCAAACAJCIAJAjwQCAACAQAAgAVCIQAEbAIKACwEAgAFAdCxRigCECQgyIiIhTAgIkSCgnsqEEoP9DTCEOssAKDR_xUICJQAxWBEJCwchwRICXiyQLMUb5ACMAKAUSoVqCT00ACxkbAAA.f_gAD_gAAAAA
"""
import logging
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_html(url):
    driver = webdriver.Firefox()
    driver.get('https://bureaux-commerces.seloger.com/search/trading?ci=590350&project=1&page=1')
    driver.add_cookie({'name': 'datadome', 'value': '7uneUyXZMoDxsJB-gvBmRvdUeoJonjl8yycjMDHD9_Y9SPUi9GDSJI8marMrPHAOKC1L8fth_pnvvkCaKEjqHLNl8XAfG9pDvq0vNpEvXumT7E~XiMfXjA00BFInTRH4'})
    driver.add_cookie({'name': 'didomi_token', 'value':'eyJ1c2VyX2lkIjoiMTg4OTA5OWMtMWI3ZC02YWRlLTk3YTUtM2M4ODVmYTVkN2FlIiwiY3JlYXRlZCI6IjIwMjMtMDYtMDZUMTI6MDY6MTguMTMxWiIsInVwZGF0ZWQiOiIyMDIzLTA2LTA2VDEyOjA2OjE4LjEzMVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsaW5rZWRpbi1tYXJrZXRpbmctc29sdXRpb25zIiwiYzpvbW5pdHVyZS1hZG9iZS1hbmFseXRpY3MiLCJjOmhhcnZlc3QtUFZUVHRVUDgiLCJjOmhvdGphci1MWWdod25VSiJdfSwicHVycG9zZXMi…Wt1QUVBRmtCSllBLkFrdUFFQUZrQkpZQSJ9'})
    driver.add_cookie({'name':'euconsent-v2','value':'CPs8KYAPs8KYAAHABBENDHCsAP_AAH_AAAAAJeNf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tqoKuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_87wS7AJMNW4gC7EscCbaMIoUQIwrCQqgUAFFAMLRAYQOrgp2VwE-sIkAKAUARgRAhwBRkwCAAACAJCIAJAjwQCAACAQAAgAVCIQAEbAIKACwEAgAFAdCxRigCECQgyIiIhTAgIkSCgnsqEEoP9DTCEOssAKDR_xUICJQAxWBEJCwchwRICXiyQLMUb5ACMAKAUSoVqCT00ACxkbAAA.f_gAD_gAAAAA'
})
    driver.get('https://bureaux-commerces.seloger.com/search/trading?ci=590350&project=1&page=1')
    html = driver.page_source
    write_html(html)
    driver.quit()
    
def write_html(html):
    logging.info('Writing html')
    with open('html.html', 'w') as file:
        file.write(html)


if __name__ == "__main__":
    logging.info('Starting scrapping')
    get_html('https://bureaux-commerces.seloger.com/search/trading?ci=590350&project=1&page=1')
    