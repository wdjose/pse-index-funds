# Philippine Stock Exchange (PSE) Index Funds Comparison

_Unit Investment Trust Funds (UITF)_ are open-ended investment fund pools operated by a trustee (usually a bank) where investors can participate by buying units at the Net Asset Value per Unit (NAVPU) for the day. _Mutual Funds (MF)_, on the other hand, are corporations whose purpose is to invest the fund pool. Investors can participate by buying shares of the corporation at the Net Asset Value per Share (NAVPS). Finally, _Exchange-Traded Funds (ETF)_ are funds traded on the stock exchange (with its own ticker symbol); the ETF itself is invested by the issuer into underlying securities. Investors can participate by buying shares of the ETF on the stock exchange. 

Some UITFs and MFs are invested in the money market, some in bonds, and others in equities. In particular, __index funds__ are passive funds which seek to replicate the Philippine Stock Exchange Index (PSEi), which is a basket of 30 common stocks in the PSE. One would then expect the returns to also mimic the PSEi. There are some UITFs and MFs which are index funds. In the Philippines, there is only one ETF at the moment, and it is also an index fund. 

This notebook seeks to explore: are all PSEi index funds created equal? Which ones follow the PSEi most faithfully? When price appreciation and dividends of underlying stocks are taken into account, are UITFs / MFs / ETFs still good value for your money?

Index Funds / Indices Analyzed as of April 3, 2020:

| Fund / Index Name | Institution | Type |
| --- | --- | --- |
| BDO Equity Index Fund | BDO Unibank, Inc. | UITF |
| BDO PERA Equity Index Fund | BDO Unibank, Inc. | UITF |
| BPI Philippine Equity Index Fund | BPI Asset Management and Trust Corporation | UITF |
| CTBC Bank - Sun Life Philippines Stock Index Feeder Fund | CTBC Bank (Philippines) Corp. | UITF |
| EastWest PSEi Tracker Fund | EastWest Banking Corporation | UITF |
| Metro Philippine Equity Index Tracker Fund | Metropolitan Bank & Trust Co. | UITF |
| PNB Phil-Index Tracker Fund | Philippine National Bank | UITF |
| SB Philippine Equity Index Fund | Security Bank Corporation | UITF |
| UnionBank Philippine Equity Index Portfolio | UnionBank | UITF |
| UCPB Philippine Index Equity Fund | United Coconut Planters Bank | UITF |
| First Metro Save and Learn Philippine Index Fund | First Metro Asset Management, Inc. | MF |
| PAMI Equity Index Fund | Philam Asset Management, Inc. | MF |
| Philequity PSE Index Fund | Philequity Management, Inc. | MF |
| Philippine Stock Index Fund | BPI Investment Management, Inc. | MF |
| Sun Life Prosperity Philippine Stock Index Fund | Sun Life Asset Management Company, Inc. | MF |
| First Metro Equity Exchange-Traded Fund | First Metro Asset Management, Inc. | ETF |
| PSEi | Philippine Stock Exchange | Index |
| PSEi Total Return | Philippine Stock Exchange | Index |

<br />

---
Additional Notes on Index Funds Selection and Omission:
- ATRAM Philippine Equity Smart Index Fund was removed even though it has "Index" in its name, since it mentions in its information disclosure sheet that it combines elements of passive and active management.   
- LandBank Equity [Index] Fund was not included, since it seems LandBank is removing "Index" from the fund's name, and it wasn't mentioned anywhere in the fund information documents that it specifically tracks the PSEi.
- First Metro Save and Learn Philippine Index Fund was subsequently added to the list, since its fund information sheet says its goal is to track the index.




## Summary

From my qualitative analysis of the price data, the following funds which seem to be the best and worst performing are listed below. Otherwise, the rest of the funds are average and more or less track the PSEi closely. 

### Best-Performing Index Funds:

