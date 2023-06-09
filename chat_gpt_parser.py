import os
import re
import time
import random
import json
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox import options as firefox_options


def parse_pages():
    results = pd.DataFrame()
    pages_paths = os.listdir("data")
    for pages_path in pages_paths:
        with open(os.path.join("data", pages_path), "rb") as f_in:
            page = f_in.read()
            var_script = parse_page(page)
            print(var_script)
            # results = results.append(parse_page(page))
    return results


def parse_page(page):
    soup = BeautifulSoup(page, "html.parser")
    result = pd.DataFrame()
    variable_name = "initListingClassifieds"
    var_script_str = get_script_variable_value(page, variable_name)
    print(var_script_str)
    json_data = json.loads(var_script_str)
    return var_script_str


# def get_script_variable_value(html_content, variable_name):
#     soup = BeautifulSoup(html_content, "html.parser")
#     script_tags = soup.find_all("script")
#     for script_tag in script_tags:
#         script_content = script_tag.string
#         if script_content and variable_name in script_content:
#             match = re.search(rf"{variable_name}\s*=\s*(.*?);", script_content)
#             if match:
#                 variable_value = match.group(1)
#                 return variable_value
#     return variable_name


def get_script_variable_value(html_content, variable_name):
    soup = BeautifulSoup(html_content, "html.parser")
    script_tags = soup.find_all("script")
    for script_tag in script_tags:
        script_content = script_tag.string
        if script_content and variable_name in script_content:
            match = re.search(rf"{variable_name}\s*=\s*(.*?);", script_content)
            if match:
                variable_value = match.group(1)
                return variable_value
    return variable_name



def main():
    results = parse_pages()
    print(results)


if __name__ == "__main__":
    main()
