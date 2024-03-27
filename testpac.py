import pandas as pd
import requests

# url = 'https://www.sec.gov/files/company_tickers_exchange.json'
# headers = {'User-Agent': 'Mozilla'}
# res = requests.get(url, headers=headers)
# cik_list = res.json()

# cik_df = pd.DataFrame(cik_list['data'], columns=cik_list['fields'])

# NVIDIA_CIK = cik_df.iat[2, 0]

# CIK = 'CIK0001045810'
# url = f'https://data.sec.gov/submissions/{CIK}.json'
headers = {"User-Agent": 'Mozilla'}

# res = requests.get(url, headers=headers).json()

# dataFrame = pd.DataFrame(res['filings']['recent'], columns=[
#                          'accessionNumber', 'filingDate', 'form', 'primaryDocument'])

# access_number = dataFrame[dataFrame.form ==
#                           '10-K'].accessionNumber.values[0].replace("-", "")
# file_name = dataFrame[dataFrame.form == '10-K'].primaryDocument.values[0]

# req_content = requests.get(
#     f'https://www.sec.gov/Archives/edgar/data/{NVIDIA_CIK}/{access_number}/{file_name}', headers=headers).content.decode('utf-8')


# https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json

# 특정 기간에 특정 요소에 대한 데이터. 회사는 cik를 이용해서 찾아야 한다.
response1 = requests.get(
    'https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json', headers=headers).json()

dataframe1 = pd.DataFrame(response1['data'], columns=[
                          'accn', 'cik', 'entityName', 'val'])

print(dataframe1.head(3))
