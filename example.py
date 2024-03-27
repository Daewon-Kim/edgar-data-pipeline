import requests
import pandas as pd

# edgar api(무료) 사용법

# CIK는 기업 고유 번호, 아래는 Apple의 CIK
CIK = '0000320193'

# 요청할 URL
# https://data.sec.gov/submissions/CIK##########.json 여기에 요청을 보내라고 하는데, ##은 CIK 코드를 넣으라는 의미였다.
# 그래서 아래와 같이 CIK를 포함시켰다.

url = f'https://data.sec.gov/submissions/CIK{CIK}.json'

# header는 서버에 보내는 추가 정보 같은 느낌이다. 여기서는 클라이언트가 Mozilla 브라우저처럼 작동하라는 뜻인데, 필요 요구 사항은 보통 api 문서에서 알려준다.
headers = {
    'User-Agent': 'Mozilla'
}

# requests는 서버에 요청을 보낼 수 있게 도와주는 라이브러리. get이라는 함수는 필수 인수로 url이 필요하다. headers는 필요한 추가 정보라 해서 넣은 것.
# 뒤에 json()은 변수를 json 으로 변환시켜서 보기 편하게 하기 위함이다.
# json은 {a:1, b:2} 이런 파일이다.

response = requests.get(url, headers=headers).json()

# 여기서 이 response를 출력하면 너무 많은 정보가 나온다.
# json은 안에 array(list)도 들어갈 수 있는데, 이 response안에 그렇게 들어가 있다.

# 이 데이터에서 필요한 정보에 대한 키는 response['filings']['recent'].keys() 이렇게 접근할 수 있다.
# print(response['filings']['recent'].keys())

# 출력해서 어떤 키가 있는지 보고, 필요하다 생각하는 것을 출력해서 연습해보면 좋을 것 같다.
# ex) print(response['filings']['recent']['filingDate']) 문서의 생성 날짜들만 출력된다.


# 예쁘게 표 형태로 표현해서 보려면, pandas의 dataFrame 으로 표현하면 좋다.

dataFrame = pd.DataFrame(response['filings']['recent'], columns=[
                         'accessionNumber', 'filingDate', 'form',])
# 이렇게 하면 accessionNumber, filingDate, form이 열(속성)으로 나오는 표가 생성된다.

# 출력 해보기
print(dataFrame)
