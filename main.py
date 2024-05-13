import praw
import os
from dotenv import load_dotenv

load_dotenv()
def get_top_stocks(subreddit_name, num_posts):
    # Reddit API credentials
    reddit = praw.Reddit(client_id= os.getenv('CLIENT_ID'),
                         client_secret= os.getenv('CLIENT_SECRET'),
                         user_agent= os.getenv('USER_AGENT') )

    # Get subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Initialize dictionary to store stock mentions and their frequencies
    stock_freq = {}

    # Iterate through top 'num_posts' posts
    for submission in subreddit.top(limit=num_posts):
        # Get post title and selftext
        post_text = submission.title + ' ' + submission.selftext
        # Split the text into words
        words = post_text.split()
        # Iterate through words to find potential stock mentions
        for word in words:
            # Check if the word is a stock symbol (e.g., AAPL, TSLA)
            if word.isupper() and word.isalpha() and len(word) <= 5:
                # Increment frequency count for the stock symbol
                if word in stock_freq:
                    stock_freq[word] += 1
                else:
                    stock_freq[word] = 1

    # Sort stocks by frequency in descending order
    sorted_stocks = sorted(stock_freq.items(), key=lambda x: x[1], reverse=True)

    # Print the top 10 discussed stocks
    print("Top 10 discussed stocks:")
    for i, (stock, freq) in enumerate(sorted_stocks[:10], start=1):
        print(f"{i}. {stock}: {freq} mentions")

# Example usage
subreddit_name = 'stocks'  # You can change this to any subreddit you want
num_posts = 1000  # Number of top posts to analyze
get_top_stocks(subreddit_name, num_posts)
