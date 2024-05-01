import pandas as pd
from openai import OpenAI

import json

fp = '/Users/rohhaechang/Desktop/testfolder0/edgar-crawler-main/datasets/EXTRACTED_FILINGS/320193_10Q_2022_0000320193-23-000006.json'

with open(fp, "r", encoding="utf-8") as file:
    data = json.load(file)


all_text = ""
for key, value in data.items():
    all_text += f"{key}: {value}\n"

API_KEY = 'secretapikey'
client = OpenAI(api_key=API_KEY)

# text = 'he following table shows net sales by category for 2023, 2022 and 2021 (dollars in millions):\n2023 Change 2022 Change 2021\nNet sales by category:\niPhone (1)\n$ 200,583 (2) % $ 205,489 7 % $ 191,973\nMac (1)\n29,357 (27) % 40,177 14 % 35,190\niPad (1)\n28,300 (3) % 29,292 (8) % 31,862\nWearables, Home and Accessories (1)\n39,845 (3) % 41,241 7 % 38,367\nServices (2)\n85,200 9 % 78,129 14 % 68,425\nTotal net sales $ 383,285 (3) % $ 394,328 8 % $ 365,817'

# js = [['segment by categories', '2023', '2022', '2021', '2020', '2019'], ['iphone', '200583', '205489', '191973', '137781', '142381'], ['mac', '29357', '40177', '35190', '28622', '25740'], ['ipad', '28300', '29292', '31862', '23724',
#                                                                                                                                                                                               '21280'], ['Wearables, Home and Accessories', '39845', '41241', '37367', '30520', '24482'], ['Services', '85200', '78129', '68425', '53768', '46291'], ['Total net sales', '383285', '394328', '365817', '274515', '260174']]
# df = pd.DataFrame(js)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"using this disclosure data, give investment advice for this company. {all_text}"}
    ]
)

print(completion.choices[0].message)

# 637, 739
# dataframe - 847, 932 (210, 193)
# text - 1054, 1158 (207, 226)
# all_text(10-q) - 9946, 1397 (약 10000)

# gpt-3은 토큰 1000000 당 질문은 0.5달러, 대답은 1.5달러  gpt-4 turbo는 질문은 10달러, 대답은 30달러
# gpt-3 최대 토큰 개수는 16385, gpt-4 turbo 최대 토큰 개수는 128,000

# 10-k, gpt4-turbo
# apple의 10-k를 텍스트화 시킨 것의 토큰 개수는 약 50000개 정도
# 약 20개의 10-k를 입력하려면 10달러가 필요

# 10-q, gpt3.5
# 10-q를 텍스트화 시킨 것의 토큰 개수는 약 10000개 정도
# 100개의 10-q를 입력한다면 0.5달러가 필요

# gpt3.5는 10000 토큰에 0.005, gpt4-turbo는 10000토큰에 0.1
# 표 데이터만 추려서 입력한다면, 하나의 보고서에 20~30개의 표 데이터가 있다고 가정하면, 하나의 표 데이터의 토큰이 200~400이라고 가정하면, 4000~12000 토큰이 필요하다.
# gpt3.5를 이용했을 경우에는 입력에 0.002~0.006달러(3~9원), gpt4-turbo를 이용했을 경우에는 입력에 0.04~0.12달러(60~180원)
