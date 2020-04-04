#!/usr/bin/env python
# coding: utf-8

# # Index Fund Data Processing
# 
# This notebook contains code for data scraping and formatting of index fund prices into time-series JSON files. Index funds processed include Unit Investment Trust Funds (UITF), Mutual Funds (MF), and Exchange-Traded Funds (ETF) which are invested in the Philippine Stock Exchange, track the Philippine Stock Exchange Index (PSEi), and whose portfolios track the PSEi composition. In addition, this notebook also downloads and processes the PSEi and the PSEi Total Return Index (PSEi TRI) time-series prices as benchmarks so the index funds' performances can be compared. 

# In[1]:


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime


# In[2]:


overwrite_uitf = False
overwrite_mf = False
overwrite_etf = False
overwrite_index = False

print_json = False


# ## Unit Investment Trust Fund (UITF) Data Extraction
# 
# The code below extracts the list of peso equity funds from uitf.com.ph, and upon user selection, will extract the entire price history of the selected fund. Output is a JSON file containing key-value pairs of "Date": "NAVPU". 
# 
# The UITFs included in this analysis are hand-picked below to be specifically "index funds"; their fund information sheets should specifically note that the portfolio track the PSEi composition. 
# 
# These funds are: 
# - BDO Equity Index Fund
# - BDO PERA Equity Index Fund
# - BPI Philippine Equity Index Fund
# - CTBC Bank - Sun Life Philippine Stock Index Feeder Fund
# - EastWest PSEi Tracker Fund
# - PNB Phil-Index Tracker Fund
# - SB Philippine Equity Index Fund
# - UnionBank Philippine Equity Index Portfolio
# - UCPB Philippine Index Equity Fund

# In[3]:


# URL containing list of Peso equity UITFs
uitf_fund_list_url = "http://www.uitf.com.ph/fund-matrix.php?sortby=bank&sortorder=asc&class_id=1&currency=PHP&btn=Filter"


# In[4]:


# We GET from the URL above, and parse the HTML document to get the 4th <table>

response = requests.get(uitf_fund_list_url)

soup = BeautifulSoup(response.content)
table = soup.find_all('table')[3]


# In[5]:


# We parse the HTML <table> and convert it to a Pandas dataframe
# The dataframe's columns are: 'Bank', 'Fund Name', 'Bank ID', 'Fund ID'
# The 'Bank ID' and 'Fund ID' are parsed from the 'View' GET request per row

for row in table.find_all('tr'):
  th_tags = row.find_all('th')
  if len(th_tags) > 0:
    column_names = [" ".join(th.get_text().split()) for th in th_tags]
    uitf_fund_list = pd.DataFrame(columns=(column_names + ["Bank ID", "Fund ID"]))
  td_tags = row.find_all('td')
  if len(td_tags) > 0:
    row_append = pd.Series([" ".join(td.get_text().split()) for td in td_tags], column_names)
    
    get_attrs = td_tags[-1].find('a').attrs['href'].split('?')[1].split('&')
    fund_id = int(get_attrs[0].split('=')[1])
    bank_id = int(get_attrs[1].split('=')[1])
    bank_fund_id = pd.Series([bank_id, fund_id], ["Bank ID", "Fund ID"])

    row_append = row_append.append(bank_fund_id)

    uitf_fund_list = uitf_fund_list.append(row_append, ignore_index=True)

uitf_fund_list = uitf_fund_list[['Bank', 'Fund Name', 'Bank ID', 'Fund ID']]


# In[6]:


# This is a manual selection (i.e. human-selected) of index equity funds from:
# uitf_fund_list[["Bank", "Fund Name"]].to_numpy().tolist()

index_fund_name = [['BDO Unibank, Inc.', 'BDO EQUITY INDEX FUND'],
 ['BDO Unibank, Inc.', 'BDO PERA EQUITY INDEX FUND'],
 ['BPI Asset Management and Trust Corporation', 'BPI Philippine Equity Index Fund'],
 ['CTBC Bank (Philippines) Corp.', 'CTBC Bank - Sun Life Philippine Stock Index Feeder Fund'],
 ['EastWest Banking Corporation', 'EastWest PSEI Tracker Fund'],
 ['Metropolitan Bank & Trust Co.', 'Metro Philippine Equity Index Tracker Fund'],
 ['Philippine National Bank', 'PNB PHIL-INDEX TRACKER FUND(formerly PNB ENHANCED PHIL-INDEX REFERENCE FUND)'],
 ['Security Bank Corporation', 'SB PHILIPPINE EQUITY INDEX FUND'],
 ['Union Bank', 'UnionBank Philippine Equity Index Portfolio'],
 ['United Coconut Planters Bank', 'UCPB Philippine Index Equity Fund']]

index_fund_name = set(tuple(x) for x in index_fund_name)

uitf_index_fund_list = uitf_fund_list[uitf_fund_list.apply(lambda x: (tuple([x['Bank'], x['Fund Name']]) in index_fund_name), axis=1)].reset_index(drop=True)

