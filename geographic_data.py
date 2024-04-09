import time
import pandas as pd
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import collections
collections.Callable = collections.abc.Callable


def get_geographic_data(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)
    time.sleep(3)

    html_source = driver.page_source

    soup = BeautifulSoup(html_source, 'html.parser')

    data = soup.find_all("td", {"class": "text"})

    t_data = []

    for table in data:
        f_data = table.find('table')
        if f_data:
            td_tags = soup.find_all('td')
            for td_tag in td_tags:
                if not td_tag.text.strip():
                    td_tag.decompose()
            span_tags = f_data.find_all('span')
            for span_tag in span_tags:
                if 'United States' in span_tag.text or 'Americas' in span_tag.text:
                    list_data = parser_functions.make2d(f_data)
                    for item in list_data:
                        item = list(filter(None, item))
                        t_data.append(item)

    df = pd.DataFrame(t_data)
    print(df)

    driver.quit()
