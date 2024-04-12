from revise import revise_table
import time
import pandas as pd
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tabulate import tabulate
import collections
collections.Callable = collections.abc.Callable


def scrapping(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    get_geographic_data(url, driver)
    driver.quit()


def get_geographic_data(url, driver):

    driver.get(url)
    time.sleep(3)

    html_source = driver.page_source

    soup = BeautifulSoup(html_source, 'html.parser')

    data = soup.find_all("td", {"class": "text"})

    t_data = []

    for table in data:
        f_data = table.find('table')
        if f_data:
            span_tags = f_data.find_all('span')
            for span_tag in span_tags:
                if 'United States' in span_tag.text or 'Americas' in span_tag.text:
                    revise_table(f_data)
