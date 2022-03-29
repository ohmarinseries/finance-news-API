# Finance News API / Scrapper Service

## Setup

The first thing to do is to clone the repository(using SSH):

```shell
$ git clone git@github.com:ohmarinseries/finance-news-API.git
```
#### Then navigate to cloned project

# Build
To start application locally you need to run following command:

####Required: You need to have docker desktop on your machine to run.

```shell
$ docker-compose up --build
```
####Note: Also build will take some time

# Use
Finance News API is an REST API for collecting news articles from Yahoo RSS Feed.
Scrapping Service is collecting data for AAPL, TWTR, INTC, GC=F (by default), but
can add additional symbols by sending request:
To see symbols that data is being collected for send request to:

```http request
GET http://localhost:8080/news/symbols/
```
To create additional symbols for collection:
```http request
POST http://localhost:8080/news/symbols/
BODY:
{
'symbol': 'EXAMPLE'
}
```

Celery is scrapping data every minute from Yahoo RSS Feed

To see all scrapped articles send request to:

```http request
GET http://localhost:8080/news/articles/
```

To see scrapped articles from specific symbol add query parameter to previous request:

```http request
GET  http://localhost:8080/news/articles/?symbol=TWTR
```

Use query parameters page_size and page to navigate through pagination, example:

```http request
GET http://localhost:8080/news/articles/?page_size=5&page=3&symbol=AAPL
```

#To open full documentation:
```http request
GET http://localhost:8080/swagger/
```

#Run Tests
To run tests for application run the following command:
```shell
python3 manage.py test financeAPI
```
