import requests
from bs4 import BeautifulSoup
import lxml
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'
}

for i in range(0, 140, 8):
    url = f'https://www.skiddle.com/api/v1/events/search/?limit=8&offset={i}&eventcode=CLUB%2CBARPUB%2CGAMING%2CEDU%2CAWARD%2CTRAVEL&radius=10&minDate=2025-06-01T00%3A00%3A00&maxDate=2025-07-31T23%3A59%3A59&hidecancelled=1&order=trending&showVirtualEvents=0&artistmeta=1&artistmetalimit=3&aggs=genreids%2Ceventcode&pub_key=42f25&platform=web&collapse=uniquelistingidentifier'
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    print(json_data)
    
    # with open(f'data{i}', 'w', encoding='utf-8') as file:
    #     json.dump(json_data, file, indent=4, ensure_ascii=False)
    # html_response = json_data['html']

    # with open(f'index_{i}.html', 'w') as file:
    #     file.write(html_response)