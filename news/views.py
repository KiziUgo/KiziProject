import requests
import html5lib
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from newsapi import NewsApiClient



def news(request):
    newsapi = NewsApiClient(api_key="85641f417ecf4f7ca44c8117c15d96b5")
    topheadlines = newsapi.get_top_headlines(sources='the-wall-street-journal')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'news/index.html', context={"mylist": mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key="85641f417ecf4f7ca44c8117c15d96b5")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'bbc.html', context={"mylist": mylist})


