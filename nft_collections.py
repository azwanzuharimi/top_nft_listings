# -*- coding: utf-8 -*-
"""nft_collections.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1455HvD-oxAZ4DKINV6HzCF-GeEvt3iXv
"""

# !pip install -q scrapy

# %config IPCompleter.use_jedi = False
import pandas as pd
import numpy as np
import scrapy
from scrapy.selector import Selector
import re
import requests
import json

def get_listings():
  url = 'https://coinmarketcap.com/nft/collections/'
  req = requests.get(url)

  total_listings = Selector(text=req.content).css('p.sc-1eb5slv-0.hykWbK::text').get()
  total_listings = int(re.findall('\d+', total_listings)[-1])
  print(f'There are {total_listings} total listings ')

  nfts = requests.get(f'https://api.coinmarketcap.com/data-api/v3/nft/collections?start=0&limit={total_listings}&sort=volume&desc=true&period=4')

  df = pd.json_normalize(json.loads(nfts.text), ['data', 'collections'] ).drop('rank', axis=1).sort_values('volumeAT', ascending=False).reset_index(drop=True)

  return df

# get_listings().to_csv('nft.csv', index=False)









