import json

# 파일 경로 
appl_data_path = "APPLE_EXTRACTED_FILINGS.json file path"
msft_data_path = "MICROSOFT_EXTRACTED_FILINGS.json file path"
amzn_data_path = "AMAZON_EXTRACTED_FILINGS.json file path"


# 기업의 10K 데이터 load
def load_10K(corporation):
    if corporation == "apple":
        path = appl_data_path
    elif corporation == "microsoft":
        path = msft_data_path
    elif corporation == "amazon":
        path = amzn_data_path
    else:
        return None

    if path:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    return None