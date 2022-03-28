# Financial News API / Scrapper Service

## Setup

The first thing to do is to clone the repository:

```shell
$ git clone git@github.com:ohmarinseries/finance-news-API.git
```
Then navigate to project:

```shell
$ cd finance-news-API
```

# Build 

To start application you need to run following command:

Note: You need to have docker desktop on your machine to run

```shell
$ docker-compose up -build
```

# Walkthrough
Finance News API is an REST API for collecting news articles from Yahoo RSS feed.
Scrapping Service is collecting data for AAPL, TWTR, INTC, GC=F (by default), but
can add additional symbols you need to send request:

```http request
POST https://localhost:8080/news/symbols/
```

To see symbols that data is being collected for send:

```http request
GET https://localhost:8080/news/symbols/
```

To see all saved articles sent request to:

```http request
GET https://localhost:8080/news/articles/
```

Use query parameters page_size and page to use pagination, example:

```http request
GET https://localhost:8080/news/articles/?page_size=5&page=3
```

#Run Tests
To run tests for application run the following command:
```shell
python3 manage.py test financialAPI
```