1. __First Metro Equity Exchange-Traded Fund (FMETF)__: Based on the plots, FMETF's performance is a positive outlier and has clearly outperformed the PSEi (not the PSEi TRI; this is explained in the Introduction section below). FMETF charges the lowest management fee at 0.50%, and comparing their stock holdings with stock holdings of other index funds, their composition seems to be the closest to the PSEi. I also speculate that when the bid-ask spread of FMETF in the PSE moves significantly away from the intra-day NAVPU (enough to overcome the stock transaction fee), First Metro buys (sells) shares at a discount (premium) at the detriment of the retail seller (buyer). These are probably the reasons why FMETF has the highest return among all index funds. 
1. __UCPB Philippine Index Equity Fund__: Based on the plots, this is actually the second-ranked among index funds, and consistently in the top 3. It even manages to beat the FMETF during the most recent downtrend. If FMETF has the lowest overall management fee, UCPB is one of the funds with the lowest management fee among UITFs at 0.75%. Other than that, I am unaware of why this fund would have better returns than the rest of the index funds. Maybe they might be more efficient to compete against bigger banks. 
1. __EastWest PSEi Tracker Fund__: In its early days, this EastWest index fund was just average and in the middle of the pack. However, in more recent years, it is among the top 2 and 3 index funds. This might also be due to its UITF-best management fee of 0.75%. The fund also declares a low tracking error (0.0002), which is better than FMETF's 0.04% (also self-declared). 
1. __UnionBank Philippine Equity Index Portfolio__: This UnionBank index fund does not particularly stand out as a positive outlier in the plots below, but it is a consistent 3rd or 4th placer, and consistently above the benchmark PSEi. Although it has an average management fee at 1%, it is still notable and has the potential to break away from the average funds. This is another relatively new fund that I'm keeping tabs on, since it might have improved performance as time goes on. 

### Worst-Performing Index Funds:

1. __First Metro Save and Learn Philippine Index Fund__: This First Metro Index Mutual Fund has the worst performance among all index funds. Even though it has the same supporting institution as FMETF, it is very perplexing to see such bad performance that I'm wondering if it really is an actively managed fund (and not an index fund). Nevertheless, I am adding this fund to the list to illustrate how some index funds are inherently bad in tracking the index.
1. __PNB Phil-Index Tracker Fund__: If FMETF is a positive outlier, then this PNB index fund is clearly a negative outlier. It is one of only three funds around for greater than 12 years, but it has miserably failed to track the PSEi compared to its contemporaries, Philequity PSE Index Fund and Philippine Stock Index Fund. There is some reason for hope though; during the past year, though its performance is still among the worst, it doesn't seem like an outlier anymore. 
1. __BDO PERA Equity Index Fund__: This is a special kind of UITF index fund since it serves only Personal Equity and Retirement Account (PERA) investments. Its biggest advantage is the fund's tax-exempt status, so this should yield a higher return than the regular BDO Equity Index Fund, right? Unfortunately, this is also clearly an negative outlier, and since inception it is even much worse than the PNB index fund. My guess is that since PERA is unpopular (probably due to weak marketing, pending implementing rules and regulations, and tedious application process), the fund size is too small that the expense ratio is much greater than their regular index fund. Indeed, according to the latest KIIDS, the PERA fund has a Net Asset Value (NAV) of only &#8369; 31M vs the regular fund's NAV of &#8369; 4.4B. I hope this improves in the future. 

### Caveats: 

1. The analysis is purely based on the Net Asset Value per Unit (NAVPU) or Net Asset Value per Share (NAVPS) of the index funds. Entry / exit costs, sales loads, transaction costs, early redemption fees, and bid-ask spreads (for FMETF) are not taken into account. 
1. The analysis also does not take into account dividends to investors, if any, except for the two stock dividends awarded by FMETF. However, as far as I am aware, the UITF and MF index funds do not give out dividends. 
1. The comparisons below against the PSEi Total Return Index (PSEi TRI) is not fully reliable, as price data only became available from February 1, 2019. Therefore, the funds' tracking performance against the PSEi TRI are mostly during the a sideways or downtrend market. 