uitf_index_fund_list['Fund Name'] = uitf_index_fund_list['Fund Name'].replace(
    'BDO EQUITY INDEX FUND', 'BDO Equity Index Fund').replace(
    'BDO PERA EQUITY INDEX FUND', 'BDO PERA Equity Index Fund').replace(
    'EastWest PSEI Tracker Fund', 'EastWest PSEi Tracker Fund').replace(
    'PNB PHIL-INDEX TRACKER FUND(formerly PNB ENHANCED PHIL-INDEX REFERENCE FUND)', 'PNB Phil-Index Tracker Fund').replace(
    'SB PHILIPPINE EQUITY INDEX FUND', 'SB Philippine Equity Index Fund')


# In[7]:


fmonth = '01'
fday = '01'
fyear = '1970'
tmonth = '12'
tday = '31'
tyear = '2030'

data_dir = 'data'
if not os.path.exists(data_dir):
  os.makedirs(data_dir)


# In[8]:


for index_fund in list(uitf_index_fund_list.iterrows()):
  bank_id = index_fund[1]['Bank ID']
  fund_id = index_fund[1]['Fund ID']

  timeseries_url = 'http://www.uitf.com.ph/daily_navpu_details_json.php?bank_id={}&fund_id={}&fmonth={}&fday={}&fyear={}&tmonth={}&tday={}&tyear={}&btn=Filter'.format(
      bank_id, fund_id, fmonth, fday, fyear, tmonth, tday, tyear
  )

  response = requests.get(timeseries_url)
  navpu_list = [tuple(reversed(x.replace('NAVpu : <b>', '').replace('</b>', '').replace('Date : ', '').split('<br>'))) for x in json.loads(response.content)['thlabels']]
  
  if print_json:
    print(index_fund[1]['Fund Name'])
    print(json.dumps(dict(navpu_list)))
    print('')
  
  json_file = os.path.join(data_dir, index_fund[1]['Fund Name'] + '.json')
  
  if not os.path.isfile(json_file) or overwrite_uitf:
    with open(json_file, 'w') as f:
      json.dump(dict(navpu_list), f)
  


# In[9]:


# Fix data from 'PNB Phil-Index Tracker Fund'
raw_file = os.path.join(data_dir, 'PNB Phil-Index Tracker Fund' + '.json')
with open(raw_file, 'r') as f:
  raw_dict = json.loads(f.readline().strip())
raw_dict.pop(' 26, 2016', None)
with open(raw_file, 'w') as f:
  json.dump(raw_dict, f)


# ## Mutual Fund (MF) Data Extraction
# 
# The MF data was scraped using other tools; this section will transform the raw price data into the standard JSON file format used in the UITF section above. 
# 
# The MFs included in this analysis are hand-picked below to be specifically "index funds"; their fund information sheets should specifically note that the portfolio track the PSEi composition. 
# 
# These funds are: 
# - PAMI Equity Index Fund
# - Philequity PSE Index Fund
# - Philippine Stock Index Fund
# - Sun Life Prosperity Philippine Stock Index Fund

# In[10]:


raw_data_dir = 'raw-data'
data_dir = 'data'
if not os.path.exists(data_dir):
  os.makedirs(data_dir)


# In[11]:


# PAMI Equity Index Fund

fund_name = 'PAMI Equity Index Fund'
raw_file = os.path.join(raw_data_dir, fund_name + '.txt')
json_file = os.path.join(data_dir, fund_name + '.json')

navps = dict()
with open(raw_file, 'r') as f1:
  line_list = reversed(f1.readlines())

for line in line_list:
  line = line.strip()
  date = line.split('\t')[0]
  date = datetime.strptime(date, '%Y-%m-%d').strftime('%b %-d, %Y')
  price = line.split('\t')[1][:-1]
  navps[date] = price

if print_json:
  print(fund_name)
  print(json.dumps(navps))
  print('')

if not os.path.isfile(json_file) or overwrite_mf:
  with open(json_file, 'w') as f2:
    json.dump(navps, f2)


# In[12]:


# Philequity PSE Index Fund

fund_name = 'Philequity PSE Index Fund'
raw_file = os.path.join(raw_data_dir, fund_name + '.txt')
json_file = os.path.join(data_dir, fund_name + '.json')

navps = dict()
with open(raw_file, 'r') as f1:
  line_list = f1.readlines()[1:]

for line in line_list:
  line = line.strip()
  date = line.split('\t')[0]
  date = datetime.strptime(date, '%Y-%m-%d').strftime('%b %-d, %Y')
  price = line.split('\t')[1]
  navps[date] = price

if print_json:
  print(fund_name)
  print(json.dumps(navps))
  print('')

if not os.path.isfile(json_file) or overwrite_mf:
  with open(json_file, 'w') as f2:
    json.dump(navps, f2)


# In[13]:


# Philippine Stock Index Fund

