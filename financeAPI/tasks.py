from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Article, Symbols
from .serializer import ArticleSerializer, SymbolSerializer


def create_default_symbols():
    symbols = Symbols.objects.all()
    if len(symbols) is 0:
        default_symbols = [
            {
                'symbol': 'INTC'
            },
            {
                'symbol': 'AAPL'
            },
            {
                'symbol': 'TWTR'
            },
            {
                'symbol': 'GC=F'
            }
        ]
        for i in default_symbols:
            serializer = SymbolSerializer(data=i)
            serializer.is_valid(raise_exception=True)
            serializer.save()


@shared_task(bind=True)
def collect_articles(self):
    create_default_symbols()
    symbols = Symbols.objects.all()
    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s='
    other_params = '&region=US&lang=en-US'

    for j in symbols:
        get_articles = requests.get(url + j.symbol + other_params, headers={'User-agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(get_articles.content, 'xml')
        articles = soup.findAll('item')
        articles_list = []
        symbol_id = j.id

        for i in articles:
            article = {
                'title': i.find('title').text,
                'description': i.find('description').text,
                'external_id': i.find('guid').text,
                'article_link': i.find('link').text,
                'publish_date': i.find('pubDate').text,
                'symbol': symbol_id

            }

            articles_list.append(article)

        for i in articles_list:

            existing_article = Article.objects.get_or_none(external_id=i.get('external_id'))

            if existing_article is None:
                serializer = ArticleSerializer(data=i)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else:
                serializer = ArticleSerializer(instance=Article.objects.get(external_id__exact=i.get('external_id')), data=i)
                serializer.is_valid()
                serializer.save()
        articles_list = []

    return "Done"

