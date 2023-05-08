from flask import render_template, request
from app import app
from .vader_Sentiment import analyze_sentiment_vader
from .title_scraper import get_google_news, api_key, get_titles
from .reddit_scraper import search_reddit, target_subreddits

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/search')
def search():
    query = request.args.get('query', '')
    news_results = get_google_news(query, api_key)
    news_titles = get_titles(news_results)
    reddit_titles = search_reddit(query, target_subreddits)
    avg_compound_score, avg_positive_score, avg_neutral_score, avg_negative_score = analyze_sentiment_vader(news_titles + reddit_titles)
    result = {
        'query': query,
        'compound': avg_compound_score,
        'positive': avg_positive_score,
        'neutral': avg_neutral_score,
        'negative': avg_negative_score
    }
    
    return render_template('index.html', result=result)

