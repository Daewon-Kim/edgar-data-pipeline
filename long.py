# need url: https://opendart.fss.or.kr/api/list.json?crtfc_key=인증키
import requests
import pandas

crtfc_key = 'ea527c624351f396e141e8534aa7da0180e04ed6'


def get_dart_data():
    url = "https://opendart.fss.or.kr/api/list.json?crtfc_key=ea527c624351f396e141e8534aa7da0180e04ed6"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)


def get_executive(corp_code):
    crtfc_key = 'ea527c624351f396e141e8534aa7da0180e04ed6'
    bsns_year = '2023'
    reprt_code = '11013'
    post_url = f'https://opendart.fss.or.kr/api/exctvSttus.json?crtfc_key={crtfc_key}&corp_code={corp_code}&bsns_year={bsns_year}&reprt_code={reprt_code}'
    response = requests.get(post_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error', response.status_code)


dart_data = get_dart_data()

dataList = []

for i in range(5):
    dataList.append(dart_data['list'][i])

dataFrame = pandas.DataFrame(dataList)

# dataFrame = dataFrame.at[0, 'corp_code']

# executive_data = get_executive(dataFrame)

# dataList2 = []

# for i in range(5):
#     dataList.append(executive_data['list'][i])

# dataFrame2 = pandas.DataFrame(dataList2)

print(dataFrame)
