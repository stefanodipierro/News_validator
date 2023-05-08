from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .title_scraper import get_google_news, api_key, get_titles
from .reddit_scraper import search_reddit, target_subreddits
from .positive_words import positive_words
from .negative_words import negative_words

def analyze_sentiment_vader(titles):
    analyzer = SentimentIntensityAnalyzer()
    analyzer.lexicon.update(positive_words)
    analyzer.lexicon.update(negative_words)
    
    compound_scores = []
    positive_scores = []
    neutral_scores = []
    negative_scores = []

    for title in titles:
        sentiment = analyzer.polarity_scores(title)
        compound_scores.append(sentiment['compound'])
        positive_scores.append(sentiment['pos'])
        neutral_scores.append(sentiment['neu'])
        negative_scores.append(sentiment['neg'])

    average_compound_score = sum(compound_scores) / len(compound_scores)
    average_positive_score = sum(positive_scores) / len(positive_scores)
    average_neutral_score = sum(neutral_scores) / len(neutral_scores)
    average_negative_score = sum(negative_scores) / len(negative_scores)

    return average_compound_score, average_positive_score, average_neutral_score, average_negative_score

if __name__ == '__main__':
    query = 'BTC'
    news_results = get_google_news(query, api_key)
    news_titles = get_titles(news_results)
    reddit_titles = search_reddit(query, target_subreddits)
    average_compound_score, average_positive_score, average_neutral_score, average_negative_score = analyze_sentiment_vader(news_titles + reddit_titles)
    print(average_compound_score, average_positive_score, average_neutral_score, average_negative_score)

