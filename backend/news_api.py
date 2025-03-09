"""
This file contains the code for scraping news from the Google News website.
This code is used to get the news from the internet and store it in the database.
"""
import requests
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("NEWS_API")
news_url = f"https://newsapi.org/v2/everything?q=india&apiKey={api_key}"

response = requests.get(news_url)
news = response.json()
articles = news['articles']

def get_full_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        full_content = ' '.join([para.get_text() for para in paragraphs])
        return full_content
    else:
        return "Failed to retrieve the full content."

for i in range(2):  # Get the first 2 articles
    content = articles[i]['content']
    url = articles[i]['url']
    print(f"Truncated Content: {content}")
    full_content = get_full_content(url)
    print(f"Full Content: {full_content}\n")