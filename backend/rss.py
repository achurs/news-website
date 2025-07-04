import random
import feedparser
import time

def news():
    feed = feedparser.parse("https://news.google.com/rss")
    if not feed.entries:
        return "No news available at the moment."
    entry = random.choice(feed.entries)
    info = {
        "title": entry.title,
        "link": entry.link,
        "published": entry.published
    }
    return info

def rss_test():
    feed = feedparser.parse("https://news.google.com/rss")
    headlines = [entry.title for entry in feed.entries]
    if not headlines:
        return "No news available at the moment."
    print("Fetched news headlines:", headlines)
    return random.choice(headlines)

if __name__ == "__main__":
    while True:
        print(news())
        time.sleep(2)
