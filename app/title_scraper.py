import requests
import json
from datetime import datetime, timedelta

api_key = "e442b41967dd4ea0b151a185cf4d18c0"
cx = "b50a399b67ccc4f5a"


def get_google_news(query, api_key, pages=10):
    api_key = "e442b41967dd4ea0b151a185cf4d18c0"
    results = []
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%dT%H:%M:%S')
    for i in range(1, pages + 1):
        url = f"https://newsapi.org/v2/everything?q={query}&from={yesterday_str}&apiKey={api_key}&pageSize=10&page={i}"
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "ok":
            results.extend(data["articles"])
        else:
            print(f"Error: {data['message']}")
            break

    return results
def get_titles(dict_news):
    titles = []
    for news in dict_news:
        titles.append(news["title"])
    return titles


if __name__ == '__main__': 
    query = "btc"
    news_results = get_google_news(query, api_key)
    titles = get_titles(news_results)


    '''for i, news in enumerate(news_results):
    print(f"{i+1}. {news['title']}") '''

    print(titles)







