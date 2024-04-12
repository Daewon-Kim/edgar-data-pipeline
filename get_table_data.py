import requests
import pandas as pd
import xml.etree.ElementTree as ET
from tabulate import tabulate
from geographic_data import scrapping

# 입력할 것은 찾고 싶은 단어의 리스트, ticker의 리스트
# 반환은 회사 - 이름 - url

# 총 매출, 지역별 매출, 품목별 매출
# 각각을 특정하는 키워드들을 찾는 것이 목표.

# msft, aapl, nvda, amzn, nflx

headers = {
    "User-Agent": "Mozilla"
}

_GEOKEYWORD = ['segment', 'information', 'tables']


def find_cik(ticker):
    ticker_list = []
    for item in ticker:
        ticker_list.append(item.upper().replace(".", "-"))

    ticker_json = requests.get(
        "https://www.sec.gov/files/company_tickers.json", headers=headers).json()

    cik_list = []

    for item in ticker_list:
        for company in ticker_json.values():
            if company['ticker'] == item:
                cik_list.append(str(company['cik_str']).zfill(10))

    return cik_list


def get_company_recent_filings_df_list(list):
    result = []
    for item in list:
        url = (f'https://data.sec.gov/submissions/CIK{item}.json')
        data = requests.get(url, headers=headers).json()
        result.append(pd.DataFrame(data['filings']['recent']))
    return result


def filtering(list):
    result = []
    for item in list:
        result.append(item[(item['form'] == '10-K')
                      | (item['form'] == '10-Q')])
    return result


def get_latest_num(list):
    result = []
    for item in list:
        result.append(item['accessionNumber'].iloc[0])
    return result


def get_filing_summary(num_list, cik_list):
    result = []
    base_url = "https://www.sec.gov/Archives/edgar/data"

    for i in range(len(cik_list)):
        ac_num = num_list[i].replace('-', '')
        url = f"{base_url}/{cik_list[i]}/{ac_num}/FilingSummary.xml"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            xml_data = response.content
            tree = ET.ElementTree(ET.fromstring(xml_data))

            name_list = [cik_list[i]]

            for report in tree.findall('.//Report'):
                html_file_name = report.find('HtmlFileName').text if report.find(
                    'HtmlFileName') is not None else 'N/A'
                long_name = report.find('LongName').text if report.find(
                    'LongName') is not None else 'N/A'
                short_name = report.find('ShortName').text if report.find(
                    'ShortName') is not None else 'N/A'
                name_list.append(
                    [short_name, f'{base_url}/{cik_list[i]}/{ac_num}/{html_file_name}'])
            result.append(name_list)

        else:
            print('error')

    return result


def finding(data_list, search_list):
    for name_list in data_list:
        print('')
        print(name_list[0])
        for data in name_list:
            if all(item in data[0].lower() for item in search_list):
                scrapping(data[1])


def get_data(ticker, search_words):
    cik_list = find_cik(ticker)

    company_recent_filings_df_list = get_company_recent_filings_df_list(
        cik_list)

    company_recent_filings_df_list = filtering(company_recent_filings_df_list)

    ac_num_list = get_latest_num(company_recent_filings_df_list)

    data_list = get_filing_summary(ac_num_list, cik_list)

    finding(data_list, search_words)


# 지역별 매출은 _GEOKEYWORD, 제품별 매출은
get_data(['msft', 'aapl', 'nvda', 'amzn', 'nflx'], _GEOKEYWORD)


# 파라미터: 회사 ticker(list), 키워드(list)
# 'msft', 'aapl', 'nvda', 'amzn', 'nflx'
# get_data(['msft', 'aapl', 'nvda', 'amzn', 'nflx'],
#          ['segment', 'information', 'tables'])
