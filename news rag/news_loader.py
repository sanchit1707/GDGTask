import os
from newsapi import NewsApiClient

newsapi=NewsApiClient(api_key=os.getenv("32dd9a5221cc4b5daeb8baab6a504373"))


def fetch_news(query="stock market",page_size=20):
    response=newsapi.get_everything(
        q=query,
        language="en",
        sort_by="relevancy",
        page_size=page_size
    )
    
    docs = []
    for article in response["articles"]:
        docs.append(f"""
Title: {article['title']}
Source: {article['source']['name']}
Published: {article['publishedAt']}
Description: {article['description']}
Content: {article['content']}
""")

    return docs
