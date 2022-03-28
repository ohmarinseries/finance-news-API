# Financial News API / Scrapper Service

## Setup

The first thing to do is to clone the repository(using SSH):

```shell
$ git clone git@github.com:ohmarinseries/finance-news-API.git
```
Then navigate to project:

```shell
$ cd finance-news-API
```

# Build

To start application you need to run following command:

####Required: You need to have docker desktop on your machine to run.

```shell
$ docker-compose up --build
```
Note: Also build will take a bit of time

# Use
Finance News API is an REST API for collecting news articles from Yahoo RSS Feed.
Scrapping Service is collecting data for AAPL, TWTR, INTC, GC=F (by default), but
can add additional symbols by sending request:

```http request
POST https://localhost:8080/news/symbols/
BODY:
{
'symbol': 'example-symbol'
}
```

Celery is fetching data every minute from Yahoo RSS Feed

To see symbols that data is being collected for send request to:

```http request
GET https://localhost:8080/news/symbols/
```

To see all scrapped articles send request to:

```http request
GET https://localhost:8080/news/articles/
```

Use query parameters page_size and page to navigate through pagination, example:

```http request
GET https://localhost:8080/news/articles/?page_size=5&page=3
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
