import praw
import prawcore

target_subreddits = ['Cryptocurrency', 'CryptoMarkets', 'Bitcoin']


def search_reddit(query, subreddits, limit=200):
    CLIENT_ID = '4UZJBwNXTLoEAohHl4FsRQ'
    CLIENT_SECRET = '5xiH5akBQ16p_eQoLbQgoJCJ621wRg'
    USER_AGENT = 'Financial-Ad7890'
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
    subreddit_str = '+'.join(subreddits)
    reddit_titles = []
    try:
        results = reddit.subreddit(subreddit_str).search(query, limit = 1000, sort='new')
    except prawcore.exceptions.BadRequest as e:
        print(f"Errore durante la ricerca: {e}")
        return
    for post in results:
        reddit_titles.append(post.title)
    return reddit_titles


if __name__ == '__main__':
    search_query = 'crypto'
 
    reddit_titles = search_reddit(search_query, target_subreddits)
    print(reddit_titles)
