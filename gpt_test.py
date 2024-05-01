import pandas as pd
from openai import OpenAI

import json

data_path = '/Users/rohhaechang/Desktop/testfolder0/edgar-crawler-main/datasets/EXTRACTED_FILINGS/320193_10K_2023_0000320193-23-000106.json'

with open(data_path, "r", encoding="utf-8") as file:
    data = json.load(file)

item1 = data['item_8']

text = """
Item 1.
- Company Background
- Products (iPhone, Mac, iPad, Wearables, Home, Accessories)
- Services (Advertising, AppleCare, Cloud Services, Digital Content, Payment Services)
- Segments (Americas, Europe, Greater China, Japan, Rest of Asia Pacific)
- Markets and Distribution
- Competition
- Supply of Components
- Research and Development
- Intellectual Property
- Business Seasonality and Product Introductions
- Human Capital
- Workplace Practices and Policies
- Compensation and Benefits
- Inclusion and Diversity
- Engagement
- Health and Safety
- Available Information

Item 1A.
1. Macroeconomic and Industry Risks
2. Political events, trade and other international disputes
3. Adverse economic conditions
4. Natural disasters, public health issues, and industrial accidents
5. Global climate change
6. Industrial accidents at suppliers and contract manufacturers
7. Competition in global markets
8. Intellectual property protection
9. Business interruptions
10. Data protection and cybersecurity risks
11. Legal and regulatory compliance risks
12. Financial risks related to foreign exchange rates, credit risk, and tax liabilities
13. Stock price volatility

Item 2.
- Headquarters location
- Owned or leased facilities
- Corporate functions
- R&D facilities
- Data centers
- Retail locations
- Condition of facilities and equipment

Item 3.
- Epic Games lawsuit regarding antitrust violations
- Masimo complaint regarding patent infringement on Apple Watch Series 6 and 7
- Other ongoing legal proceedings and claims not fully resolved with potential financial impact on the company's financial condition or operating results.


Item 4.
- Compliance with regulations set forth by regulatory bodies such as the Mine Safety and Health Administration (MSHA)
- Measures taken to ensure a safe working environment for employees in mining operations
- Training programs and safety protocols implemented to prevent accidents and injuries in mines
- Reporting of any incidents or violations related to mine safety regulations
- Investments in technology or equipment to improve mine safety standards and practices

Item 5.
- Market for Registrant's Common Equity
- Holders of the Company's common stock
- Purchases of Equity Securities by the Issuer and Affiliated Purchasers
- Share repurchase program details
- Company Stock Performance and comparison to S&P 500 Index and Dow Jones U.S. Technology Supersector Index

Item 6.
-

Item 7.
- Fiscal Period
- Fiscal Year Highlights
- Macroeconomic Conditions
- Segment Operating Performance
- Products and Services Performance
- Gross Margin
- Operating Expenses
- Provision for Income Taxes
- Liquidity and Capital Resources
- Capital Return Program
- Critical Accounting Estimates
- Uncertain Tax Positions
- Legal and Other Contingencies

Item7A.
- Interest Rate Risk
- Foreign Exchange Rate Risk
- Investment Portfolio
- Term Debt
- Derivative Instruments
- Value-at-Risk Model
- Monte Carlo Simulation
- Fair Value
- U.S. Dollar Strength
- Currency Exposures
- Gross Margins
- Sales
- Accounting Considerations

Item 8.
financial statements, supplementary data, index to consolidated financial statements, statements of operations, statements of comprehensive income, balance sheets, statements of shareholders' equity, statements of cash flows, notes to the financial statements, reports of independent registered public accounting firm, share-based compensation, internal control over financial reporting, share repurchase program, restricted stock units, revenue from different geographical segments, operating income by segment, deferred tax assets and liabilities, uncertain tax positions, commitment, contingencies, and supply concentrations.

Item 9.
-

Item 9A.
- Evaluation of Disclosure Controls and Procedures
- Inherent Limitations over Internal Controls
- Management’s Annual Report on Internal Control over Financial Reporting
- Changes in Internal Control over Financial Reporting

Item 9B.
- Insider Trading Arrangements
- Disclosure Regarding Foreign Jurisdictions that Prevent Inspections

Item 10.
1. Directors
2. Executive Officers
3. Corporate Governance

Item 11.
- Executive Compensation

Item 12.
- Security ownership
- Beneficial owners
- Management
- Related stockholder matters

Item 13.
-

Item 14.
-Principal Accountant Fees and Services.
Item 15.

"""
# all_text = ""
# for key, value in data.items():
#     all_text += f"{key}: {value}\n"

