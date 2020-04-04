# Philippine Stock Exchange (PSE) Index Funds Comparison

UITFs are open-ended investment fund pools . Some UITFs are invested in the money market, some in bonds, and others in equities. In particular, so-called "index funds" are passive funds which seek to replicate the Philippine Stock Exchange Index (PSEi), which is a basket of 30 common stocks in the PSE. One would then expect the returns to also mimic the PSEi. 

This notebook seeks to explore: are all PSEi index funds created equal? Which ones follow the PSEi most faithfully? When price appreciation and dividends of underlying stocks are taken into account, are UITFs / MFs / ETFs still good value for your money?

Index Funds / Indices Analyzed:

Fund / Index Name | Institution | Type 
--- | --- | ---
ATRAM Philippine Equity Smart Index Fund | ATRAM Trust Corporation | UITF
BDO Equity Index Fund | BDO Unibank, Inc. | UITF
BDO PERA Equity Index Fund | BDO Unibank, Inc. | UITF
BPI Philippine Equity Index Fund | BPI Asset Management and Trust Corporation | UITF
CTBC Bank - Sun Life Philippines Stock Index Feeder Fund | CTBC Bank (Philippines) Corp. | UITF
EastWest PSEi Tracker Fund | EastWest Banking Corporation | UITF
Metro Philippine Equity Index Tracker Fund | Metropolitan Bank & Trust Co. | UITF
PNB Phil-Index Tracker Fund | Philippine National Bank | UITF
SB Philippine Equity Index Fund | Security Bank Corporation | UITF
UnionBank Philippine Equity Index Portfolio | UnionBank | UITF
UCPB Philippine Index Equity Fund | United Coconut Planters Bank | UITF
First Metro Save and Learn Equity Fund | First Metro Asset Management, Inc. | MF
PAMI Equity Index Fund | Philam Asset Management, Inc. | MF
Philequity PSE Index Fund | Philequity Management, Inc. | MF
Philippine Stock Index Fund | BPI Investment Management, Inc. | MF
Sun Life Prosperity Philippine Stock Index Fund | Sun Life Asset Management Company, Inc. | MF
First Metro Equity Exchange-Traded Fund | First Metro Asset Management, Inc. | ETF
PSEi | Philippine Stock Exchange | Index
PSEi Total Return | Philippine Stock Exchange | Index

## Data Sources

- For all UITFs: http://www.uitf.com.ph
  - Exact URL: http://www.uitf.com.ph/fund-matrix.php
  - I performed web scraping to extract the pricing data. 
  - No terms and conditions regarding web scraping was found on the website. 
- For First Metro Save and Learn Equity Fund [MF]: https://fami.com.ph
  - Exact URL: https://fami.com.ph/mutual-fund/save-learn-equity-fund
  - I performed web scraping to extract the pricing data. 
  - No terms and conditions regarding web scraping were found on the website. 
- For PAMI Equity Index Fund [MF]: https://www.philamfunds.com
  - Exact URL: https://www.philamfunds.com/en/our-products/equity/pami-equity-index-fund.html
  - I directly copy-pasted the prices, which Philam releases without restrictions. 
  - No terms and conditions regarding web scraping were found on the website, only copyright claims allowing for personal/non-commercial use. 
- For Philequity PSE Index Fund [MF]: https://www.philequity.net
  - Exact URL: https://www.philequity.net/pefi_historicalnavps.php
  - I performed web scraping to extract the pricing data. 
  - No terms and conditions regarding web scraping were found on the website. 
- For Philippine Stock Index Fund [MF]: https://www.alfmmutualfunds.com
  - Exact URL: https://www.alfmmutualfunds.com/#fund_tracking_result
  - performed web scraping to extract the pricing data. 
  - No terms and conditions regarding web scraping were found on the website. 
- For Sun Life Prosperity Philippine Stock Index Fund [MF]: https://www.sunlife.com.ph
  - Exact URL: https://www.sunlife.com.ph/PH/Investments/NAVPS
  - I performed web scraping to extract the pricing data. 
  - No terms and conditions regarding web scraping were found on the website, only copyright claims allowing for personal/non-commercial use. 
- For First Metro Equity Exchange-Traded Fund [ETF]: https://fami.com.ph
  - Exact URL: https://fami.com.ph/first-metro-exchange-traded-fund
  - I performed web scraping to extract the pricing data. 
  - No terms and conditions regarding web scraping were found on the website. 
- For the PSEi: https://finance.yahoo.com
  - Exact URL: https://finance.yahoo.com/quote/PSEI.PS/history
  - Yahoo Finance is actually the easiest to extract data from (hence, my favorite), as they allow you download historical data up to the maximum they have stored. The PSEi data I downloaded started in January 2, 1987. 
  - No terms and conditions regarding web scraping were found on the website. 
- For the PSEi Total Return (TRI): https://pse.com.ph
  - Exact URL: https://pse.com.ph/stockMarket/marketInfo-marketActivity.html?tab=5
  - Official market data is under Market Activity -> Index History -> PSEi Total Return
  - Unfortunately, PSE only publishes the most recent 30 days historical data. I gathered the rest of the data from: https://economicsmbw.blogspot.com, who has fortunately posted 30-day screenshots of the PSEi TRI from February 2019 to January 2020. 
  - mbwECONOMICS+ does not have records for April 2019 and February 2020 (at the moment)
  - I substituted data from the official Facebook page of the PSE: https://www.facebook.com/PhStockExchange. From the archived posts, I was able to deduce the entire April 2019 PSEi TRI except for April 23, 2019. I interpolated this from the April 22, 2019 data, and the corresponding PSEi for April 22 and 23. 
  - For February 2020, I do not have exact data for February 1-18, 2020 (when I visited pse.com.ph, remaining data is only up to February 19, 2020). While waiting for the post of mbwECONOMICS+, I also interpolated the PSEi TRI data here from January 31, 2020 and February 19, 2020, as well as the PSEi data from February 1-18, 2020. Validated against February 19, 2020, the relative error is only around 0.02%, so the interpolation is acceptable. 
  - Copyright claims were found on the website, allowing for personal/non-commercial use. 