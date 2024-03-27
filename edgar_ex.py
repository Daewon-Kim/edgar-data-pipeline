import requests
import pandas as pd
import json

CIK = 'CIK0000320193'
url = f'https://data.sec.gov/submissions/{CIK}.json'
headers = {'User-Agent': 'Mozilla'}
res = requests.get(url, headers=headers).json()
# response에서 중요한 정보는 filings에 있고, recent와 files가 나오는데 recent는 최근의 문서 정보, files는 문서들 집합의 정보이다.

# dataFrame에 지금 필요한 속성들만 넣었다.
dataFrame = pd.DataFrame(res['filings']['recent'], columns=[
                         'accessionNumber', 'filingDate', 'form', 'primaryDocument'])

# Apple의 최신 10-K 보고서에 대한 정보 dataFrame 출력
# print(dataFrame[dataFrame.form == "10-K"])

# 그 중 가장 최신 보고서 html 파일로 받기
access_number = dataFrame[dataFrame.form ==
                          '10-K'].accessionNumber.values[0].replace("-", "")
file_name = dataFrame[dataFrame.form == '10-K'].primaryDocument.values[0]
# 이 Url에 요청하면 준다.
filingUrl = f'https://www.sec.gov/Archives/edgar/data/{CIK}/{access_number}/{file_name}'

req_content = requests.get(
    'https://www.sec.gov/Archives/edgar/data/1776048/000109991022000055/ammx_10k.htm', headers=headers).content.decode("utf-8")

with open(file_name, "w") as f:
    f.write(req_content)
    f.close()


entireCompanyFacts = requests.get(
    "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json", headers=headers).json()

# entireCompanyFacts.keys() - 'cik', 'entityName', 'facts'

# entireCompanyFacts['facts'].keys() - 'dei', 'us-gaap'

# entireCompanyFacts['facts']['dei'].keys() - outstanding shares(전체 주식. 경영진과 임원이 소유하고 있는 것 포함)와 public float(실제 유통되는 주식) 정보

file_path = 'iwanttofindit.json'
with open(file_path, 'w') as f:
    json.dump(entireCompanyFacts['facts']['us-gaap'], f)

# 'accessionNumber', 'filingDate', 'reportDate',
# 'acceptanceDateTime', 'act', 'form', 'fileNumber',
# 'filmNumber', 'items', 'size', 'isXBRL', 'isInlineXBRL', 'primaryDocument', 'primaryDocDescription'


# https://data.sec.gov/submissions/CIK##########.json
# 특정 회사(CIK)의 최신 filing 정보
# response['filings']['recent'] 로 dataFrame을 만들고, columns에 필요한 속성은 accessionNumber, filingDate, form, primaryDocument 정도인 것 같다.


# https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/AccountsPayableCurrent.json
#


# https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
# https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json