fund_name = 'Philippine Stock Index Fund'
raw_file = os.path.join(raw_data_dir, fund_name + '.txt')
json_file = os.path.join(data_dir, fund_name + '.json')

navps = dict()
with open(raw_file, 'r') as f1:
  raw_dict = json.loads(f1.readline().strip())

date_list = raw_dict['category']
price_list = raw_dict['values']

for i in range(len(date_list)):
  date = date_list[i]
  date = datetime.strptime(date, '%Y-%m-%d').strftime('%b %-d, %Y')
  price = "{}".format(price_list[i])
  navps[date] = price

if print_json:
  print(fund_name)
  print(json.dumps(navps))
  print('')

if not os.path.isfile(json_file) or overwrite_mf:
  with open(json_file, 'w') as f2:
    json.dump(navps, f2)


# In[14]:


# Sun Life Prosperity Philippine Stock Index Fund

fund_name = 'Sun Life Prosperity Philippine Stock Index Fund'
raw_file = os.path.join(raw_data_dir, fund_name + '.txt')
json_file = os.path.join(data_dir, fund_name + '.json')

navps = dict()
with open(raw_file, 'r') as f1:
  line_list = f1.readline().strip()[3:-3].split('\'), (\'')

for line in line_list:
  line = line.strip()
  date = line.split('\', \'')[0]
  date = datetime.strptime(date, '%b %d, %Y').strftime('%b %-d, %Y')
  price = line.split('\', \'')[1]
  navps[date] = price

if print_json:
  print(fund_name)
  print(json.dumps(navps))
  print('')

if not os.path.isfile(json_file) or overwrite_mf:
  with open(json_file, 'w') as f2:
    json.dump(navps, f2)


# ## Exchange-Traded Fund (ETF) Data Extraction
# 
# The ETF data was also scraped using other tools; this section will transform the raw price data into the standard JSON file format used in the UITF and MF sections above. 
# 
# Currently, there is only one ETF in the PSE, and it specifically tracks the PSEi composition; hence, it is an index fund. 
# 
# This fund is: 
# - First Metro Equity Exchange-Traded Fund

# In[15]:


raw_data_dir = 'raw-data'
data_dir = 'data'
if not os.path.exists(data_dir):
  os.makedirs(data_dir)


# In[16]:


# First Metro Equity Exchange-Traded Fund

fund_name = 'First Metro Equity Exchange-Traded Fund'
raw_file = os.path.join(raw_data_dir, fund_name + '.txt')
json_file = os.path.join(data_dir, fund_name + '.json')

navps = dict()
with open(raw_file, 'r') as f1:
  line_list = f1.readline().strip()[2:-2].split('],[')

for line in line_list:
  line = line.strip()
  date = int(line.split(',')[0]) // 1000
  date = datetime.utcfromtimestamp(date).strftime('%b %d, %Y')
  price = line.split(',')[1]
  navps[date] = price

if print_json:
  print(fund_name)
  print(json.dumps(navps))
  print('')

if not os.path.isfile(json_file) or overwrite_etf:
  with open(json_file, 'w') as f2:
    json.dump(navps, f2)


# ## PSEi and PSEi TRI Data Extraction
# 
# The PSEi and PSEi TRI were also scraped / downloaded using other tools and sources. This section will transform the raw price data into the standard JSON file format used in the UITF, MF, and ETF sections above. 

# In[17]:


raw_data_dir = 'raw-data'
data_dir = 'data'
if not os.path.exists(data_dir):
  os.makedirs(data_dir)


# In[18]:


# PSEi

fund_name = 'PSEi'
raw_file = os.path.join(raw_data_dir, fund_name + '.txt')
json_file = os.path.join(data_dir, fund_name + '.json')

navps = dict()
with open(raw_file, 'r') as f1:
  line_list = f1.readlines()[1:]

for line in line_list:
  line = line.strip()
  date = line.split(',')[0]
  date = datetime.strptime(date, '%Y-%m-%d').strftime('%b %-d, %Y')
  price = line.split(',')[1]
  navps[date] = price

if print_json:
  print(fund_name)
  print(json.dumps(navps))
  print('')

if not os.path.isfile(json_file) or overwrite_index:
  with open(json_file, 'w') as f2:
    json.dump(navps, f2)


# In[19]:


# PSEi Total Return

fund_name = 'PSEi Total Return'
raw_file = os.path.join(raw_data_dir, fund_name + '.txt')
json_file = os.path.join(data_dir, fund_name + '.json')

navps = dict()
with open(raw_file, 'r') as f1:
  line_list = f1.readlines()

for line in line_list:
  line = line.strip()
  date = line.split('\t')[0]
  date = datetime.strptime(date, '%m/%d/%Y').strftime('%b %-d, %Y')
  price = line.split('\t')[1]
  navps[date] = price

if print_json:
  print(fund_name)
  print(json.dumps(navps))
  print('')

if not os.path.isfile(json_file) or overwrite_index:
  with open(json_file, 'w') as f2:
    json.dump(navps, f2)

