
![https://en.wikipedia.org/wiki/Raspberry_Pi](https://en.wikipedia.org/wiki/Raspberry_Pi)

### Create bash script to activate env and run spider
 
    #!/usr/bin/env bash

    source /home/pi/Documents/Scrape/bin/activate
    cd /home/pi/Documents/Scrape/Scrapy19/jobz/spiders
    scrapy crawl jobzspider
----

### Schedule in CRON

    # For example, you can run a backup of all your user accounts
    # at 5 a.m every week with:
    0 15 * * * ~/Documents/Scrape/Scrapy19/jobz/spiders/cj.sh
    # 
    # For more information see the manual pages of crontab(5) and cron(8)
    # 
    # m h  dom mon dow   command

---
OUTPUT 3 days later...

    jobs=# select posted from listings group by 1;
    posted   
    ------------
    2021-06-04
    2021-06-05
    2021-06-06
    (3 rows)****
--------------------------

