# sentiment_analysis.py
from positive_words import positive_words
from negative_words import negative_words
from title_scraper import get_google_news, api_key, query, get_titles

def analyze_sentiment(titles):
    score = 0
    
    for title in titles:
        words = title.lower().split()
        for word in words:
            if word in positive_words:
                score += 1
            elif word in negative_words:
                score -= 1
                
    return score

news_results = get_google_news(query, api_key)
titles = get_titles(news_results)

result = analyze_sentiment(titles)
print("Sentiment score:", result)



