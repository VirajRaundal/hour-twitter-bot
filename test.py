import tweepy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_twitter_connection():
    try:
        # Get credentials from environment variables
        api_key = os.getenv('TWITTER_API_KEY')
        api_secret = os.getenv('TWITTER_API_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        
        # Verify that all credentials are present
        if not all([api_key, api_secret, access_token, access_token_secret]):
            print("Error: Missing credentials in .env file")
            return False
            
        # Initialize Twitter client
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        # Try to post a test tweet
        test_tweet = client.create_tweet(text="This is a test tweet from my bot! 🤖")
        print("Success! Test tweet posted.")
        print(f"Tweet ID: {test_tweet.data['id']}")
        return True
        
    except Exception as e:
        print(f"Error connecting to Twitter: {str(e)}")
        return False

if __name__ == "__main__":
    test_twitter_connection()