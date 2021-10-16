### This is an implementation of Alphavantage APIs
In this application, there are two APIs.
- GET /api/v1/quotes
    - This API fetches the latest BTC/USD conversion rate.
    - It first checks the cache for the data: if not available in cache, it fetches from the postges.
    - If postgres also does not contain the exchange rate: it calls the Alphavantage API to fetch the data, saves it in postgres and cache db and returns it
- POST /api/v1/quotes
    - This API fetches the latest exchange rate from Alphavantage APIs and returns it to the user after saving in postgres and cache.

The application also has a background scheduler which runs every hour at 10th minute in UTC and saves the latest data into postgres and caches it.
### How to run the application
- Install postgres and create a database called alphavantage after logging into postgres
                
                create database alphavantage;

- Install docker and docker compose
- In the project root folder and  alphavantage folder, copy .env.example to .env and enter your alphavantage key and your postgres password
- Run the docker using

                docker-compose -f docker-compose.yml build
                docker-compose -f docker-compose.yml up

- The application APIs can be used in postman or curl
- Postman collection for the APIs can be found in Alphavantage.postman.json, you can import and use them.