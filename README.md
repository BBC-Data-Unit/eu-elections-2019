# 2019 European elections: How many new MEPs might you get?

![](https://ichef.bbci.co.uk/news/624/cpsprodpb/8854/production/_106900943_meppay-nc.png)

In May 2019 we [published an analysis of data relating to the upcoming EU elections](https://www.bbc.co.uk/news/uk-england-48202795), "some facts and figures about the choice voters have about who represents them in Brussels and Strasbourg."

The article was based on a range of analysis, including combining ONS data with information on MEP wages; a Python-based Twitter scraper and analysis in R; collating names and using a names gender API; and generating some visualisation using R.

## Get the data 

* European Parliament: [Salaries and pensions](https://www.europarl.europa.eu/news/en/faq/13/salaries-and-pensions); [European elections: What pay can UK MEPs expect?](https://www.bbc.co.uk/news/uk-politics-48037162)
* BBC: [2019 European elections: List of candidates](https://www.bbc.co.uk/news/uk-politics-48081172)
* Spreadsheet: [MEPs standing and not standing](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/MEPS%20STANDING%20NOT%20STANDING%20CHECKED.xlsx)
* ONS: [Employee earnings in the UK: 2018](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2018)
* Spreadsheet: [Matching earnings by region against MP salaries](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/DATA%20FOR%20CHARTS.xlsx)
* CSV: [MEP pay versus regional average](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/mepspay.csv)
* European Parliament: [Turnout and gender factsheet (PDF)](https://www.europarl.europa.eu/RegData/etudes/BRIE/2018/614733/EPRS_BRI(2018)614733_EN.pdf)
* CSV: [Turnout by country](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/mepturnout.csv)
* CSV: [Female MEPs by country](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/femalemeps.csv)
* Spreadsheet: [MP names' gender - API results, analysis and checking](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/candidatesnamesGENDEREDapi.xlsx)
* Spreadsheet: [Checking numbers of candidates by party and region](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/candidates%20check.xlsx)
* CSV: [UK MEP Twitter accounts](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/ukmepaccounts.csv)
* CSV: [Word frequency comparison, lower case versus original case](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/wordfrequpperandlower.csv) - this was used to check whether terms like 'EU' and 'UK' were from URLs or being used in reference to geography
* Two datasets - 180,001 scraped tweets, and a dataset of all tweets by MEPs in the ast 12 months - are too large to include here
* Spreadsheet: [analysis of election spending data from Electoral Commission (not used in the final story)](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/Euro%20Campaign%20Spending%20last3.xlsx)
* CSV: [Donations during 2014 European election period](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/donations%20during%20euro%202014%20period.csv) (unused, as it is not possible to distinguish between donations for EU or other elections)

## Quotes and interviews

* Julie Girling, independent MEP for the South West
* Mary Honeyball, Labour Party MEP for London

## Visualisation

* Table: Number of parties standing vs number of seats for each region
* Table: MEPs standing down by region
* Lollipop chart: MEPs' pay compared with regional averages
* Bar chart: Most common words tweeted by UK MEPs
* Bar chart: Percentage of MEPs that are female by member state
* Bar chart: Turnout in European elections 2014 by member state

## Code and scripts

* [Twitter scraper](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/meptwitterscraper.py): the first part collects accounts from a list; the second part scrapes the most recent 3,300 tweets by each account on a list
* [R Markdown: analysing MEP tweets](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/meptweets.Rmd)
* [Shell script: generating a word count from a text file](https://github.com/BBC-Data-Unit/eu-elections-2019/blob/master/wordfreq.sh) (unused). *Note: the text file is created by changing the .csv extension to .txt*
