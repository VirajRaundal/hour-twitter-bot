import tweepy
from datetime import datetime, timezone
import time
import os
from dotenv import load_dotenv
import pytz

# Load environment variables
load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

def setup_twitter_api():
    """Set up and return Twitter API client"""
    client = tweepy.Client(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )
    return client

def calculate_year_progress():
    """Calculate hours passed and remaining in 2025 (Pacific Time)"""
    # Get current Pacific Time
    pacific_tz = pytz.timezone('America/Los_Angeles')
    now = datetime.now(pacific_tz)
    
    # Define start and end of 2025 in Pacific Time
    year_start = pacific_tz.localize(datetime(2025, 1, 1))
    year_end = pacific_tz.localize(datetime(2026, 1, 1))
    
    # Calculate hours
    total_hours_in_year = 8760  # 365 days * 24 hours
    hours_passed = int((now - year_start).total_seconds() / 3600)
    hours_remaining = total_hours_in_year - hours_passed
    
    return hours_passed, hours_remaining

def create_tweet_text(hours_passed, hours_remaining):
    """Create formatted tweet text"""
    pacific_time = datetime.now(pytz.timezone('America/Los_Angeles'))
    return f"2025 Progress Update 🕒 (PST)\n\nHours passed: {hours_passed:,}\nHours remaining: {hours_remaining:,}\n\nUpdated: {pacific_time.strftime('%I:%M %p')}\n\n"

def main():
    # Set up Twitter API
    client = setup_twitter_api()
    
    while True:
        try:
            # Calculate progress
            hours_passed, hours_remaining = calculate_year_progress()
            
            # Create and post tweet
            tweet_text = create_tweet_text(hours_passed, hours_remaining)
            client.create_tweet(text=tweet_text)
            
            # Wait for an hour before next update
            time.sleep(3600)  # 3600 seconds = 1 hour
            
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(300)  # Wait 5 minutes if there's an error

if __name__ == "__main__":
    main()