I will try to improve the analysis in the future with updated data and more comparisons. I am trying to replicate how the funds computed the tracking error; it seems I am getting different values, even though I am computing based on the original paper definition here: [Determinants of Tracking Error for Equity Portfolios](https://joi.pm-research.com/content/13/2/37/tab-article-info). 




## Introduction

There are a lot of equity UITFs and MFs in the Philippines, but only a handful of equity index funds (listed in the table above). I classified UITFs and MFs as index funds if their fund information sheet explicitly notes that they track the index by buying component stocks of the PSEi with the same weight. Index funds are classified as passive funds, since the fund managers do not need to do their due diligence with each individual stock's performance, and only have to ensure the stock weights are as close as possible to the PSEi. 

In contrast, all other equity funds can be considered as "active funds" since the fund manager has the discretion to choose different weights, or different stocks altogether. In practice, many equity funds still closely mirror the PSEi (possibly due to liquidity reasons), but they may decide otherwise from time to time. There are other equity funds who focus investments on specific market sectors, dividend plays, or conviction stocks. These active funds may have higher or lower returns than the index depending on the fund managers' skill, luck, and timing, and hence are not the focus of comparison here. 

Going back to index funds: how do index funds earn? The PSEi only tracks the prices of the underlying stocks. However, many of these stocks give out dividends to shareholders. When a stock or cash dividend is paid out to shareholders, the stock's price drops the same amount to take into account the "transfer of value". As far as I know, stock dividends are treated similar to stock splits; hence, it is automatically applied to the price history and will have no effect on the PSEi. However, cash dividends are paid directly to shareholders. This amount lowers the PSEi, but the value of cash dividends are not considered when computing the PSEi. 

Because of this, investors actually earn in two ways: first, via stock price appreciation (i.e. buy low, sell high); and second, via cash dividends. Since most index funds only track the PSEi's performance, it means that the funds still receive the cash dividends and add these to the Net Asset Value (NAV). This means that they actually have additional earnings which help them track the PSEi. 

The PSE has actually tried to address this (similar with other countries) by releasing a new index: the PSEi Total Return Index (PSEi TRI). This index takes into account both the stock prices of the underlying stocks, and the cash dividends distributed by the stocks. Technically, index funds should be tracking the PSEi TRI instead of just the PSEi, but it would make their fund performance look worse. This is also the reason why some index funds like the FMETF beat the PSEi; this is because index funds add the cash dividends to their NAV. When compared against the PSEi TRI, the FMETF is actually underperforming (see analysis in the sections below). But this also means that other index funds are performing even worse. 

In practice, although index funds might have additional income from cash dividends, they have additional expenses due to:

- Management / trust fees
  - Compared to index funds in the US market (as low as 0.03%), management fees of index funds in the Philippines 
- Stock transaction fees
  - These are incurred when rebalancing fund portfolios, or when investors participate and withdraw from the fund. 
  - Again, these are also quite expensive in the Philippines, with a mandated minimum broker's commission, taxes, and miscellaneous fees. 
- Bid-ask spreads and mandated price increments
  - Due to relatively illiquid market conditions in the PSE, bid-ask spreads make large volume transactions difficult to execute without affecting price.
  - Compared to the US market, price increments in the PSE are much larger steps and are equivalent to "discretization error". 
- Imperfect stock index weights replication
  - This is due to minimum board lot and lot size restrictions and stock transaction fees again. 
- Trustee, custodianship, and external auditor fees
- Non-real-time rebalancing (compared to the PSEi itself)

Hence, for most funds, the earnings from the dividends actually cancel out the additional expenses incurred by the fund. In practice, this means that most index funds closely follow the PSEi even with the expensive management fees in the Philippines (. 




## Data Sources

The price data were gathered from each funds' inception date up to April 3, 2020 so far. Raw price data (in JSON format) can be found on my GitHub page: https://github.com/wdjose/pse-index-funds/. These were extracted / downloaded from:

- For all UITFs: http://www.uitf.com.ph
  - Exact URL: http://www.uitf.com.ph/fund-matrix.php
  - I performed web scraping to extract the pricing data. 
  - No terms and conditions regarding web scraping was found on the website. 
- For Philequity PSE Index Fund [MF]: https://www.philequity.net
  - Exact URL: https://www.philequity.net/pefi_historicalnavps.php
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
  - I performed web scraping to extract the pricing data. Stock price adjustment was done to take into account two stock dividends given by FMETF in 2017 and 2018. 
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
  
