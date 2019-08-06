
# Performance Metrics
Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting. Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system. It is expected to be stored and processed in a relational database of your choice.

Sample dataset: https://gist.github.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/

## Client of this API should be able to:

filter by time range (date_from / date_to is enough), channels, countries, operating systems
group by one or more columns: date, channel, country, operating system
sort by any column in ascending or descending order
see derived metric CPI (cost per install) which is calculated as cpi = spend / installs
Please make sure that the client can use filtering, grouping, sorting at the same time.

## Common API use cases:

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order. Hint:
``` bash
=> select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from sampledataset where date <= '2017-06-01' group by channel, country order by clicks desc;
     channel      | country | impressions | clicks 
------------------+---------+-------------+--------
 adcolony         | US      |      532608 |  13089
 apple_search_ads | US      |      369993 |  11457
 vungle           | GB      |      266470 |   9430
 vungle           | US      |      266976 |   7937
 ...
 ```
 ```bash
 /api/performance_metrics?date_to=01-06-2017&group_by=channel&sort_by=-clicks
 ```
2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
``` bash
    /api/performance_metrics?date_from=01-05-2017&date_to=31-05-2017&os=ios&group_by=os=sort_by=+revenue
```
3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
``` bash
   /api/performance_metrics?date_from=01-06-2017&os=ios&group_by=os=sort_by=-revenue
```
4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.
``` bash
   /api/performance_metrics?country=CA&group_by=channel&sort_by=+cpi
```
Please make sure you have single API endpoint that is compliant with all use-cases described above and explicitly specify urls for each of 4 cases in your Readme.

We expect it to be written in the way so that it could go in production and be maintained by your teammates. Clean code is your CV.

Please have in mind that we use Python 3 and Django. Don't spend any time on Docker.

Feel free to ask me a question on skype vitaliy.kotik.

## Assumptions / Improvements to be done
- Filter is on single value for a field. for example: ***channels=a,b,c*** is not possible as per the current implementation. Instead *channel=a* is possible
- Column preferences - request arguments to accept the columns to be returned. For eg: ***columns=cpi,channel,date,country*** will return all the columns mentioned in the columns argument. Default columns would be all the columns: ***date,channel,country,os,impressions,clicks,installs,spend,revenue,cpi***

- Date format is - ***DD-MM-YYYY*** as per the implementation. 


When ready, please share your private repository with https://github.com/kotik