# item_5 = data['item_5']
# item_6 = data['item_6']
# item_7 = data['item_7']


API_KEY = ''
client = OpenAI(api_key=API_KEY)

# text = 'he following table shows net sales by category for 2023, 2022 and 2021 (dollars in millions):\n2023 Change 2022 Change 2021\nNet sales by category:\niPhone (1)\n$ 200,583 (2) % $ 205,489 7 % $ 191,973\nMac (1)\n29,357 (27) % 40,177 14 % 35,190\niPad (1)\n28,300 (3) % 29,292 (8) % 31,862\nWearables, Home and Accessories (1)\n39,845 (3) % 41,241 7 % 38,367\nServices (2)\n85,200 9 % 78,129 14 % 68,425\nTotal net sales $ 383,285 (3) % $ 394,328 8 % $ 365,817'

# js = [['segment by categories', '2023', '2022', '2021', '2020', '2019'], ['iphone', '200583', '205489', '191973', '137781', '142381'], ['mac', '29357', '40177', '35190', '28622', '25740'], ['ipad', '28300', '29292', '31862', '23724',
#                                                                                                                                                                                               '21280'], ['Wearables, Home and Accessories', '39845', '41241', '37367', '30520', '24482'], ['Services', '85200', '78129', '68425', '53768', '46291'], ['Total net sales', '383285', '394328', '365817', '274515', '260174']]
# df = pd.DataFrame(js)


# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": f"in this disclosure data, tell me topics. {item1}"}
#     ]
# )

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user",
            "content": f". {item1}"}
    ]
)

print(completion.choices[0].message.content)

a = completion.choices[0].message.content

print(type(a))  # 무조건 String

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": f"using this disclosure data, Summarize each topic into one or two lines, {item_1}"}
#     ]
# )

# print(completion.choices[0].message.content)


# 637, 739
# dataframe - 847, 932 (210, 193)
# text - 1054, 1158 (207, 226)
# all_text(10-q) - 9946, 1397 (약 10000)

# gpt-3.5은 토큰 1000000 당 질문은 0.5달러, 대답은 1.5달러  gpt-4 turbo는 질문은 10달러, 대답은 30달러
# gpt-3.5 최대 토큰 개수는 16385, gpt-4 turbo 최대 토큰 개수는 128,000

# 10-k, gpt4-turbo
# apple의 10-k를 텍스트화 시킨 것의 토큰 개수는 약 50000개 정도
# 약 20개의 10-k를 입력하려면 10달러가 필요

# 10-q, gpt3.5
# 10-q를 텍스트화 시킨 것의 토큰 개수는 약 10000개 정도
# 100개의 10-q를 입력한다면 0.5달러가 필요

# 10-k, gpt3.5
# 20개의 10-k를 입력하려면 0.5달러가 필요 -> 출력은 이보다 적음 최대로 합해서 1달러 라고 하자.
# 한 회사 당 5개년을 본다고 하면, 0.25달러가 필요.

# 1달러로 4개의 회사, 5달러로 20개의 회사의 5개년 답변 받기 가능.


# gpt3.5는 10000 토큰에 0.005, gpt4-turbo는 10000토큰에 0.1
# 표 데이터만 추려서 입력한다면, 하나의 보고서에 20~30개의 표 데이터가 있다고 가정하면, 하나의 표 데이터의 토큰이 200~400이라고 가정하면, 4000~12000 토큰이 필요하다.
# gpt3.5를 이용했을 경우에는 입력에 0.002~0.006달러(3~9원), gpt4-turbo를 이용했을 경우에는 입력에 0.04~0.12달러(60~180원)
