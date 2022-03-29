# Finance News API / Scrapper Service

## Setup
First thing to do is open your terminal

Then navigate to directory where you want the project to be cloned

Then clone the repository(using SSH):

```shell
git clone git@github.com:ohmarinseries/finance-news-API.git
```
Then navigate to cloned project:
```shell
cd finance-news-API
```

# Build
To deploy application locally you need to run following command:

####Required: You need to have docker desktop installed on your machine to deploy. Also docker desktop needs to be opened.

```shell
docker-compose up
```
####Note: Also build will take some time

If build was successful, inside your docker desktop app you will see 5 running containers. 

# Use
Finance News API is a Django based REST API for fetching scrapped news from Yahoo RSS Feed.
Scrapping Service is collecting data for AAPL, TWTR, INTC, GC=F (by default), but
you can add additional symbols.
To see symbols that data is being collected for send request to:

```http request
GET http://localhost:8080/news/symbols/
```
To add symbols for collection(example for Bitcoin news):
```http request
POST http://localhost:8080/news/symbols/
BODY:
{
'symbol': 'BTC'
}
```

Celery is scrapping data every minute from Yahoo RSS Feed

To see all scrapped articles(all symbols) send request to:

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
####Important: If you already executed docker-compose up --build, app has been tested during build!
```shell
python3 manage.py test financeAPI
```
