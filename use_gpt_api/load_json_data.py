import json

# json 파일 open 및 load
def load_json(file_name):
    if file_name == "corporation":
        file_path = "company_list.json file path"
    elif file_name == "prompt":
        file_path = "prompt_list.json file path"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)