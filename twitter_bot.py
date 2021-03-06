from twitter import Twitter, OAuth, TwitterHTTPError
import time
from typing import List

OAUTH_TOKEN = "xxxxx"
OAUTH_SECRET = "xxxxx"
CONSUMER_KEY = "xxxxx"
CONSUMER_SECRET = "xxxxx"

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))


def search_tweets(q: str, count: int =100):
    """
    Search all tweets containing query phrase "q".
    """
    return t.search.tweets(q=q, result_type="recent", count=count)


def fav_tweet(tweet: Twitter):
    """
    Favorite a given tweet.
    """
    try:
        result = t.favorites.create(_id=tweet["id"])
        print "Favorited: %s" % (result["text"])
        return result
    except TwitterHTTPError as e:
        print "Error: ", e
        return None


def auto_fav(q: str, count: int = 100):
    """
    Repeatedly favorite "count" number number of tweets containing query phrase "q".
    """
    result = search_tweets(q, count)
    a = result["statuses"][0]["user"]["screen_name"]
    print (a)
    success = 0
    for tweet in result["statuses"]:
        if fav_tweet(tweet) is not None:
            success += 1
    print ("We Favorited a total of %i out of %i tweets" % (success, len(result["statuses"])))


def main():
    auto_fav(q="ice cream", count=250)
    return None


if __name__ == "__main__":
    main()
