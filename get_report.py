import requests
import pandas


def getData():
    url = 'https://opendart.fss.or.kr/api/fnlttSinglIndx.json'
    params = {
        'crtfc_key': 'ea527c624351f396e141e8534aa7da0180e04ed6',
        'corp_code': '00126380',
        'bsns_year': '2023',
        'reprt_code': '11011',
        'idx_cl_code': 'M210000'
    }
    response = requests.get(url, params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('error')


report = getData()
dataFrame = pandas.DataFrame(report['list'])
revised_dataFrame = dataFrame.iloc[:, [5, 7, 8]]

print(revised_dataFrame)
