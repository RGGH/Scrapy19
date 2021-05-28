## Scrapy To Postgresql for ML / NLP

### Notes:
  - Run as 'scrapy crawl' not via crawler process, as pipelines don't work with crawler process
  - Make sure columns in Postgres have large enough varchar() for long urls
  - written with Python 3.9.5
  - If you are coming from MySQL, change port to 5432 !
  - Keep search small, as the site has 'load more' (not AJAX/JSON) so will not work from scrapy
  

