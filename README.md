# Fear and Greed
### The Impacts of Covid-19 on worldwide economic performance, social sentiment and asset prices

![Fear and Greed](https://www.simplifiedblogs.com/wp-content/uploads/2021/07/Red-and-Black-Dark-Gamer-Sports-YouTube-Outro-12-1.jpg)

***Authors: Aidan Laird, Arkie Ariyana, Mitchell Langdon***

January 2022

---

## Objectives of this report

The following report combines Covid-19 data alongside key economic data, social sentiment data and asset price data from various data sources to test a number of questions surrounding the impacts of Covid-19 globally. The report will answer the following questions:
 * Is the increase in Covid-19 cases correlated with greed in the cryptocurrency market and stockmarket?
 * Has Covid-19 impacted per capita GDP growth and inflation?
 * What are the top ten nations with the most Covid-19 cases? Do these same countries feature in the top 10 nations with the highest economic growth? 
 * Are future predictions of various cryptocurrencies (Bitcoin and Ethereum) aligned to predictions against the S & P 500 stockmarket index?

 ## Approach

 The report utilises data from a number of different sources. These include:

 | Data | Source| Structure|
| ----------- | ---------- | ---------|
| Covid-19 Data | [John Hopkins University](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2022.csv) | Static (CSV)|
| GDP and Inflation Data | [Trading Economics](https://tradingeconomics.com/)| Static (CSV)| 
| Cryptocurrency Data | [CoinGecko](https://www.coingecko.com/en) | API Connection |
| Fear Greed Index | [RapidAPI](https://rapidapi.com/rpi4gx/api/fear-and-greed-index/details) | API Connection |

## Methods Utilised in this report

The report utilises the primary python modules (e.g. pandas, numpy, datetime etc). To make use of additional Python modules, the team have utilised Python *Dash*; an interactive dashboarding module to better present data that can rival its Business Intelligence counterparts (Tableau, Power BI). The use of *fbprohpet*, a time-series forecasting tool was also utilised to broadly predict the direction of specific assets relating to equities and cryptocurrencies.

## Approach

To produce the final dashboard, the team conducted a phased approach to preparing the final dashboard output:

 (1) Data cleaning and preparation: the final dashboard uses data from various different data sources and therefore needed to be prepared accordingly. This can be identifed in the *Data Preparation.ipynb* file.

 (2) Structuring the layout of the dashboard/report: using Python's *Dash* module, the group produced a single page layout to answer separate questions related to a particular piece of analysis. 

## How the dashboard operates

The dashboard is operated locally, meaning that accessibility is a challenge given the creators' computers must be running in order to use the tool. 