import json
from openai import OpenAI
import re


appl_data_path = '/Users/rohhaechang/Desktop/testfolder0/edgar-crawler-main/datasets/EXTRACTED_FILINGS/320193_10K_2023_0000320193-23-000106.json'
msft_data_path = '/Users/rohhaechang/Desktop/testfolder0/edgar-crawler-main/datasets/EXTRACTED_FILINGS/789019_10K_2023_0000950170-23-035122.json'
amzn_data_path = '/Users/rohhaechang/Desktop/testfolder0/edgar-crawler-main/datasets/EXTRACTED_FILINGS/1018724_10K_2022_0001018724-23-000004.json'

data = ''

# 입력 받기
while True:
    prompt_company = input("애플, 마이크로소프트, 아마존 중 검색할 회사를 입력하세요: ")
    if (prompt_company.strip() == "애플"):
        with open(appl_data_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        break
    elif (prompt_company.strip() == "마이크로소프트"):
        with open(msft_data_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        break
    elif (prompt_company.strip() == "아마존"):
        with open(amzn_data_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")

# item 1에 대한 데이터
prompt_data = data['item_1']


# gpt 부분
API_KEY = ''
client = OpenAI(api_key=API_KEY)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user",
            "content": f"in this disclosure data, summarize the main products and services in one or two lines, and if there is a new product, please explain it in one or two lines, like this format. products and service: ... \n new product:... {prompt_data}"}
    ]
)

print(completion.choices[0].message.content)
