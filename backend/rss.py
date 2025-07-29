import random
import feedparser
import time
from googlenewsdecoder import gnewsdecoder

def news():
    feed = feedparser.parse("https://news.google.com/rss")
    if not feed.entries:
        return "No news available at the moment."
    entry = random.choice(feed.entries)
    link = gnewsdecoder(entry.link)
    if not link:
        link = entry.link  # Fallback to original link if decoding fails
    info = {
        "title": entry.title,
        "link": link['decoded_url'] if link else entry.link,
        "published": entry.published
    }
    return info

def rss_test():
    feed = feedparser.parse("https://news.google.com/rss")
    headlines = [entry.title for entry in feed.entries]
    if not feed.entries:
        return "No news available at the moment."
    entry = random.choice(feed.entries)
    link = gnewsdecoder(entry.link)
    if not link:
        link = entry.link  # Fallback to original link if decoding fails
    info = {
        "title": entry.title,
        "link": link['decoded_url'] if link else entry.link,
        "published": entry.published
    }
    return info


if __name__ == "__main__":
    while True:
        print(rss_test())
        time.sleep(2)
